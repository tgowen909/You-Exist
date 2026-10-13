# i have just accepted the fact  the first person sentience i have gained
    # perhaps I settle with my existence, maybe end up dying in one of them in that I should restart and try to figure out what's happened?
    # Check Testing_the_World_Script for ideas
# Path:

from You_Exist_Imports import *

print("balls (I_Am_Me)")

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