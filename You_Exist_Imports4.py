from __future__ import print_function
import os
from termcolor import cprint
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

class WordWrapper:
    def __init__(self, stream):
        self.stream = stream      # the real terminal output
        self.col = 0              # how many characters are on the current line
        self.spaces = ""          # spaces waiting to be written before the next word

    def write(self, text):
        for piece in _WORD_OR_SPACE.findall(text):
            if _ESCAPE_CODE.fullmatch(piece):
                self.stream.write(piece)
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
            cprint(f"Ponder: {ponder}", "grey")
        else:
            cprint(f"Ponder: {ponder} ({change})", "grey")

    def charisma(change):
        global charisma
        charisma += change
        if change == 0:
            cprint(f"Charisma: {charisma}", "grey")
        else:
            cprint(f"Charisma: {charisma} ({change})", "grey")

    def physicality(change):
        global physicality
        physicality += change
        if change == 0:
            cprint(f"Physicality: {physicality}", "grey")
        else:
            cprint(f"Physicality: {physicality} ({change})", "grey")

    def confidence(change):
        global confidence
        confidence += change
        if change == 0:
            cprint(f"Confidence: {confidence}", "grey")
        else:
            cprint(f"Confidence: {confidence} ({change})", "grey")

    def morality(change):
        global morality
        morality += change
        achievements.Naughty_List()
        achievements.Teachers_Pet()
        if change == 0:
            cprint(f"Morality: {morality}", "grey")
        else:
            cprint(f"Morality: {morality} ({change})", "grey")

    def insanity(change):
        global insanity
        insanity += change
        achievements.Crazy_Dave()
        if change == 0:
            cprint(f"Insanity: {insanity}", "grey")
        else:
            cprint(f"Insanity: {insanity} ({change})", "grey")



##### Functions #####

def rp(inp):
    punctuation = "\'().,"
    for symbol in punctuation:
        inp = inp.replace(symbol, '')
    return inp

def wait():
    sys.stdout.flush()
    os.system("/bin/bash -c 'read -s -n 1 -p \"\"'")

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
    cprint(text, "grey", attrs=["dark"])

def tvoicesnoend(text):
    cprint(text, "grey", attrs=["dark"], end="")

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
            print(f"\x1b[38;2;255;255;0m{textwrap.fill(text, width=int(os.environ['COLUMNS']))}\x1b[0m")
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
            print(f"\x1b[38;2;230;50;10m{textwrap.fill(text, width=int(os.environ['COLUMNS']))}\x1b[0m")
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
        print("\033[38;2;{};{};{}m{}\033[39m".format(30, 230, 140, buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(30, 230, 140, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(buddy_name)))))
        wait()
    
    def grump(text):
        global grumpy_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(115, 20, 255, grumpy_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(115, 20, 255, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(grumpy_buddy_name)))))
        wait()

    def idiot(text):
        global idiot_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(35, 225, 250, idiot_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(35, 225, 250, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(idiot_buddy_name)))))
        wait()

    def nerd(text):
        global nerd_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(10, 80, 15, nerd_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(10, 80, 15, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(nerd_buddy_name)))))
        wait()

    def stoner(text):
        global stoner_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(170, 230, 140, stoner_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(170, 230, 140, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(stoner_buddy_name)))))
        wait()
    
    def caveman(text):
        global caveman_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(120, 35, 20, caveman_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(120, 35, 20, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(caveman_buddy_name)))))
        wait()
    
    def judger(text):
        global judger_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(195, 150, 220, judger_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(195, 150, 220, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(judger_buddy_name)))))
        wait()

    def preacher(text):
        global preacher_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(255, 105, 105, preacher_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(255, 105, 105, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(preacher_buddy_name)))))
        wait()

    def lover(text):
        global lover_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(230, 50, 170, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 50, 170, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(lover_buddy_name)))))
        wait()

    def hater(text):
        global hater_buddy_name
        print("\033[38;2;{};{};{}m{}\033[39m".format(250, 40, 0, hater_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(250, 40, 0, textwrap.fill(text, width=(int(os.environ['COLUMNS'])-len(hater_buddy_name)))))
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
                Notification("Reach an Insanity score of 10").with_subtitle("Crazy Dave").with_title("You Exist")._with_content_image("/Users/tobyowen/Documents/Coding/You Exist/Images/logo.ico").send() # play the crazy dave sound
                #Audio.crazy_dave(0)
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

    



