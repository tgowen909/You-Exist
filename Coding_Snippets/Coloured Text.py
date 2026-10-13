from termcolor import cprint, colored
import termcolor
import os

def cp_aqua(text):
    os.system('''printf "\x1b[38;2;0;255;255m''' + text + '''\x1b[0m\n"''')

cp_aqua("balls")

cprint('This text is red!','red', 'on_green')

print(colored('This text is red!','dark_grey'))

# light_grey, dark_grey, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan.

cprint("Hello there you wonderful person, how are you going? (black, dark)", "black", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (black)", "black")
cprint("Hello there you wonderful person, how are you going? (dark grey, dark)", "dark_grey", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (dark grey)", "dark_grey")
cprint("Hello there you wonderful person, how are you going? (grey, dark)", "grey", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (grey)", "grey")

cprint("Hello there you wonderful person, how are you going? (green, dark)", "green", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (green)", "green")
cprint("Hello there you wonderful person, how are you going? (light green)", "light_green")
cprint("Hello there you wonderful person, how are you going? (light green, dark)", "light_green", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (red, dark)", "red", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (red)", "red")
cprint("Hello there you wonderful person, how are you going? (light red)", "light_red")
cprint("Hello there you wonderful person, how are you going? (light red, dark)", "light_red", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (yellow, dark)", "yellow", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (yellow)", "yellow")
cprint("Hello there you wonderful person, how are you going? (light yellow)", "light_yellow")
cprint("Hello there you wonderful person, how are you going? (light yellow, dark)", "light_yellow", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (blue, dark)", "blue", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (blue)", "blue")
cprint("Hello there you wonderful person, how are you going? (light blue)", "light_blue")
cprint("Hello there you wonderful person, how are you going? (light blue, dark)", "light_blue", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (magenta, dark)", "magenta", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (magenta)", "magenta")
cprint("Hello there you wonderful person, how are you going? (light magenta)", "light_magenta")
cprint("Hello there you wonderful person, how are you going? (light magenta, dark)", "light_magenta", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (cyan, dark)", "cyan", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (cyan)", "cyan")
cprint("Hello there you wonderful person, how are you going? (light cyan)", "light_cyan")
cprint("Hello there you wonderful person, how are you going? (light cyan, dark)", "light_cyan", attrs=["dark"])

cprint("Hello there you wonderful person, how are you going? (white, dark)", "white", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (white)", "white")
cprint("Hello there you wonderful person, how are you going? (normal, dark)", attrs=["dark"])
cprint("Hello there you wonderful person, how are you going? (normal)")
cprint("Hello there you wonderful person, how are you going? (light grey)", "light_grey")
cprint("Hello there you wonderful person, how are you going? (light grey, dark)", "light_grey", attrs=["dark"])
















# make different characters different colours
# changes depending on person/personality




##### COLOURS:

### Existences
# red, attrs=["bold", "dark"]: the being talking to you (about to die)
# attrs["bold"]: the being giving you hints or trying to control you (talking to you not when you're about to die)

### Emotions
# grey: loneliness
# yellow: happiness
# light




