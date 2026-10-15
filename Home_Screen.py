# ============================================================
#  You Exist: home screen
#  Shows a menu before the game starts: Play, Achievements, Quit.
#  Use the arrow keys (or the number keys) and Enter. Esc or Q goes back.
#
#  Runs: each playthrough is a "run". Progress is saved at the start of every life,
#  so a run can be continued later from the start of the life the player was on.
#  Pressing Esc while the story is waiting for a key (or typing "menu" at a choice)
#  returns to the home screen.
# ============================================================

import os
import sys
import re
import time
import select
import termios
import datetime
import json
import builtins

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


def choose_paged(items, fixed, heading=None):
    """A menu that splits a long list of items over several pages if the window
    is too short. The fixed options (like Back) appear on every page.
    Returns ("item", position in items), ("fixed", position in fixed), or None for Esc."""
    page = 0
    selected = 0
    while True:
        overhead = 3 + (2 if heading else 0) + 1 + len(fixed) + 3   # title, heading, gap, fixed options, hints
        per_page = max(1, game.size.lines - overhead)
        pages = max(1, -(-len(items) // per_page))
        page = min(page, pages - 1)
        shown = items[page * per_page:(page + 1) * per_page]
        options = shown + fixed
        selected = min(selected, len(options) - 1)

        clear()
        draw_title()
        if heading:
            print(centred(colour(UNLOCKED_COLOUR, fit(heading, game.size.columns - 2)), min(len(heading), game.size.columns - 2)))
            print()
        width = game.size.columns - 4
        for i, option in enumerate(options):
            if i == len(shown) and shown:
                print()                                  # gap between the list and the fixed options
            text = fit(option, width)
            if i == selected:
                print(centred(colour(HIGHLIGHT_COLOUR, f"›  {text}", bold=True), len(text) + 3))
            else:
                print(centred(colour(DIM_COLOUR, f"   {text}"), len(text) + 3))
        print()
        hint = "↑ ↓ to move, Enter to select"
        if pages > 1:
            hint = f"Page {page + 1} of {pages}   ← → to turn the page   " + hint
        print(centred(colour(DIM_COLOUR, fit(hint, game.size.columns - 2)), min(len(hint), game.size.columns - 2)))
        sys.stdout.flush()

        key = read_key()
        if key == "up":
            selected = (selected - 1) % len(options)
        elif key == "down":
            selected = (selected + 1) % len(options)
        elif key == "right" and page < pages - 1:
            page += 1
        elif key == "left" and page > 0:
            page -= 1
        elif key == "back":
            return None
        elif key == "enter" or (key and key.isdigit() and 1 <= int(key) <= len(options)):
            if key != "enter":
                selected = int(key) - 1
            if selected < len(shown):
                return ("item", page * per_page + selected)
            return ("fixed", selected - len(shown))


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
        # Unlocked achievements first, in the order they were earned (earliest at the top),
        # then locked ones in their usual order. The save file lists achievements in the
        # order they were unlocked. (To show the most recent first, add reverse() below.)
        earned_order = list(getattr(game, "save_data", {}).get("achievements", []))
        def sort_key(achievement):
            name, title, description, got = achievement
            if not got:
                return (1, 0)
            return (0, earned_order.index(name) if name in earned_order else len(earned_order))
        achievements = sorted(all_achievements(), key=sort_key)
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


# ---------- Path tracking (GoatCounter) ----------
# Sends a small signal to your GoatCounter dashboard when players start lives,
# unlock achievements, die (see die() in You_Exist_Imports.py) and reach the ending.
# Uses the LAUNCH_COUNTER address from You_Exist_Imports.py. Like the launch
# counter, it does nothing in VS Code and silently gives up without internet.
import threading
import urllib.parse
import urllib.request

def track(path, title=None, wait_for_it=False):
    counter = getattr(game, "LAUNCH_COUNTER", "")
    if not counter or "YOURCODE" in counter or os.environ.get("TERM_PROGRAM") == "vscode":
        return

    def send():
        try:
            import ssl
            try:
                import certifi
                context = ssl.create_default_context(cafile=certifi.where())
            except ImportError:
                context = ssl.create_default_context()
            params = urllib.parse.urlencode({"p": path, "t": title or path, "rnd": time.time()})
            request = urllib.request.Request(
                f"{counter}?{params}",
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) You-Exist-game"},
            )
            urllib.request.urlopen(request, timeout=3, context=context)
        except Exception:
            pass

    thread = threading.Thread(target=send, daemon=True)
    thread.start()
    if wait_for_it:
        thread.join(timeout=3)   # for signals sent just before the game restarts
    return thread

def track_achievements():
    """Records each achievement the moment a player unlocks it."""
    achievements = getattr(game, "achievements", None)
    if achievements is None:
        return
    for name, check in list(vars(achievements).items()):
        flag = f"{name}_Gotten"
        if name.startswith("_") or not hasattr(game, flag):
            continue
        func = check.__func__ if isinstance(check, staticmethod) else check
        if not callable(func) or getattr(func, "_tracked", False):
            continue
        def make_wrapper(name=name, flag=flag, func=func):
            def wrapper(*args, **kwargs):
                was_gotten = getattr(game, flag)
                result = func(*args, **kwargs)
                if not was_gotten and getattr(game, flag):
                    track(f"/achievement/{name}", f"Achievement: {name.replace('_', ' ')}")
                return result
            wrapper._tracked = True
            return wrapper
        setattr(achievements, name, staticmethod(make_wrapper()))


# ---------- Runs ----------
# Variables that belong to the current run, and are saved at the start of every life
RUN_VARIABLES = ["lives_lived", "all_there_is", "first_person", "physical_form"]
POINTS = ["ponder", "charisma", "physicality", "confidence", "morality", "insanity"]
MAX_UNFINISHED_RUNS = 10    # save slots: when they're all full, the player picks one to replace

# In VS Code, achievements aren't saved, but runs are kept in a separate testing file
# so you can still test continuing a run. Delete that file to clear your test runs.
TESTING_RUNS_FILE = os.path.expanduser("~/Library/Application Support/You Exist/runs (testing).json")
_testing_data = None

def _run_store():
    global _testing_data
    if getattr(game, "SAVING_ON", False) and hasattr(game, "save_data"):
        return game.save_data
    if _testing_data is None:
        try:
            with open(TESTING_RUNS_FILE) as f:
                _testing_data = json.load(f)
        except (OSError, ValueError):
            _testing_data = {}
    return _testing_data

def all_runs():
    return _run_store().setdefault("runs", [])

def resumable_runs():
    # A run can be continued once it has a checkpoint and hasn't finished (newest first)
    runs = [run for run in all_runs() if run.get("checkpoint") and not run.get("finished")]
    return sorted(runs, key=lambda run: run.get("last_played", ""), reverse=True)

def save_progress():
    if getattr(game, "SAVING_ON", False) and hasattr(game, "write_save"):
        game.write_save(game.save_data)
        return
    try:
        os.makedirs(os.path.dirname(TESTING_RUNS_FILE), exist_ok=True)
        with open(TESTING_RUNS_FILE, "w") as f:
            json.dump(_run_store(), f, indent=2)
    except OSError:
        pass

def now():
    return datetime.datetime.now().isoformat(timespec="minutes")

def start_new_run():
    """Start a new run. If every save slot is full, the player chooses which run
    to replace. Returns the new run, or None if they cancel."""
    unfinished = resumable_runs()
    if len(unfinished) >= MAX_UNFINISHED_RUNS:
        replaced = pick_run(f"All {MAX_UNFINISHED_RUNS} save slots are full. Which run should the new one replace?",
                            unfinished, "Cancel")
        if replaced is None:
            return None
    else:
        replaced = None
    runs = all_runs()
    number = max((run["number"] for run in runs), default=0) + 1
    run = {"number": number, "started": now(), "last_played": now(), "finished": False, "checkpoint": None}
    if replaced is not None:
        # The old run is only removed once the new one is actually saved (after its first
        # life), so abandoning the new run early doesn't lose the old one for nothing
        run["replaces"] = replaced["number"]
    # Keep only runs that can still be continued (finished and never-saved runs are dropped)
    runs[:] = [r for r in runs if r in unfinished] + [run]
    game.current_run = run
    save_progress()
    return run

def nice_time(when):
    try:
        return datetime.datetime.fromisoformat(when).strftime("%-d %b, %-I:%M%p").replace("AM", "am").replace("PM", "pm")
    except (TypeError, ValueError):
        return "?"

def describe_run(run, start="Continue run"):
    life = (run.get("checkpoint") or {}).get("lives_lived", 0) + 1
    return f"{start} {run['number']}: life {life} (last played {nice_time(run.get('last_played'))})"

def menu_with_heading(heading, options):
    """A menu with a line of explanation above it. Returns the chosen position, or None."""
    def draw(selected):
        clear()
        draw_title()
        if heading:
            print(centred(colour(UNLOCKED_COLOUR, fit(heading, game.size.columns - 2)), min(len(heading), game.size.columns - 2)))
            print()
        draw_menu(options, selected)
    return choose(options, draw)

def pick_run(heading, runs, last_option):
    """Let the player pick one of the given runs. Returns it, or None for the last option / Esc."""
    picked = choose_paged([describe_run(run, "Run") for run in runs], [last_option], heading)
    if picked is None or picked[0] == "fixed":
        return None
    return runs[picked[1]]

def delete_a_run():
    while True:
        unfinished = resumable_runs()
        if not unfinished:
            return
        run = pick_run("Which run would you like to delete?", unfinished, "Back")
        if run is None:
            return
        sure = menu_with_heading(f"Delete run {run['number']}? This can't be undone.",
                                 ["No, keep it", "Yes, delete it"])
        if sure == 1:
            all_runs().remove(run)
            save_progress()

def choose_run():
    """Returns the run to play: a new one, or one to continue.
    Returns None if the player backs out."""
    first_visit = True
    while True:
        unfinished = resumable_runs()
        if not unfinished and first_visit:
            return start_new_run()      # nothing saved when Play was pressed, so go straight into a new run
        first_visit = False             # once the save slots have been shown, stay on them (even if they're all empty)
        empty_slots = max(0, MAX_UNFINISHED_RUNS - len(unfinished))
        items = [describe_run(run) for run in unfinished] + ["Empty save slot"] * empty_slots
        fixed = ["Start a new run", "Delete a run", "Back"]
        picked = choose_paged(items, fixed)
        if picked is None or picked == ("fixed", 2):
            return None
        if picked == ("fixed", 1):
            delete_a_run()
            continue
        if picked == ("fixed", 0) or picked[1] >= len(unfinished):
            # "Start a new run", or an empty save slot
            run = start_new_run()
            if run is not None:
                return run
            continue                    # they cancelled replacing a run
        run = unfinished[picked[1]]
        run["last_played"] = now()
        game.current_run = run
        save_progress()
        return run

def apply_run(run, namespace):
    """Set up the game's variables for this run: saved values when continuing,
    starting values for a new run."""
    saved = run.get("checkpoint") or {}
    for name in RUN_VARIABLES + POINTS:
        if name in saved:
            value = saved[name]
        else:
            value = getattr(game, name, 0)   # the starting value from You_Exist_Imports
        setattr(game, name, value)
        if namespace is not None:
            namespace[name] = value

# ---------- Statistics ----------
# Lifetime totals across every run. Points are counted as the CHANGE over each
# finished life (so reaching life 4 with 10 Ponder doesn't add 10 again).

def stats():
    store = _run_store()
    st = store.setdefault("stats", {})
    points = st.setdefault("points", {})
    for name in POINTS:
        points.setdefault(name, 0)
    for key in ("lives_completed", "deaths", "runs_completed"):
        st.setdefault(key, 0)
    st.setdefault("deaths_found", [])
    return st

def points_now():
    return {name: getattr(game, name, 0) for name in POINTS}

def count_finished_life(run):
    """Add the points gained or lost during the life that just ended to the lifetime totals."""
    started = run.get("life_start")
    if not started:
        return
    st = stats()
    current = points_now()
    for name in POINTS:
        st["points"][name] += current[name] - started["points"].get(name, 0)
    st["lives_completed"] += 1
    run["life_start"] = None   # so the same life can never be counted twice

def record_death(name):
    st = stats()
    st["deaths"] += 1
    if name not in st["deaths_found"]:
        st["deaths_found"].append(name)
    save_route(name)
    save_progress()

# ---------- Routes (for the discovery tree) ----------
# During each life, every choice the player makes is remembered. When the life
# ends (in a death, or the ending), that route is saved with how it ended.
# A typed answer only counts as a choice if it matches one of the options shown
# in brackets, like (fret) or (accept), or is yes/no to a question with no
# bracketed options, so rejected answers aren't recorded.
current_route = []
_recent_text = []

def _clean(text):
    for symbol in "'().,":
        text = text.replace(symbol, "")
    return text.lower().strip()

def _remember_printed(text):
    _recent_text.append(text)
    if len(_recent_text) > 400:
        del _recent_text[:200]

def note_answer(answer):
    """Called with everything the player types. Records it if it's one of the offered options."""
    shown = "".join(_recent_text)
    _recent_text.clear()
    options = {_clean(o) for o in re.findall(r"\(([^()\n]{1,40})\)", shown) if re.search(r"[A-Za-z]", o)}
    choice = _clean(answer)
    if choice and choice in options:
        pass
    elif not options and choice in ("yes", "no"):
        options = {"yes", "no"}          # yes/no questions don't show their options in brackets
    else:
        return                           # not one of the offered options: the game will ask again
    # Remember the question asked at this point, for the discovery tree
    plain = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]|\x1b[78]", "", shown)
    lines = [line.strip() for line in plain.splitlines() if line.strip()]
    questions = stats().setdefault("questions", {})
    questions[">".join(current_route)] = {"question": lines[-1] if lines else "", "options": sorted(options)}
    current_route.append(choice)

def save_route(ending):
    if not current_route and ending is None:
        return
    routes = stats().setdefault("routes", [])
    for route in routes:
        if route["choices"] == current_route and route["end"] == ending:
            route["times"] += 1
            break
    else:
        routes.append({"choices": list(current_route), "end": ending, "times": 1})
    current_route.clear()

def install_route_recording():
    out = sys.stdout
    if getattr(out, "_route_tap", False):
        return
    original_write = out.write
    def write(text):
        _remember_printed(text)
        return original_write(text)
    try:
        out.write = write
        out._route_tap = True
    except AttributeError:
        pass   # can't tap this output (very unlikely): routes just won't be recorded


def all_deaths():
    """Every death in the game, found by reading the die("...") lines in the story files."""
    folder = os.path.dirname(os.path.abspath(game.__file__))
    names = set()
    for file in os.listdir(folder):
        if file.endswith(".py") and file not in ("Home_Screen.py", "You_Exist_Imports.py", "launcher.py"):
            try:
                with open(os.path.join(folder, file), encoding="utf-8") as f:
                    names.update(re.findall(r'\bdie\("([^"]+)"', f.read()))
            except OSError:
                pass
    return names

def statistics_screen():
    st = stats()
    known = all_deaths()
    found = len([d for d in st["deaths_found"] if d in known]) if known else len(st["deaths_found"])
    rows = [("Lives lived", str(st["lives_completed"])),
            ("Deaths", str(st["deaths"])),
            ("Deaths discovered", f"{found} of {len(known)}" if known else str(found)),
            ("Runs completed", str(st["runs_completed"]))]
    point_rows = [(name.capitalize(), f"{st['points'][name]:+d}" if st["points"][name] else "0") for name in POINTS]
    width = max(len(label) for label, _ in rows + point_rows) + 10
    options = ["Discoveries", "Back"]
    selected = 0
    while True:
        clear()
        draw_title()
        heading = "Statistics across all your runs"
        print(centred(colour(UNLOCKED_COLOUR, heading, bold=True), len(heading)))
        print()
        for label, value in rows:
            line = label + value.rjust(width - len(label))
            print(centred(colour(UNLOCKED_COLOUR, line), len(line)))
        print()
        sub = "Points gained or lost over all your lives"
        print(centred(colour(DIM_COLOUR, sub), len(sub)))
        for label, value in point_rows:
            line = label + value.rjust(width - len(label))
            print(centred(colour(UNLOCKED_COLOUR, line), len(line)))
        print()
        for index, option in enumerate(options):
            text = ("›  " if index == selected else "   ") + option
            print(centred(colour(HIGHLIGHT_COLOUR, text, bold=True) if index == selected else colour(DIM_COLOUR, text), len(text)))
        print()
        hint = "↑ ↓ to move, Enter to select"
        print(centred(colour(DIM_COLOUR, hint), len(hint)))
        sys.stdout.flush()
        key = read_key()
        if key in ("up", "down"):
            selected = 1 - selected
        elif key == "back" or (key == "enter" and options[selected] == "Back"):
            return
        elif key == "enter" and options[selected] == "Discoveries":
            discoveries_screen()


def start_of_life(namespace):
    """Call at the start of each life: saves the run so it can be continued from here.
    A brand new run isn't saved until its first life is over, since continuing it
    would just be the same as starting fresh."""
    run = getattr(game, "current_run", None)
    if run is None:
        return
    life = namespace.get("lives_lived", 0) + 1
    track(f"/life/{life}", f"Started life {life}")
    lives = namespace.get("lives_lived", 0)
    started = run.get("life_start")
    if started and lives > started.get("life", lives):
        count_finished_life(run)          # the previous life is over: add its point changes
    run["life_start"] = {"life": lives, "points": points_now()}
    current_route.clear()
    if run.get("checkpoint") is None and namespace.get("lives_lived", 0) == 0:
        return   # first life of a new run: nothing worth saving yet
    if "replaces" in run:
        # Now that this run is being saved, it takes over the slot the player chose
        runs = all_runs()
        runs[:] = [r for r in runs if r.get("number") != run["replaces"] or r is run]
        del run["replaces"]
    checkpoint = {name: namespace.get(name, getattr(game, name, 0)) for name in RUN_VARIABLES}
    checkpoint.update({name: getattr(game, name, 0) for name in POINTS})
    run["checkpoint"] = checkpoint
    run["last_played"] = now()
    save_progress()

def finish_run():
    """Call when a run reaches its ending, so it's no longer offered to continue."""
    run = getattr(game, "current_run", None)
    track("/run/finished", "Reached the ending", wait_for_it=True)
    if run is not None:
        count_finished_life(run)
        stats()["runs_completed"] += 1
        save_route("THE ENDING")
        run["finished"] = True
        run["last_played"] = now()
        save_progress()


# ---------- Getting back to the home screen ----------
def back_to_home_screen(track_leaving=True):
    """Restart the game, which brings up the home screen. The run was saved
    at the start of this life, so it can be continued from there."""
    if track_leaving:
        track("/run/left-for-home-screen", "Left a run for the home screen", wait_for_it=True)
    os.environ["YOU_EXIST_RESTARTED"] = "1"   # so the restart isn't counted as a new launch
    sys.stdout.write("\033[r\033[?25h")
    sys.stdout.flush()
    if getattr(sys, "frozen", False):
        os.execv(sys.executable, [sys.executable])                  # the built app
    else:
        os.execv(sys.executable, [sys.executable] + sys.argv)       # running in VS Code

def obliterate():
    """For deaths that end a run for good: the run can no longer be continued,
    and the game goes straight back to the home screen."""
    run = getattr(game, "current_run", None)
    if run is not None:
        count_finished_life(run)
        run["finished"] = True
        run["last_played"] = now()
        save_progress()
    time.sleep(1)   # a brief, empty pause before the home screen appears
    back_to_home_screen(track_leaving=False)

def ask_to_leave():
    """Shows a one-line question. Returns True if the player wants to go home.
    During a new run's first life there's nothing to lose, so it doesn't ask."""
    run = getattr(game, "current_run", None)
    if run is None or run.get("checkpoint") is None:
        return True
    question = "Return to the home screen? You'll continue from the start of this life.  (Enter/Space: Yes. Any other key: No)"
    question = fit(question, game.size.columns - 1)
    sys.stdout.write("\r\033[2K")
    sys.stdout.write(colour(DIM_COLOUR, question))
    sys.stdout.flush()
    answer = read_key()
    sys.stdout.write("\r\033[2K")        # rub the question out again
    sys.stdout.flush()
    if hasattr(sys.stdout, "col"):
        sys.stdout.col = 0
    return answer == "enter"

def wait():
    """Waits for a key press, like before, but Esc offers to go back to the home screen."""
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    while True:
        old_settings = termios.tcgetattr(fd)
        new_settings = termios.tcgetattr(fd)
        new_settings[3] &= ~(termios.ECHO | termios.ICANON)
        new_settings[6][termios.VMIN] = 1
        new_settings[6][termios.VTIME] = 0
        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
        try:
            data = os.read(fd, 1)
            while select.select([fd], [], [], 0.02)[0]:
                data += os.read(fd, 64)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if data != b"\x1b":            # anything but a lone Esc: carry on with the story
            return
        if ask_to_leave():
            back_to_home_screen()
        # they said no: keep waiting for a key to continue the story

_original_input = builtins.input
def input_with_menu(prompt=""):
    """Typing "menu" at any choice also offers to go back to the home screen."""
    while True:
        answer = _original_input(prompt)
        if answer.strip().lower() != "menu":
            note_answer(answer)
            return answer
        if ask_to_leave():
            back_to_home_screen()


# ---------- Discoveries ----------
# An overview of every chapter, with a dot for each of its deaths (filled in once
# found), leading into an explorer that walks through the routes the player has
# taken, one decision at a time.
FOUND_COLOUR = TITLE_COLOUR    # discovered deaths use the being's red

def chapters_in_order():
    """Chapter names in the order they appear in the story, each with its deaths in order."""
    folder = os.path.dirname(os.path.abspath(game.__file__))
    order = ["You_Exist"]
    try:
        with open(os.path.join(folder, "You_Exist.py"), encoding="utf-8") as f:
            for name in re.findall(r'resource_path\("([^"]+)\.py"\)', f.read()):
                if name not in order:
                    order.append(name)
    except OSError:
        pass
    deaths = {}
    for chapter in order + sorted(f[:-3] for f in os.listdir(folder) if f.endswith(".py")):
        if chapter in deaths or chapter in ("Home_Screen", "You_Exist_Imports", "launcher"):
            continue
        try:
            with open(os.path.join(folder, chapter + ".py"), encoding="utf-8") as f:
                found = re.findall(r'\bdie\("([^"]+)"', f.read())
        except OSError:
            continue
        if found:
            deaths[chapter] = list(dict.fromkeys(found))   # keep order, drop repeats
    return deaths

def pretty(name):
    return name.replace("_", " ")

def death_label(death):
    # "The_Land_Left/protect/escape" -> "protect / escape"
    return " / ".join(death.split("/")[1:]) or death

def discoveries_screen():
    selected = 0
    while True:
        deaths = chapters_in_order()
        found = set(stats()["deaths_found"])
        chapters = list(deaths)
        name_width = max([len(pretty(c)) for c in chapters] + [10])
        items = []
        for chapter in chapters:
            got = sum(1 for d in deaths[chapter] if d in found)
            dots = " ".join(colour(FOUND_COLOUR, "●") if d in found else colour(DIM_COLOUR, "○") for d in deaths[chapter])
            dots_width = len(deaths[chapter]) * 2 - 1
            count = f"{got} of {len(deaths[chapter])}"
            items.append((chapter, pretty(chapter), dots, dots_width, count))
        options = [i[1] for i in items] + ["Explore every route", "Back"]
        total_found = sum(1 for c in chapters for d in deaths[c] if d in found)
        total = sum(len(deaths[c]) for c in chapters)

        clear()
        draw_title()
        heading = f"Discoveries: {total_found} of {total} deaths found"
        print(centred(colour(UNLOCKED_COLOUR, heading, bold=True), len(heading)))
        print()
        widest = max(i[3] for i in items) if items else 0
        count_width = max([len(i[4]) for i in items] + [0])
        show_dots = name_width + widest + 16 <= game.size.columns
        for index, (chapter, name, dots, dots_width, count) in enumerate(items):
            marker = "›  " if index == selected else "   "
            style = (lambda t: colour(HIGHLIGHT_COLOUR, t, bold=True)) if index == selected else (lambda t: colour(UNLOCKED_COLOUR, t))
            line = style(marker + name.ljust(name_width)) + "   "
            length = 3 + name_width + 3
            if show_dots:
                line += dots + " " * (widest - dots_width) + "   "
                length += widest + 3
            line += colour(DIM_COLOUR, count.rjust(count_width))
            length += count_width
            print(centred(line, length))
        print()
        for offset, extra in enumerate(options[len(items):]):
            index = len(items) + offset
            text = f"›  {extra}" if index == selected else f"   {extra}"
            print(centred(colour(HIGHLIGHT_COLOUR, text, bold=True) if index == selected else colour(DIM_COLOUR, text), len(text)))
        print()
        hint = "↑ ↓ to move, Enter to explore a chapter's routes"
        print(centred(colour(DIM_COLOUR, fit(hint, game.size.columns - 2)), min(len(hint), game.size.columns - 2)))
        sys.stdout.flush()

        key = read_key()
        if key == "up":
            selected = (selected - 1) % len(options)
        elif key == "down":
            selected = (selected + 1) % len(options)
        elif key == "back" or (key == "enter" and options[selected] == "Back"):
            return
        elif key == "enter":
            chapter = None if selected >= len(items) else items[selected][0]
            explore_routes(chapter)

def build_tree(chapter=None):
    """Turn the saved routes into a tree. Each node is a dict:
    {"children": {choice: node}, "ends": {death: times}}. If a chapter is given,
    only routes that ended in that chapter are included."""
    root = {"children": {}, "ends": {}}
    for route in stats().get("routes", []):
        end = route.get("end") or ""
        if chapter and not end.startswith(chapter + "/"):
            continue
        node = root
        for choice in route["choices"]:
            node = node["children"].setdefault(choice, {"children": {}, "ends": {}})
        node["ends"][end] = node["ends"].get(end, 0) + route.get("times", 1)
    return root

def deaths_below(node):
    found = set(d for d in node["ends"] if d != "THE ENDING")
    for child in node["children"].values():
        found |= deaths_below(child)
    return found

def explore_routes(chapter=None):
    tree = build_tree(chapter)
    path = []               # the choices taken to reach the current point
    selected = 0
    questions = stats().get("questions", {})
    while True:
        node = tree
        for choice in path:
            node = node["children"][choice]
        info = questions.get(">".join(path), {})
        # Discovered choices from here, then untried options shown as ???
        rows = []
        for choice, child in node["children"].items():
            below = deaths_below(child)
            if child["children"]:
                note = f"{len(below)} death{'s' if len(below) != 1 else ''} found beyond here" if below else "explored"
                rows.append((choice, note, True))
            else:
                ends = [death_label(d) if d != "THE ENDING" else "the ending" for d in child["ends"]]
                rows.append((choice, "✝ " + ", ".join(ends) if ends else "", False))
        if not chapter:
            for option in info.get("options", []):
                if option not in node["children"]:
                    rows.append(("???", "not yet explored", False))
        options = [r[0] for r in rows] + ["Back"]
        selected = min(selected, len(options) - 1)

        clear()
        draw_title()
        crumbs = " › ".join(["you exist"] + path)
        if chapter:
            crumbs = pretty(chapter) + ":  " + crumbs
        if len(crumbs) > game.size.columns - 4:
            crumbs = "… " + crumbs[-(game.size.columns - 6):]
        print(centred(colour(DIM_COLOUR, crumbs), len(crumbs)))
        print()
        question = info.get("question", "")
        if question:
            q = fit(question, game.size.columns - 4)
            print(centred(colour(UNLOCKED_COLOUR, q), len(q)))
            print()
        if not rows:
            message = "No routes discovered yet." if not path else "Nothing more found down this path yet."
            print(centred(colour(DIM_COLOUR, message), len(message)))
            print()
        width = max([len(r[0]) for r in rows] + [4]) + 4
        note_room = max(10, game.size.columns - width - 9)
        block = 3 + width + max([len(fit(r[1], note_room)) for r in rows] + [0])
        margin = " " * max(0, (game.size.columns - block) // 2)    # line the rows up with each other
        for index, (label, note, can_enter) in enumerate(rows):
            chosen = index == selected
            text = ("›  " if chosen else "   ") + label.ljust(width)
            body = colour(HIGHLIGHT_COLOUR, text, bold=True) if chosen else colour(UNLOCKED_COLOUR if label != "???" else DIM_COLOUR, text)
            note_colour = FOUND_COLOUR if note.startswith("✝") else DIM_COLOUR
            print(margin + body + colour(note_colour, fit(note, note_room)))
        print()
        back = "›  Back" if selected == len(rows) else "   Back"
        print(centred(colour(HIGHLIGHT_COLOUR, back, bold=True) if selected == len(rows) else colour(DIM_COLOUR, back), len(back)))
        print()
        hint = "Enter to follow a choice, Esc to step back"
        print(centred(colour(DIM_COLOUR, fit(hint, game.size.columns - 2)), min(len(hint), game.size.columns - 2)))
        sys.stdout.flush()

        key = read_key()
        if key == "up":
            selected = (selected - 1) % len(options)
        elif key == "down":
            selected = (selected + 1) % len(options)
        elif key in ("back", "left") or (key == "enter" and selected == len(rows)):
            if not path:
                return
            last = path.pop()
            selected = list(node_at(tree, path)["children"]).index(last)
        elif key in ("enter", "right") and selected < len(rows) and rows[selected][2]:
            path.append(rows[selected][0])
            selected = 0

def node_at(tree, path):
    node = tree
    for choice in path:
        node = node["children"][choice]
    return node


# ---------- Version (shown at the bottom of the home screen) ----------
# Shows the date of the latest update, worked out automatically from GitHub:
# the launcher remembers which version it downloaded, and the date of that
# version is looked up once (then saved, so it's instant from then on).
GITHUB_USER = "tgowen909"
GITHUB_REPO = "You-Exist"
APP_FOLDER = os.path.expanduser("~/Library/Application Support/You Exist")
_version_text = None

def version_text():
    global _version_text
    if _version_text is not None:
        return _version_text
    _version_text = ""
    game_folder = os.path.join(APP_FOLDER, "game")
    if not os.path.abspath(game.__file__).startswith(game_folder + os.sep):
        _version_text = "Testing version (not the downloaded game)"   # e.g. running in VS Code
        return _version_text
    try:
        with open(os.path.join(APP_FOLDER, "version.txt")) as f:
            sha = f.read().strip()
    except OSError:
        return _version_text          # no download yet (first launch without internet)
    cache_file = os.path.join(APP_FOLDER, "version_date.json")
    try:
        with open(cache_file) as f:
            cached = json.load(f)
        if cached.get("sha") == sha:
            _version_text = f"Updated {cached['date']}"
            return _version_text
    except (OSError, ValueError, KeyError):
        pass
    try:
        import ssl
        try:
            import certifi
            context = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            context = ssl.create_default_context()
        request = urllib.request.Request(f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/commits/{sha}",
                                         headers={"User-Agent": "You-Exist-launcher"})
        with urllib.request.urlopen(request, timeout=3, context=context) as response:
            when = json.loads(response.read())["commit"]["committer"]["date"]
        local = datetime.datetime.fromisoformat(when.replace("Z", "+00:00")).astimezone()
        date = local.strftime("%-d %b %Y")
        with open(cache_file, "w") as f:
            json.dump({"sha": sha, "date": date}, f)
        _version_text = f"Updated {date}"
    except Exception:
        pass                          # no internet: just don't show it this time
    return _version_text


# ---------- The home screen itself ----------
def home_screen(namespace=None):
    """Show the home screen. Pass globals() from You_Exist.py so the chosen run's
    progress can be loaded into the game."""
    # Keep the run's variables out of "import *", so the chapter files (which start
    # with "from You_Exist_Imports import *") can't reset them partway through a run
    game.__all__ = [name for name in vars(game) if not name.startswith("_") and name not in RUN_VARIABLES]
    # Swap in the versions of wait() and input() that know about the home screen
    game.wait = wait
    builtins.input = input_with_menu
    install_route_recording()
    original_die = getattr(game, "die", None)
    if original_die is not None and not getattr(original_die, "_counted", False):
        def die(name, scroll=True):
            record_death(name)
            return original_die(name, scroll=scroll)
        die._counted = True
        game.die = die
    if namespace is not None:
        namespace["wait"] = wait
        if original_die is not None:
            namespace["die"] = game.die
    track_achievements()

    sys.stdout.write("\033[r\033[?25l")   # use the whole window, and hide the cursor
    try:
        options = ["Play", "Achievements", "Stats", "Quit"]
        picked = 0
        while True:
            def draw(selected):
                clear()
                print("\n" * max(0, game.size.lines // 4 - 3), end="")
                draw_title()
                draw_menu(options, selected)
                version = version_text()
                if version:
                    # bottom line of the window, small and grey
                    sys.stdout.write(f"\033[{game.size.lines};1H")
                    sys.stdout.write(centred(colour(DIM_COLOUR, fit(version, game.size.columns - 2)), min(len(version), game.size.columns - 2)))
                    sys.stdout.flush()
            picked = choose(options, draw, picked)
            if picked is None or options[picked] == "Quit":
                clear()
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
                sys.exit()
            if options[picked] == "Achievements":
                achievements_screen()
            elif options[picked] == "Stats":
                statistics_screen()
            elif options[picked] == "Play":
                run = choose_run()
                if run is not None:
                    if run.get("checkpoint"):
                        track("/run/continued", "Continued a run")
                    else:
                        track("/run/new", "Started a new run")
                    apply_run(run, namespace)
                    return
    finally:
        # Put the screen back exactly how the story expects it
        sys.stdout.write("\033[?25h")
        clear()
        game.set_scroll_region()
        sys.stdout.write("\033[H")
        sys.stdout.flush()
