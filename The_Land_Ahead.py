# dark, ominous (still gotta figure this one out)
# Path: no > body > smells > forwards

from You_Exist_Imports import *

print("balls (the land ahead)")

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