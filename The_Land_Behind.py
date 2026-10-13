# You have just elected to go behind you, where you didn't smell anything
    # go there by not pulling yourself to the 'smell (there's none), but you instead push yourself away from the other smells
    # smell something unknown, turns out to be a bunch of other existences,
    # maybe you feel 'unrivalled potential' in developing another sense of your choice,
        # or just all of the senses, or a select few.
# Path: no > body > smells > behind

from You_Exist_Imports import *


print("balls (the land behind)")

story = ["", ""]

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "" and choice != "":
            print("")
            wait()
            print("")
            choice = rp(input("> ").lower().strip())

        if choice == "":
            story = ["", ""]
            
        elif choice == "":
            story = ["", ""]