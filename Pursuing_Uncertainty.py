# You have chosen to explore your mind and your uncertainty (developing emotions)
    # YOUR DIFFERENT EMOTIONS HAVE DIFFERENT COLOURS AND THEY START TALKING TO YOU
# Path: yes > more > mind > pursue

from You_Exist_Imports import *

print("balls (Pursuing Uncertainty)")

story = []

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = input("> ").lower().strip()

        while choice != "" and choice != "":
            print("")
            wait()
            print("")
            choice = rp(input("> ").lower().strip())

        if choice == "":
            story = ["", ""]
            
        elif choice == "":
            story = ["", ""]