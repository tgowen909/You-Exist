# You have just elected that the regret you felt was out of the goodness of your heart, and you are now going to pursue that (emotion: kindness)
    # You can then go on to questioning the emotion of regret you felt, which can be another emotion
    # You can go forward and develop more emotions after, which speak to you in different colours
# Path: 

from You_Exist_Imports import *

print("balls (pursuing_kindness)")


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