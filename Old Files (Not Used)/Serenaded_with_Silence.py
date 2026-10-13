# You have just elected to ignore  the distant voices and serenade yourself with silence
    # gain 1 or 2 ponder points;
    # ask yourself pointless questions, maybe gain some more ponder points,
    # question why your life was the way it was
    # question your existence, realise you've reached a dead end, 'fizzle out' of existence and gain a charisma point
# Path: no > body > sounds > quieten > ignore

from You_Exist_Imports import *

print("balls (serenaded with silence)")

story = ["", ""]

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
    
