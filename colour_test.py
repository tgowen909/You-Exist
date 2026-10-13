# Run this in the VS Code terminal, take a screenshot, and use a colour picker
# on each solid block to get the exact colour VS Code shows.
# (Blocks are easier to pick from than letters, which have blurry edges.)

from termcolor import cprint

BLOCK = "██████████  "

print("\nNamed colours (termcolor):\n")
cprint(BLOCK + "1. The being            red, bold + dark", "red", attrs=["bold", "dark"])
cprint(BLOCK + "2. Voices               light_grey, dark", "light_grey", attrs=["dark"])
cprint(BLOCK + "3. Point stats          dark_grey", "dark_grey")
cprint(BLOCK + "4. Timed voices         grey, dark", "grey", attrs=["dark"])
cprint(BLOCK + "5. Bold narration       bold, no colour", attrs=["bold"])
print(BLOCK + "6. Normal text          no colour")

print("\nExact RGB colours (buddies and emotions):\n")
rgb_colours = [
    ("Buddy", (30, 230, 140)),
    ("Grumpy buddy", (115, 20, 255)),
    ("Idiot buddy", (35, 225, 250)),
    ("Nerd buddy", (10, 80, 15)),
    ("Stoner buddy", (170, 230, 140)),
    ("Caveman buddy", (120, 35, 20)),
    ("Judger buddy", (195, 150, 220)),
    ("Preacher buddy", (255, 105, 105)),
    ("Lover buddy", (230, 50, 170)),
    ("Hater buddy", (250, 40, 0)),
    ("Loneliness", (128, 128, 128)),
    ("Happiness", (255, 255, 0)),
    ("Anger", (230, 50, 10)),
]
for name, (r, g, b) in rgb_colours:
    print(f"\033[38;2;{r};{g};{b}m{BLOCK}\033[0m{name}  (code says {r}, {g}, {b})")
print()
