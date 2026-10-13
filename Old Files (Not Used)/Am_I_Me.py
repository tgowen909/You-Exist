# I have just elected to fret over the fact that I have now gained first-person sentience
    # maybe i will question that since I *was* something else 'before', if 'later on' I will be something new?
    # you could choose to investigate the whole past/future thing, or continue to question ???
        # if choose to investigate the past, could begin to discover things, and the being then kills you
        # if investigating the future, ...
# Path: 

from You_Exist_Imports import *


print("balls (Am_I_Me?)")
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