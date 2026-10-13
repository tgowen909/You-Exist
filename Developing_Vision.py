# You have just chosen to predict the world around you (sight)
    # obviously some very eloquent descriptions of the world around you (when it gets to it)
    # for now, maybe get to a stage where you wonder about what you look like, given you can see other things
# Path: yes > more > body > predict

# ACHIEVEMENT: VISION

# like spawn in your sight or whatever (maybe a choice as to what you think you'll see - make them wildly contrasting)
# perhaps a go insane possibility?
# Create like an orb of light
# 'shadows lurking in the dark' that kinda thing - add some mysteriousness
# ponder whether you should look at yourself or the world around you
    # if look at yourself, maybe start to amalgamate a body of sorts (human likely, maybe another kind? - maybe even more choices to change that)
    # once you start to see your own body and such, perhaps you realise the space around you and begin to explore
    # then other existences (that have the same body (human, animal, etc.) as you) start to appear, and you try and converse with them
    # realise they're making noise, but you can't hear???
    # develop hearing (ACHIEVEMENT)
    # then realise you don't understand them
        # lost cause or keep trying choices
        # if keep trying develop language (ACHIEVEMENT)
        # I guess this is the becoming human one (vision is the fundamental sense for humanity, everything builds off that)
        # (sink a lot of time into this, add lots of choices where you can die)
        # maybe meet their community and stuff, and your interactions with them provide opportunity for you to fuck things up.
        # have a 'try and fit in' choice or be unique
            # unique kills you obviously cause we don't like people that stand out
            # have a final 'BECOME HUMAN' achievement if you develop all the senses


### MAYBE MAKE IT THAT FOR SOME REASON YOU ACTUALLY DONT HAVE THE ABILITY TO HEAR, YET YOU DISCOVER ALL THE OTHER SENSES?
### WOULD MEAN YOU DONT HAVE TO WORRY ABOUT INTERACTING TEXT

from You_Exist_Imports import *

print("balls (developing vision)")

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
