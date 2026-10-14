from __future__ import print_function
import os
from termcolor import cprint as termcolor_cprint
import subprocess
import sys
import time
# UNUSED, removed for faster loading: from plyer import notification
from aquaui.notification.native_notification import Notification
import random
# UNUSED, removed for faster loading: import pyautogui ##### Use pyautogui.scroll(n) to scroll n lines up (negatives allowed for down)
import pynput
import signal # is actually used
# UNUSED, removed for faster loading: import keyboard
import readline
# UNUSED, removed for faster loading: from AppKit import NSSound
import math
import textwrap
#from pydub import AudioSegment     <-- THIS DOES NOT WORK (inner module discontinued in python 3.13)
            ### WILL NEED TO FIGURE OUT ANOTHER WAY TO PLAY AUDIO
#from pydub.playback import play    <-- (same as above)


##### Exact colours #####
# Terminals all show termcolor's named colours ("red", "grey" and so on) differently,
# so this table swaps each combination the game uses for an exact RGB colour that
# looks the same in any terminal. The numbers are what VS Code shows on screen:
# get them by running colour_test.py in VS Code and colour-picking a screenshot.
# Format:  (colour name, (attributes in alphabetical order)): (R, G, B)

EXACT_COLOURS = {
    ("red", ("bold", "dark")): (126, 58, 56),     # 1. the being     
    ("light_grey", ("dark",)): (130, 130, 130),   # 2. voices        
    ("dark_grey", ()):         (102, 102, 102),   # 3. point stats   
    ("grey", ("dark",)):       (80, 80, 80),      # 4. timed voices  
}

# Hand-picked stand-ins for terminals that can't show exact colours (older Mac Terminal).
# Any colour not listed here is matched automatically, but dark, muted colours have
# no close match in the 256-colour palette, so the automatic pick can be way off.
# Format:  (R, G, B): 256-colour code   (chart: https://www.ditig.com/256-colors-cheat-sheet)
FALLBACK_COLOURS = {
    (126, 58, 56): 52,    # the being: very dark red (lighter options: 88, then 95)
}

def cprint(text, color=None, on_color=None, attrs=None, **kwargs):
    attrs = tuple(sorted(attrs or []))
    rgb = EXACT_COLOURS.get((color, attrs))
    if rgb is None:
        # Not in the table (e.g. bold with no colour): use termcolor as normal
        termcolor_cprint(text, color, on_color, attrs=list(attrs) or None, **kwargs)
        return
    r, g, b = rgb
    bold = "\033[1m" if "bold" in attrs else ""
    # "dark" is left out on purpose: the RGB value already includes the fading
    print(f"{bold}\033[38;2;{r};{g};{b}m{text}\033[0m", **kwargs)
# UNUSED, removed for faster loading: from threading import Thread
# UNUSED, removed for faster loading: import pygame


# print(sys.version)  # removed so it doesn't show up when the game launches
# $ auto-py-to-exe for creating an executable
# maybe use tkinter not pygame for creating a window?

keyboard_listener = pynput.keyboard.Listener(suppress=True)
keyboard_silencer = pynput.keyboard.Listener(suppress=True)
keyboard_stopper = pynput.keyboard.Listener(suppress=True) # for some reason you can't call the same function multiple times in the same area? (object loop?) idk it doesn't make sense to me.
# Disables keyboard events
    # keyboard_listener.start()
# Enable keyboard events
    # keyboard_listener.stop()

    # keyboard.block_key("left")  <--- this does not work


# CLOSING THE TERMINAL:     os.kill(os.getppid(), signal.SIGHUP)

# Keeps track of the window size. Unlike os.get_terminal_size(), this can be
# updated in place, so every file that uses size.lines / size.columns sees the new size
class WindowSize:
    def __init__(self):
        self.update()

    def update(self):
        current = os.get_terminal_size()
        self.lines = current.lines
        self.columns = current.columns
        os.environ['LINES'] = str(self.lines)
        os.environ['COLUMNS'] = str(self.columns)

size = WindowSize()
##### Window colours and title #####
# Mac Terminal lets other programs change the colours of a single tab, so the game
# sets its own tab to a dark background and light text when it starts. This only
# affects the game's window: the player's Terminal settings and other windows are
# left alone. In VS Code (or other terminal apps) this does nothing.
BACKGROUND_COLOUR = (20, 20, 20)      # match this to VS Code's terminal background
TEXT_COLOUR = (220, 220, 220)         # normal, uncoloured text
WINDOW_TITLE = "You Exist"

def set_terminal_colours():
    if os.environ.get("TERM_PROGRAM") != "Apple_Terminal":
        return
    try:
        my_tab = os.ttyname(1)   # e.g. /dev/ttys003, identifies the game's own tab
    except OSError:
        return
    to_apple = lambda rgb: "{" + ", ".join(str(v * 257) for v in rgb) + "}"   # Terminal uses 0-65535
    script = f"""
    tell application "Terminal"
        repeat with w in windows
            repeat with t in tabs of w
                if tty of t is "{my_tab}" then
                    set background color of t to {to_apple(BACKGROUND_COLOUR)}
                    set normal text color of t to {to_apple(TEXT_COLOUR)}
                    set bold text color of t to {to_apple(TEXT_COLOUR)}
                    -- Window title: the app itself is called "You Exist", so the title
                    -- is just the program's name, with all the extras switched off
                    try
                        set custom title of t to ""
                    end try
                    try
                        set title displays custom title of t to false
                    end try
                    try
                        set title displays device name of t to false
                    end try
                    try
                        set title displays shell path of t to false
                    end try
                    try
                        set title displays window size of t to false
                    end try
                    try
                        set title displays settings name of t to false
                    end try
                    try
                        set title displays file name of t to false
                    end try
                end if
            end repeat
        end repeat
    end tell
    """
    try:
        subprocess.run(["osascript", "-e", script], timeout=5,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass   # if it doesn't work, the game still runs with the player's normal colours

set_terminal_colours()

# Clear the folder name and folder icon Terminal shows in the title
sys.stdout.write("\033]7;\007\033]6;\007")
# In other terminal apps, set the title the standard way. (Not in Mac Terminal:
# there the program's own name, "You Exist", already is the title, and this
# would add a second copy.)
if os.environ.get("TERM_PROGRAM") != "Apple_Terminal":
    sys.stdout.write(f"\033]0;{WINDOW_TITLE}\007")
sys.stdout.flush()

##### Half-screen, no-memory display #####
# Old version (worked in VS Code but not in Terminal):
# command = "tput csr 1 $((LINES/2))"
# result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 0. Wipe the normal screen AND its scrollback first (this removes the
#    "Last login" lines and the launch command Terminal shows when the game opens)
sys.stdout.write("\033[H\033[2J\033[3J")
# 1. Switch to the terminal's "alternate screen". It has no scrollback,
#    so once a line scrolls away it's gone for good and can't be scrolled back to.
sys.stdout.write("\033[?1049h")
# 2. Clear it and put the cursor at the top
sys.stdout.write("\033[2J\033[H")
# 3. Only let text scroll between row 2 and halfway down the screen
#    (the same area the old tput command set up), then return the cursor to the top
def set_scroll_region():
    sys.stdout.write(f"\033[2;{size.lines // 2 + 1}r")

set_scroll_region()
sys.stdout.write("\033[H")
sys.stdout.flush()

# 4. Whenever the window is resized, macOS sends the game a SIGWINCH signal.
#    This catches it and redoes the half-screen setup for the new size.
def on_resize(signum, frame):
    old_lines = size.lines
    size.update()
    if size.lines >= old_lines:
        # Window got taller (or only wider): keep the cursor where it was
        sys.stdout.write("\0337")   # remember cursor position
        set_scroll_region()         # (this moves the cursor to the top)
        sys.stdout.write("\0338")   # put the cursor back
    else:
        # Window got shorter: the cursor might now be below the new halfway line,
        # so move it to the bottom of the new text area
        set_scroll_region()
        sys.stdout.write(f"\033[{size.lines // 2 + 1};1H")
    sys.stdout.flush()

signal.signal(signal.SIGWINCH, on_resize)


##### Automatic word wrapping #####
# Every print() and cprint() now goes through this, which moves a whole word onto
# the next line if it won't fit, instead of letting the terminal chop it in half.
# It always uses the CURRENT window width, so it keeps working after a resize.

import re
import builtins

_ESCAPE_CODE = re.compile(r"\x1b(\[[0-9;?]*[A-Za-z]|[78])")  # colour/cursor codes (take up no space)
_WORD_OR_SPACE = re.compile(r"\x1b(?:\[[0-9;?]*[A-Za-z]|[78])|\n|\r| +|[^ \n\r\x1b]+")

# Older versions of Mac Terminal can't show exact (24-bit) RGB colours and garble
# them, e.g. into a bright highlight. Exact colours are only used where they're
# supported; everywhere else each colour is swapped for the closest of the
# 256 colours every terminal understands.
import platform

def _supports_exact_colour():
    if os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit"):
        return True    # e.g. VS Code
    if os.environ.get("TERM_PROGRAM") == "Apple_Terminal":
        mac_version = platform.mac_ver()[0] or "0"
        return int(mac_version.split(".")[0]) >= 26   # Terminal got exact colour in macOS 26 (Tahoe)
    return False

EXACT_COLOUR_SUPPORTED = _supports_exact_colour()
_RGB_CODE = re.compile(r"\x1b\[(38|48);2;(\d+);(\d+);(\d+)m")
_CUBE_LEVELS = [0, 95, 135, 175, 215, 255]

def rgb_to_256(r, g, b):
    # Closest colour in the 6x6x6 colour cube
    nearest = lambda v: min(range(6), key=lambda i: abs(_CUBE_LEVELS[i] - v))
    ri, gi, bi = nearest(r), nearest(g), nearest(b)
    cube = (_CUBE_LEVELS[ri], _CUBE_LEVELS[gi], _CUBE_LEVELS[bi])
    cube_code = 16 + 36 * ri + 6 * gi + bi
    # Closest shade in the 24-step grey ramp
    gi_ = max(0, min(23, round((((r + g + b) / 3) - 8) / 10)))
    grey = 8 + 10 * gi_
    grey_code = 232 + gi_
    dist = lambda c: (c[0] - r) ** 2 + (c[1] - g) ** 2 + (c[2] - b) ** 2
    return grey_code if dist((grey, grey, grey)) < dist(cube) else cube_code

def _fix_colour_code(code):
    if EXACT_COLOUR_SUPPORTED:
        return code
    m = _RGB_CODE.fullmatch(code)
    if not m:
        return code
    layer, r, g, b = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    code_256 = FALLBACK_COLOURS.get((r, g, b)) or rgb_to_256(r, g, b)
    return f"\x1b[{layer};5;{code_256}m"

class WordWrapper:
    def __init__(self, stream):
        self.stream = stream      # the real terminal output
        self.col = 0              # how many characters are on the current line
        self.spaces = ""          # spaces waiting to be written before the next word

    def write(self, text):
        for piece in _WORD_OR_SPACE.findall(text):
            if _ESCAPE_CODE.fullmatch(piece):
                self.stream.write(_fix_colour_code(piece))
                if piece.endswith(("H", "J")):   # cursor jumped to a new spot
                    self.col = 0
            elif piece in ("\n", "\r"):
                self.stream.write(piece)
                self.col = 0
                self.spaces = ""
            elif piece.startswith(" "):
                self.spaces += piece
            else:  # a word
                width = size.columns
                if self.col > 0 and self.col + len(self.spaces) + len(piece) > width:
                    self.stream.write("\n")      # doesn't fit: start a new line
                    self.col = 0
                    self.spaces = ""
                self.stream.write(self.spaces + piece)
                self.col = (self.col + len(self.spaces) + len(piece))
                if self.col > width:             # a single word wider than the window
                    self.col %= width
                self.spaces = ""
        return len(text)

    def flush(self):
        # Write out any waiting spaces (e.g. "Name: " right before an input)
        if self.spaces and self.col + len(self.spaces) <= size.columns:
            self.stream.write(self.spaces)
            self.col += len(self.spaces)
        self.spaces = ""
        self.stream.flush()

    def __getattr__(self, name):
        # Anything else (isatty, fileno, encoding...) goes straight to the real terminal
        return getattr(self.stream, name)

sys.stdout = WordWrapper(sys.stdout)

# After the player types something and presses Enter, they're on a fresh line
_original_input = builtins.input
def _input_with_wrap(prompt=""):
    sys.stdout.flush()
    answer = _original_input(prompt)
    sys.stdout.col = 0
    return answer
builtins.input = _input_with_wrap

os.system('clear')
os.system('tput vi')


##### Random ass variables #####

lives_lived = 0 # loop each new life into the starting dialogue
all_there_is = 0

first_person = False
physical_form = False

##### Points #####

ponder = 0
charisma = 0 # Ability to persuade/convince the 'system' to go against what it was planning (e.g. death) - at the end try and persuade the being if you have enough charisma (end goal?)
physicality = 0 # Your physical body in whatever world you're in
confidence = 0 # Your sureness in your existence
morality = 0 # How good or bad of an existence you are
insanity = 0 # How insane you are (if reaches a certain point, you kill yourself)

class points: # maybe change it so that if change == 0, then you dont print (change) and only the current points?
    
    def ponder(change):
        global ponder
        ponder += change
        achievements.Thoughtful_One()
        achievements.No_Brains_All_Brawn()
        if change == 0:
            cprint(f"Ponder: {ponder}", "dark_grey")
        else:
            cprint(f"Ponder: {ponder} ({change})", "dark_grey")

    def charisma(change):
        global charisma
        charisma += change
        if change == 0:
            cprint(f"Charisma: {charisma}", "dark_grey")
        else:
            cprint(f"Charisma: {charisma} ({change})", "dark_grey")

    def physicality(change):
        global physicality
        physicality += change
        if change == 0:
            cprint(f"Physicality: {physicality}", "dark_grey")
        else:
            cprint(f"Physicality: {physicality} ({change})", "dark_grey")

    def confidence(change):
        global confidence
        confidence += change
        if change == 0:
            cprint(f"Confidence: {confidence}", "dark_grey")
        else:
            cprint(f"Confidence: {confidence} ({change})", "dark_grey")

    def morality(change):
        global morality
        morality += change
        achievements.Naughty_List()
        achievements.Teachers_Pet()
        if change == 0:
            cprint(f"Morality: {morality}", "dark_grey")
        else:
            cprint(f"Morality: {morality} ({change})", "dark_grey")

    def insanity(change):
        global insanity
        insanity += change
        achievements.Crazy_Dave()
        if change == 0:
            cprint(f"Insanity: {insanity}", "dark_grey")
        else:
            cprint(f"Insanity: {insanity} ({change})", "dark_grey")



##### Functions #####

# The folder the game files are in (works in VS Code, in the app, and with the launcher)
GAME_FOLDER = os.path.dirname(os.path.abspath(__file__))

def die(name, scroll=True):
    """Every death in the story ends with this. It records which death it was on
    your GoatCounter dashboard (as /death/<name>), then scrolls the screen away
    like the old ending_lines code did. Use scroll=False where the screen
    shouldn't scroll (e.g. just before the game closes the window)."""
    signal_thread = None
    try:
        from Home_Screen import track
        signal_thread = track(f"/death/{name}", f"Death: {name}")
    except Exception:
        pass   # tracking is never allowed to break the game
    if scroll:
        ending_lines = (int(size.lines)/2)
        if ending_lines == 1:
            print()
            ending_lines -= 1
        while ending_lines > 1:
            print()
            time.sleep(0.075)
            ending_lines -= 1
    elif signal_thread is not None:
        signal_thread.join(timeout=3)   # give the signal a moment to send before the game closes

def play_sound(filename):
    # Plays a sound from the Audio folder in the background, using the Mac's
    # built-in afplay command (no extra libraries needed). Missing files are skipped.
    path = os.path.join(GAME_FOLDER, "Audio", filename)
    if os.path.exists(path):
        subprocess.Popen(["afplay", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)

def rp(inp):
    punctuation = "\'().,"
    for symbol in punctuation:
        inp = inp.replace(symbol, '')
    return inp

import termios, select   # (not tty: it isn't packed into the app)

def wait():
    # Waits for any key press, without showing it on screen.
    # (Used to run bash for this, which made "bash" appear in the window title.)
    sys.stdout.flush()
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Read single keys, and don't show them on screen
        new_settings = termios.tcgetattr(fd)
        new_settings[3] &= ~(termios.ECHO | termios.ICANON)
        new_settings[6][termios.VMIN] = 1
        new_settings[6][termios.VTIME] = 0
        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
        os.read(fd, 1)
        # Keys like the arrows send several characters at once: swallow the rest,
        # so one press only ever moves the story on by one line
        while select.select([fd], [], [], 0.01)[0]:
            os.read(fd, 64)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def p(text):
    print(textwrap.fill(text, width=int(os.environ['COLUMNS']))) # also include line spacing here when it's being implemented
    wait()                                                       # or maybe line spacing is just a terminal setting, and you change a value that changes it in settings?

def printwrap(text):
    print(textwrap.fill(text, width=int(os.environ['COLUMNS']))) ### WILL HAVE TO REPLACE EVERY. SINGLE. PRINT. WITH PRINTWRAP (maybe do that at the very very end)
                                                                 ### INCLUDE THE SPACING HERE (likely do this after the very very end)

def printwrapne(text): # ne for 'no end'
    print(textwrap.fill(text, width=int(os.environ['COLUMNS'])), end="") # will need to watch out for replacing print functions with no end

def being(text):
    cprint(textwrap.fill(text, width=int(os.environ['COLUMNS'])), "red", attrs=["bold", "dark"])
    wait()

def voices(text):
    cprint(textwrap.fill(text, width=int(os.environ['COLUMNS'])), "light_grey", attrs=["dark"])
    wait()

def tvoices(text): # t for time - it's in that section where it's timed, not user input based (Bathe_in_Discourse)
    cprint(text, "dark_grey")

def tvoicesnoend(text):
    cprint(text, "dark_grey", end="")

def v2(text1, text2):
    text1_length = len(text1)
    text2_length = len(text2)
    os.environ['COLUMNS'] = str(size.columns)
    number_of_spaces_needed = int(os.environ['COLUMNS']) - text1_length - text2_length
    print(text1, end="")
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    print(text2)
    wait()

def v2no_wait(text1, text2):
    text1_length = len(text1)
    text2_length = len(text2)
    os.environ['COLUMNS'] = str(size.columns)
    number_of_spaces_needed = int(os.environ['COLUMNS']) - text1_length - text2_length
    print(text1, end="")
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    print(text2)

def v2being(text1, text2):
    text1_length = len(text1)
    text2_length = len(text2)
    os.environ['COLUMNS'] = str(size.columns)
    number_of_spaces_needed = int(os.environ['COLUMNS']) - text1_length - text2_length
    cprint(text1, "red", attrs=["bold", "dark"], end="")
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    cprint(text2, "red", attrs=["bold", "dark"])
    wait()

def centre(text): # Also prints italicised (Bathe_in_Discourse)
    text_length = len(text)
    number_of_spaces_needed = (int(os.environ['COLUMNS']) - text_length)/2
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    print("\x1B[3m" + text + "\x1B[0m")
    wait()

def v2v(text1, text2): # 2 voices, the colour of other voices (grey)
    text1_length = len(text1)
    text2_length = len(text2)
    os.environ['COLUMNS'] = str(size.columns)
    number_of_spaces_needed = int(os.environ['COLUMNS']) - text1_length - text2_length
    print(text1, end="")
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    cprint(text2, "light_grey", attrs=["dark"])
    wait()

def v2vb(text1, text2): # 2 voices, the colour of other voices (grey), b for backwards (voices come first)
    text1_length = len(text1)
    text2_length = len(text2)
    os.environ['COLUMNS'] = str(size.columns)
    number_of_spaces_needed = int(os.environ['COLUMNS']) - text1_length - text2_length
    cprint(text1, "light_grey", attrs=["dark"], end="")
    count = number_of_spaces_needed
    while count > 0:
        print(" ", end="")
        count -= 1
    print(text2)
    wait()


first_path = True

def rng(boundary): # okay this shit doesn't work just whack this thingo in whenever you want rng
    chance = random.random()
    global first_path
    if chance < boundary:
        first_path = True
    elif chance >= boundary:
        first_path = False



##### Emotions #####

loneliness_discovered = False
happiness_discovered = False
anger_discovered = False


class emotion(): 
    
    def discovered_loneliness(change: bool): # the idea of these is that in the end interaction, only the emotions you discover while playing will appear
        global loneliness_discovered
        loneliness_discovered = change
        return loneliness_discovered
    
    def loneliness(text):
        global loneliness_discovered
        if loneliness_discovered == True:
            print(f"\x1b[38;2;128;128;128m{textwrap.fill(text, width=int(os.environ['COLUMNS']))}\x1b[0m")
            wait()
        else:
            p(text)
    
    def discovered_happiness(change: bool):
        global happiness_discovered
        happiness_discovered = change
        return happiness_discovered

    def happiness(text):
        global happiness_discovered
        if happiness_discovered == True:
            print(f"\x1b[38;2;255;255;84m{textwrap.fill(text, width=int(os.environ['COLUMNS']))}\x1b[0m")
            wait()
        else:
            p(text)

    def discovered_anger(change: bool):
        global anger_discovered
        anger_discovered = change
        return anger_discovered
    
    def anger(text):
        global anger_discovered
        if anger_discovered == True:
            print(f"\x1b[38;2;212;67;37m{textwrap.fill(text, width=int(os.environ['COLUMNS']))}\x1b[0m")
            wait()
        else:
            p(text)


##### Buddies #####

buddy_discovered = False
lover_discovered = False
hater_discovered = False

buddy_name = "********"
grumpy_buddy_name = "********"
idiot_buddy_name = "********"
nerd_buddy_name = "********"
stoner_buddy_name = "********"
caveman_buddy_name = "********"
judger_buddy_name = "********"
preacher_buddy_name = "********"
lover_buddy_name = "********"
hater_buddy_name = "********"

##### WHEN NAMING A BUDDY, MAKE SURE TO GO {BUDDY'S NAME, e.g. idiot_buddy_name} = NAME_BUDDY.[BUDDY] (and then all the input shebang)

class name_buddy:

    def original(new_name): # maybe add a thing that says 'hey that's a bit of a mouthful' if you ask for a name too long (otherwise the textwrap thing will be a pain in the ass and it could break)
        global buddy_name
        buddy_name = str(new_name)
        return buddy_name
    
    def grump(new_name):
        global grumpy_buddy_name
        grumpy_buddy_name = str(new_name)
        return grumpy_buddy_name
    
    def idiot(new_name):
        global idiot_buddy_name
        idiot_buddy_name = str(new_name)
        return idiot_buddy_name
    
    def nerd(new_name):
        global nerd_buddy_name
        nerd_buddy_name = str(new_name)
        return nerd_buddy_name
    
    def stoner(new_name):
        global stoner_buddy_name
        stoner_buddy_name = str(new_name)
        return stoner_buddy_name
    
    def caveman(new_name):
        global caveman_buddy_name
        caveman_buddy_name = str(new_name)
        return caveman_buddy_name
    
    def judger(new_name):
        global judger_buddy_name
        judger_buddy_name = str(new_name)
        return judger_buddy_name
    
    def preacher(new_name):
        global preacher_buddy_name
        preacher_buddy_name = str(new_name)
        return preacher_buddy_name
    
    def lover(new_name):
        global lover_buddy_name
        lover_buddy_name = str(new_name)
        return lover_buddy_name
    
    def hater(new_name):
        global hater_buddy_name
        hater_buddy_name = str(new_name)
        return hater_buddy_name


class buddy():  
    def b(text):
        global buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(109, 226, 148, buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(109, 226, 148, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(buddy_name)))))
        wait()
    
    def grump(text):
        global grumpy_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(106, 29, 245, grumpy_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(106, 29, 245, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(grumpy_buddy_name)))))
        wait()

    def idiot(text):
        global idiot_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(107, 222, 247, idiot_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(107, 222, 247, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(idiot_buddy_name)))))
        wait()

    def nerd(text):
        global nerd_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(35, 79, 26, nerd_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(35, 79, 26, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(nerd_buddy_name)))))
        wait()

    def stoner(text):
        global stoner_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(183, 228, 150, stoner_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(183, 228, 150, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(stoner_buddy_name)))))
        wait()
    
    def caveman(text):
        global caveman_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(111, 41, 27, caveman_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(111, 41, 27, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(caveman_buddy_name)))))
        wait()
    
    def judger(text):
        global judger_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(188, 152, 216, judger_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(188, 152, 216, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(judger_buddy_name)))))
        wait()

    def preacher(text):
        global preacher_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(237, 114, 110, preacher_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(237, 114, 110, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(preacher_buddy_name)))))
        wait()

    def lover(text):
        global lover_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(212, 67, 166, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(212, 67, 166, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(lover_buddy_name)))))
        wait()

    def hater(text):
        global hater_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(230, 64, 37, hater_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 64, 37, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(hater_buddy_name)))))
        wait()


##### Achievements ####

Pickle_Monologue_Gotten = False
Naughty_List_Gotten = False
Teachers_Pet_Gotten = False
Lonely_Guy_Gotten = False
Smile_Gotten = False
Not_Done_Gotten = False
Crazy_Dave_Gotten = False
Quick_Death_Gotten = False
LSD_Overdose_Gotten = False
Unusual_Company_Gotten = False
Thoughtful_One_Gotten = False 
No_Brains_All_Brawn_Gotten = False
First_Person_Gotten = False
Cranky_Gotten = False
Backtracking_Gotten = False
Lover_Gotten = False
Kids_Gotten = False
Touch_Gotten = False
Vision_Gotten = False
Linguist_Gotten = False
Exist_Gotten = False


class achievements(): # Notification("Description").with_subtitle("Title").send()

    def Pickle_Monologue(): # IMPLEMENTED
        global Pickle_Monologue_Gotten
        if Pickle_Monologue_Gotten == False:
            Notification("Be graced with the knowledge of pickles").with_subtitle("Pickles...?").with_title("You Exist").send()
            Pickle_Monologue_Gotten = True
        else:
            pass
            
    def Naughty_List(): # IMPLEMENTED
        global Naughty_List_Gotten
        global morality
        if Naughty_List_Gotten == False:
            if morality <= (-5): # can change
                Notification("Reach a Morality score of -5").with_subtitle("Naughty List").with_title("You Exist").send()
                Naughty_List_Gotten = True
            else:
                pass
        else:
            pass

    def Teachers_Pet(): # IMPLEMENTED
        global Teachers_Pet_Gotten
        global morality
        if Teachers_Pet_Gotten == False:
            if morality >= (10): # can change
                Notification("Reach a Morality score of 10").with_subtitle("Teacher's Pet").with_title("You Exist").send()
                Teachers_Pet_Gotten = True
            else:
                pass
        else:
            pass

    def Lonely_Guy(): # IMPLEMENTED
        global Lonely_Guy_Gotten
        if Lonely_Guy_Gotten == False:
            Notification("Develop Loneliness").with_subtitle("Poor Guy :(").with_title("You Exist").send()
            Lonely_Guy_Gotten = True
        else:
            pass

    def Smile(): # IMPLEMENTED
        global Smile_Gotten
        global happiness_discovered
        if Smile_Gotten == False:
            if happiness_discovered == True:
                Notification("Develop Happiness").with_subtitle("Smile!").with_title("You Exist").send()
                Smile_Gotten = True
            else:
                pass
        else:
            pass

    def Not_Done(): # IMPLEMENTED
        global Not_Done_Gotten
        if Not_Done_Gotten == False:
            Notification("Die and restart for the first time").with_subtitle("One and... not done?").with_title("You Exist").send()
            Not_Done_Gotten = True
        else:
            pass

    def Crazy_Dave(): # IMPLEMENTED ⁡⁢⁣⁡
        global Crazy_Dave_Gotten
        global insanity
        if Crazy_Dave_Gotten == False:
            if insanity >= (10): # can change
                Notification("Reach an Insanity score of 10").with_subtitle("Crazy Dave").with_title("You Exist").send()
                play_sound("Crazy_Dave.wav")
                Crazy_Dave_Gotten = True
            else:
                pass
        else:
            pass

    def Quick_Death(): # IMPLEMENTED
        global Quick_Death_Gotten
        if Quick_Death_Gotten == False:
            Notification("Choose the fastest way to die").with_subtitle("Option B: Not to be").with_title("You Exist").send()
            Quick_Death_Gotten = True
        else:
            pass

    def LSD_Overdose(): # IMPLEMENTED
        global LSD_Overdose_Gotten
        if LSD_Overdose_Gotten == False:
            Notification("Eat the strange plant your mother told you not to").with_subtitle("Strange Lookin' Thing").with_title("You Exist").send() # maybe "Didn't your mother tell you not to eat strange things in the forest?"
            LSD_Overdose_Gotten = True
        else:
            pass

    def Unusual_Company(): # IMPLEMENTED
        global Unusual_Company_Gotten
        if Unusual_Company_Gotten == False:
            Notification("Develop a buddy to keep you company").with_subtitle("You're my best friend").with_title("You Exist").send()
            Unusual_Company_Gotten = True
        else:
            pass
            
    def Thoughtful_One(): # IMPLEMENTED
        global Thoughtful_One_Gotten
        global ponder
        if Thoughtful_One_Gotten == False:
            if ponder >= 10: # can change
                Notification("Reach a Ponder score of 10").with_subtitle("O' Thoughtful One").with_title("You Exist").send()
                Thoughtful_One_Gotten = True
            else:
                pass
        else:
            pass

    def No_Brains_All_Brawn(): # IMPLEMENTED
        global No_Brains_All_Brawn_Gotten
        global ponder
        if No_Brains_All_Brawn_Gotten == False:
            if ponder <= (-10): # can change
                Notification("Reach a Ponder score of -10").with_subtitle("No Brains All Brawn").with_title("You Exist").send()
                No_Brains_All_Brawn_Gotten = True
            else:
                pass
        else:
            pass

    def First_Person(): # IMPLEMENTED
        global First_Person_Gotten
        if First_Person_Gotten == False:
            Notification("Develop the First Person").with_subtitle("I, Me, Mine").with_title("You Exist").send()
            First_Person_Gotten = True
        else:
            pass

    def Cranky(): # IMPLEMENTED
        global Cranky_Gotten
        if Cranky_Gotten == False:
            Notification("Develop Anger").with_subtitle("You No Likey").with_title("You Exist").send()
            Cranky_Gotten = True
        else:
            pass

    def Backtracking(): # IMPLEMENTED
        global Backtracking_Gotten
        if Backtracking_Gotten == False:
            Notification("Turn tail on the opportunity of a lifetime").with_subtitle("Scaredy-cat").with_title("You Exist").send() # Scaredy-cat
            Backtracking_Gotten = True
        else:
            pass

    def Lover(): # GET RID OF
        global Lover_Gotten
        if Lover_Gotten == False:
            Notification("Find your true love").with_subtitle("Mi Amor").with_title("You Exist").send()
            Lover_Gotten = True
        else:
            pass

    def Kids(): # GET RID OF
        global Kids_Gotten
        if Kids_Gotten == False:
            Notification("Have... kids?").with_subtitle("Dim the lights, baby").with_title("You Exist").send()
            Kids_Gotten = True
        else:
            pass
    
    def Touch():
        global Touch_Gotten
        if Touch_Gotten == False:
            Notification("Develop the sensation of touch").with_subtitle("Supple Skin").with_title("You Exist").send()
            Touch_Gotten = True
        else:
            pass

    def Vision():
        global Vision_Gotten
        if Vision_Gotten == False:
            Notification("Develop the sensation of sight").with_subtitle("Who turned the lights on?").with_title("You Exist").send()
            Vision_Gotten = True
        else:
            pass

    def Linguist(): # IMPLEMENTED
        global Linguist_Gotten
        if Linguist_Gotten == False:
            Notification("Discover the beauty of language").with_subtitle("Little Linguist Bitch").with_title("You Exist").send()
            Linguist_Gotten = True
        else:
            pass

    def Exist(): # Finish an End Interaction
        global Exist_Gotten
        if Exist_Gotten == False:
            Notification("Live life to the fullest").with_subtitle("Exist").with_title("You Exist").send()
            Exist_Gotten = True
        else:
            pass



# Achievement for discovering 100% of the game (the first time)
# Achievement for REALLY discovering 100% of the game (after Finale)






##### Audio #####

#def threaded_function(audio, volume_change):
#    sfx = pydub.AudioSegment.from_mp3(audio)
#    sfx = sfx + int(volume_change)
#    play(sfx)


#sound = NSSound.alloc()
#sound.initWithContentsOfFile_byReference_("Audio/Crazy_Dave.mp3", True)
#sound.play() -> DOESN'T WAIT TO PLAY THE WHOLE FILE, MOVES ON IMMEDIATELY (THIS IS GOOD!)


#class Audio(): 
#
#    def ambience1(): # EXAMPLE
#        thread = Thread(target = threaded_function, args = (r"You Exist/Audio/Ambience1.mp3", )) # need to figure out how to change volume of it partway through playing it
#        thread.start()                                                                           # either that or just have music that can be overlapped easily and/or is short and thus doesn't need to be faded out
#    
#    def crazy_dave(v_change):
#        thread = Thread(target = threaded_function, args = ("Audio/Crazy_Dave.mp3", v_change, ))
#        thread.start()

    

##### Launch counter #####
# Each time the game starts, this quietly tells GoatCounter "someone launched the game",
# so you can see launches on your GoatCounter dashboard. It runs in the background,
# never slows the game down, and silently gives up if there's no internet.
LAUNCH_COUNTER = "https://tgowen909.goatcounter.com/count"   # <-- put your GoatCounter code here

def count_launch():
    if "YOURCODE" in LAUNCH_COUNTER:
        return   # not set up yet
    if os.environ.get("TERM_PROGRAM") == "vscode":
        return   # don't count your own test runs in VS Code
    if os.environ.get("YOU_EXIST_RESTARTED"):
        return   # returning to the home screen isn't a new launch

    def send():
        try:
            import urllib.request, urllib.parse, ssl
            try:
                import certifi
                context = ssl.create_default_context(cafile=certifi.where())
            except ImportError:
                context = ssl.create_default_context()
            params = urllib.parse.urlencode({"p": "/launch", "t": "Game launched", "rnd": random.random()})
            request = urllib.request.Request(
                f"{LAUNCH_COUNTER}?{params}",
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) You-Exist-game"},
            )
            urllib.request.urlopen(request, timeout=5, context=context)
        except Exception:
            pass

    import threading
    threading.Thread(target=send, daemon=True).start()

count_launch()



##### Saved achievements #####
# Remembers which achievements a player has unlocked, so they stay unlocked
# between sessions and each one only ever pops up once.
# The save file lives outside the game folder, because the launcher clears out
# anything in the game folder that isn't on GitHub.
import json

SAVE_FILE = os.path.expanduser("~/Library/Application Support/You Exist/save.json")
SAVING_ON = os.environ.get("TERM_PROGRAM") != "vscode"   # VS Code test runs start fresh and save nothing

def load_save():
    try:
        with open(SAVE_FILE) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}   # no save yet (or it's damaged): start fresh

def write_save(data):
    try:
        os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
        temp_file = SAVE_FILE + ".tmp"
        with open(temp_file, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(temp_file, SAVE_FILE)   # swap in all at once, so a crash can't half-write it
    except OSError:
        pass   # couldn't save: the game carries on regardless

save_data = load_save() if SAVING_ON else {}
save_data.setdefault("achievements", [])

# 1. Mark everything already unlocked as "gotten", so it won't pop up again
for name in save_data["achievements"]:
    if f"{name}_Gotten" in globals():
        globals()[f"{name}_Gotten"] = True

# 2. Wrap every achievement so that the moment one is unlocked, it's saved
def _save_when_unlocked(name, check):
    def wrapper(*args, **kwargs):
        was_gotten = globals()[f"{name}_Gotten"]
        result = check(*args, **kwargs)
        if not was_gotten and globals()[f"{name}_Gotten"] and SAVING_ON:
            save_data["achievements"].append(name)
            write_save(save_data)
        return result
    return staticmethod(wrapper)

for name, check in list(vars(achievements).items()):
    if callable(check) and f"{name}_Gotten" in globals():
        setattr(achievements, name, _save_when_unlocked(name, check))