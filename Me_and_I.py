# a combination of I_Am_Me and Am_I_Me

# I_Am_Me:
    # i have just accepted the fact  the first person sentience i have gained
        # perhaps I settle with my existence, maybe end up dying in one of them in that I should restart and try to figure out what's happened?
        # Check Testing_the_World_Script for ideas

# Am_I_Me:
    # I have just elected to fret over the fact that I have now gained first-person sentience
        # maybe i will question that since I *was* something else 'before', if 'later on' I will be something new?
        # you could choose to investigate the whole past/future thing, or continue to question ???
            # if choose to investigate the past, could begin to discover things, and the being then kills you
            # if investigating the future, ...

# Path: 
from You_Exist_Imports import *

p("balls (Me_and_I)")


achievements.First_Person()
story = ["You are stuck on the idea that your thoughts aren't what they should be.", "As of yet, you had only been thinking in concepts.", "Moments.", "But... shouldn't they be *yours*?", 
         "Not just something you have, but something you own.", "Not yours, rather...", "Mine.", "I jolt - this was the first time I had heard anything like this - thoughts that were... mine.", 
         "I didn't know how to react - was this me?", "If this is me, then who *was* I?", "I falter.", "Am I okay?", "Am I... me?", 
         "I know only have two options: do I continue to (fret) over the ramifications of my newfound sentience or simply (accept) what I am?"] 
for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "fret" and choice != "accept":
            print("I swear I just said I only had two options, and yet here I am thinking of '" + choice + ".'")
            wait()
            print("How about this time I just decide to (fret) over or (accept) what I am?")
            choice = rp(input("> ").lower().strip())

        if choice == "fret": # FILE
            points.confidence(-1) # Confidence - 1
            
            
        elif choice == "accept": # FILE
            points.confidence(1)
            points.charisma(1) # Confidence + 1, Charisma + 1
    