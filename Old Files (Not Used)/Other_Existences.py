# You have just elected to try interact with the voices, and will likely meet one soon
    # maybe they are more developed, know their name and whatnot
    # they ask you yours (not know = -1 confidence; choose name = +1 physicality) 
# Path: no > body > sounds > listen > interact

from You_Exist_Imports import *

print("balls (other existences)")

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
