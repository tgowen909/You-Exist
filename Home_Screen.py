# ============================================================
#  You Exist: home screen
#  Shows a menu before the game starts: Play, Achievements, Quit.
#  Use the arrow keys (or the number keys) and Enter. Esc or Q goes back.
#
#  Runs (for later): the save file can already hold several "runs" at once.
#  Once the game can save its progress (see save_checkpoint at the bottom),
#  Play will automatically offer to continue any unfinished run, or start a new one.
# ============================================================

import os
import sys
import re
import time
import select
import termios
import datetime

import You_Exist_Imports as game

# ---------- Settings ----------
SHOW_LOCKED_DESCRIPTIONS = False    # False: locked achievements show "???" instead of how to get them
# The title uses whatever colour the being's text uses, so the two always match
TITLE_COLOUR = getattr(game, "EXACT_COLOURS", {}).get(("red", ("bold", "dark")), (126, 58, 56))
DIM_COLOUR = (102, 102, 102)        # locked achievements and hints
HIGHLIGHT_COLOUR = (220, 220, 220)  # the selected menu option
UNLOCKED_COLOUR = (220, 220, 220)


# ---------- Drawing helpers ----------
def colour(rgb, text, bold=False):
    # Bold is sent as its own code, separate from the colour, so the game's
    # older-Terminal colour fallback can recognise and convert the colour
    r, g, b = rgb
    bold_code = "\033[1m" if bold else ""
    return f"{bold_code}\033[38;2;{r};{g};{b}m{text}\033[0m"

def clear():
    # \033[r = use the whole window (resizing the window resets the game's half-screen area)
    sys.stdout.write("\033[r\033[2J\033[H")

def centred(text, visible_length=None):
    width = game.size.columns
    length = visible_length if visible_length is not None else len(text)
    return " " * max(0, (width - length) // 2) + text

def fit(text, width):
    # Cut text down to fit on one line, so nothing wraps and spoils the layout
    return text if len(text) <= width else text[: max(0, width - 3)] + "..."

def draw_title():
    print()
    print(centred(colour(TITLE_COLOUR, "Y O U   E X I S T", bold=True), 17))
    print()

def draw_menu(options, selected, hint="↑ ↓ to move, Enter to select"):
    for i, option in enumerate(options):
        if i == selected:
            line = colour(HIGHLIGHT_COLOUR, f"›  {option}", bold=True)
            print(centred(line, len(option) + 3))
        else:
            print(centred(colour(DIM_COLOUR, f"   {option}"), len(option) + 3))
    print()
    print(centred(colour(DIM_COLOUR, hint), len(hint)))
    sys.stdout.flush()


# ---------- Keyboard ----------
def read_key():
    """Wait for one key press and return it as a name: up, down, left, right,
    enter, back, a digit, or "resize" if the window changed size meanwhile."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    new_settings = termios.tcgetattr(fd)
    new_settings[3] &= ~(termios.ECHO | termios.ICANON)
    new_settings[6][termios.VMIN] = 1
    new_settings[6][termios.VTIME] = 0
    window = (game.size.lines, game.size.columns)
    termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    try:
        while not select.select([fd], [], [], 0.25)[0]:
            if (game.size.lines, game.size.columns) != window:
                return "resize"
        data = os.read(fd, 1)
        while select.select([fd], [], [], 0.02)[0]:
            data += os.read(fd, 64)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    for codes, name in ((("\x1b[A", "\x1bOA"), "up"), (("\x1b[B", "\x1bOB"), "down"),
                        (("\x1b[C", "\x1bOC"), "right"), (("\x1b[D", "\x1bOD"), "left")):
        if data.decode(errors="ignore").startswith(codes):
            return name
    key = data[:1]
    if key in (b"\r", b"\n", b" "):
        return "enter"
    if key in (b"\x1b", b"q", b"Q", b"\x7f"):
        return "back"
    if key.isdigit():
        return key.decode()
    return None

def choose(options, draw_screen, selected=0):
    """Let the player pick from a list of options. Returns the option's
    position in the list, or None if they pressed Esc / Q."""
    while True:
        draw_screen(selected)
        key = read_key()
        if key == "up":
            selected = (selected - 1) % len(options)
        elif key == "down":
            selected = (selected + 1) % len(options)
        elif key == "enter":
            return selected
        elif key == "back":
            return None
        elif key and key.isdigit() and 1 <= int(key) <= len(options):
            return int(key) - 1


# ---------- Achievements ----------
def all_achievements():
    """Read every achievement straight from You_Exist_Imports.py, so new ones
    show up here automatically. Returns (name, title, description, unlocked)."""
    try:
        with open(game.__file__, encoding="utf-8") as f:
            source = f.read()
    except OSError:
        return []
    start = source.find("class achievements")
    if start == -1:
        return []
    section = source[start:]
    found = []
    pattern = r'def (\w+)\(\):(.*?)(?=\n    def |\nclass |\n#####|\Z)'
    for name, body in re.findall(pattern, section, re.S):
        note = re.search(r'Notification\("((?:[^"\\]|\\.)*)"\)\.with_subtitle\("((?:[^"\\]|\\.)*)"\)', body)
        if note and hasattr(game, f"{name}_Gotten"):
            description, title = note.groups()
            found.append((name, title, description, bool(getattr(game, f"{name}_Gotten"))))
    return found

def achievements_screen():
    page = 0
    while True:
        achievements = all_achievements()
        unlocked = sum(1 for a in achievements if a[3])
        per_page = max(1, (game.size.lines - 9) // 2)   # each achievement takes two lines
        pages = max(1, -(-len(achievements) // per_page))
        page = min(page, pages - 1)
        width = game.size.columns - 6

        clear()
        draw_title()
        heading = f"Achievements: {unlocked} of {len(achievements)} unlocked"
        print(centred(colour(UNLOCKED_COLOUR, heading, bold=True), len(heading)))
        print()
        for name, title, description, got in achievements[page * per_page:(page + 1) * per_page]:
            if got:
                print("  " + colour(UNLOCKED_COLOUR, fit(f"✓ {title}", width), bold=True))
                print("    " + colour(DIM_COLOUR, fit(description, width)))
            else:
                hidden = description if SHOW_LOCKED_DESCRIPTIONS else "???"
                print("  " + colour(DIM_COLOUR, fit(f"· {title}", width)))
                print("    " + colour(DIM_COLOUR, fit(hidden, width)))
        print()
        hint = "Esc to go back" if pages == 1 else f"Page {page + 1} of {pages}   ← → to turn the page   Esc to go back"
        print(centred(colour(DIM_COLOUR, hint), len(hint)))
        sys.stdout.flush()

        key = read_key()
        if key in ("right", "down"):
            page = min(page + 1, pages - 1)
        elif key in ("left", "up"):
            page = max(page - 1, 0)
        elif key in ("back", "enter"):
            return


# ---------- Runs (ready for saving progress later) ----------
def all_runs():
    return game.save_data.setdefault("runs", []) if hasattr(game, "save_data") else []

def resumable_runs():
    # A run can be continued once it has a checkpoint and hasn't finished
    return [run for run in all_runs() if run.get("checkpoint") and not run.get("finished")]

def save_progress():
    if getattr(game, "SAVING_ON", False) and hasattr(game, "write_save"):
        game.write_save(game.save_data)

def start_new_run():
    runs = all_runs()
    now = datetime.datetime.now().isoformat(timespec="minutes")
    number = max((run["number"] for run in runs), default=0) + 1
    run = {"number": number, "started": now, "last_played": now, "finished": False, "checkpoint": None}
    runs.append(run)
    # Keep the save file tidy: forget old runs that can't be continued anyway
    keep = [r for r in runs if r.get("checkpoint") and not r.get("finished")]
    runs[:] = keep + [r for r in runs if r not in keep][-10:]
    game.current_run = run
    save_progress()
    return run

def describe_run(run):
    def nice(when):
        try:
            return datetime.datetime.fromisoformat(when).strftime("%-d %b, %-I:%M%p").replace("AM", "am").replace("PM", "pm")
        except (TypeError, ValueError):
            return "?"
    return f"Continue run {run['number']} (last played {nice(run.get('last_played'))})"

def choose_run():
    """Returns the run to play: a new one, or (once saving exists) one to continue.
    Returns None if the player backs out."""
    unfinished = resumable_runs()
    if not unfinished:
        return start_new_run()          # nothing to continue, so go straight into a new run
    options = [describe_run(run) for run in unfinished] + ["Start a new run", "Back"]
    def draw(selected):
        clear()
        draw_title()
        draw_menu(options, selected)
    picked = choose(options, draw)
    if picked is None or options[picked] == "Back":
        return None
    if options[picked] == "Start a new run":
        return start_new_run()
    run = unfinished[picked]
    run["last_played"] = datetime.datetime.now().isoformat(timespec="minutes")
    game.current_run = run
    save_progress()
    return run

def save_checkpoint(**progress):
    """FOR LATER: call this at a safe point in the story to save where the player is,
    e.g. save_checkpoint(chapter="Me_and_I", ponder=3, charisma=1).
    The game will then also need code to jump back to that chapter when a run is continued."""
    run = getattr(game, "current_run", None)
    if run is not None:
        run["checkpoint"] = progress
        run["last_played"] = datetime.datetime.now().isoformat(timespec="minutes")
        save_progress()

def finish_run():
    """FOR LATER: call this when a run reaches an ending, so it's no longer offered to continue."""
    run = getattr(game, "current_run", None)
    if run is not None:
        run["finished"] = True
        save_progress()


# ---------- The home screen itself ----------
def home_screen():
    sys.stdout.write("\033[r\033[?25l")   # use the whole window, and hide the cursor
    try:
        options = ["Play", "Achievements", "Quit"]
        picked = 0
        while True:
            def draw(selected):
                clear()
                print("\n" * max(0, game.size.lines // 4 - 3), end="")
                draw_title()
                draw_menu(options, selected)
            picked = choose(options, draw, picked)
            if picked is None or options[picked] == "Quit":
                clear()
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
                sys.exit()
            if options[picked] == "Achievements":
                achievements_screen()
            elif options[picked] == "Play":
                if choose_run() is not None:
                    return
    finally:
        # Put the screen back exactly how the story expects it
        sys.stdout.write("\033[?25h")
        clear()
        game.set_scroll_region()
        sys.stdout.write("\033[H")
        sys.stdout.flush()
