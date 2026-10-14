
from You_Exist_Imports import *

# Finds the story files in whatever folder the game is running from
# def resource_path(name):
#    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#    return os.path.join(base, name)
def resource_path(name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)

#pygame.mixer.init()
#crash_sound = pygame.mixer.Sound("/Users/tobyowen/Documents/Coding/You Exist/Audio/Crazy_Dave.wav")
#pygame.mixer.Sound.play(crash_sound)
#time.sleep(0.3)
#pygame.mixer.Sound.set_volume(crash_sound, 5)
#pygame.mixer.Sound.fadeout(time=1,)

#pygame.mixer.music.fadeout()

from Home_Screen import home_screen, start_of_life, finish_run
home_screen(globals())

##### Story #####
while True:
    start_of_life(globals())
    cprint("You exist.", attrs=["bold"])
    points.ponder(0)
    points.charisma(0)
    points.physicality(0)
    points.confidence(0)
    points.morality(0)
    points.insanity(0)
    wait()
    story = ["There is no before, only the now.", "The present.", "You wonder... is this all there is?"]
    for i, sentence in enumerate(story):
        print(sentence, end="")
        if i < len(story) - 1:
            print()
            wait()
        else:
            choice = rp(input("\n> ").lower().strip())
            
            while choice != "yes" and choice != "no":
                p(f"Your half-assed answer of '{choice}' doesn't satisfy your fervent curiosity.")
                print("Perhaps a simple yes or no would suffice?")
                choice = rp(input("> ").lower().strip())

            if choice == "yes": # DONE
                points.confidence(-1) # Confidence - 1
                all_there_is += 1
                if all_there_is >= 2:
                    points.insanity(1)
                story = ["That's it?", "A few brief moments of *something*, and then... gone?", "You wonder if this is all your existence will weigh up to.", "Is there something (more) or are you just a (speck), waiting to be snuffed out?"]
                for i, sentence in enumerate(story):
                    print(sentence)
                    if i < len(story) - 1:
                        wait()
                    else:
                        choice = rp(rp(input("> ").lower().strip()))   

                        while choice != "more" and choice != "speck":
                            p("'" + choice + "' crosses your mind, but you quickly shut it down.")
                            print("You are fixed on determining what you are - something (more) or a (speck)?")
                            choice = rp(rp(input("> ").lower().strip()))

                        if choice == "more": # DONE
                            points.charisma(1) # Charisma + 1
                            story = ["But your confidence in your existence has already wavered.", "Having just determined there might be more to your feeble actuality, you desperately struggle to solidify your being.", 
                                     "You feel yourself slipping.", "How is that even possible? What is it that's 'slipping'?", "Is it some kind of physical (body), or a figment of your (mind)?"]
                            for i, sentence in enumerate(story): 
                                print(sentence)
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    choice = rp(rp(input("> ").lower().strip()))   

                                    while choice != "body" and choice != "mind":
                                        p("You feel this is an important decision.")
                                        p("You don't think '" + choice + "' is important enough.")
                                        print("You come to the conclusion that you need to choose between your (body) or your (mind).")
                                        choice = rp(rp(input("> ").lower().strip()))

                                    if choice == "body": # DONE
                                        points.physicality(1) 
                                        story = ["With a newfound sense of determination, you begin to question the physical reality in which you lie.", "Your world thus far has consisted of only your thoughts.", 
                                                 "But what *are* you?", "*Where* are you?", "If you were to experience whatever is around you...", "Would it be to (predict) what is to come, or to (feel) it in the moment?"]
                                        for i, sentence in enumerate(story):
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(rp(input("> ").lower().strip()))   

                                                while choice != "predict" and choice != "feel": 
                                                    p("Perhaps your determination needs more determination.")
                                                    print("You remind yourself - would you (predict) the world around you, or (feel) it in the moment?")
                                                    choice = rp(rp(input("> ").lower().strip()))

                                                if choice == "predict": # FILE
                                                    points.ponder(1) 
                                                    with open(resource_path("Developing_Vision.py")) as f:
                                                        code = f.read() #################### Developing_Vision
                                                        exec(code)      #################### Developing_Vision
                                                    
                                                elif choice == "feel": # FILE
                                                    points.confidence(1) 
                                                    with open(resource_path("Developing_Touch.py")) as f:
                                                        code = f.read() #################### Developing_Touch
                                                        exec(code)      #################### Developing_Touch


                                        
                                    elif choice == "mind": # DONE
                                        points.ponder(1) # Ponder + 1
                                        story = ["With a newfound sense of determination, you begin to ponder your internal dialogue.", "You have some form of sentience, that much is evident.", "How, though, you are unsure.", 
                                                 "Unsure...", "Uncertainty...", "You cannot shake this nagging feeling of what may or may not be.", "You decide that you must either (ignore) your qualms, or (pursue) this feeling of yours."] 
                                        for i, sentence in enumerate(story):
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(input("> ").lower().strip())   

                                                while choice != "ignore" and choice != "pursue":
                                                    p("After throwing around the idea of '" + choice + "', you determine this is no laughing matter.")
                                                    print("You must choose to either (ignore) or (pursue) your fleeting uncertainty.")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "ignore": # END
                                                    points.charisma(-1)
                                                    points.ponder(-1) # Ponder - 1, Charisma - 1
                                                    story = ["...", "*sigh*", "You were so close.", "Given your start, I never thought you'd get even this far.", "But it seems it was all false hope.", "Sometimes, even you surprise me.", 
                                                             "Your fear - your *reluctance* - to be anything more than you were spawned as leaves a sick taste in my mouth.", "Grow a little, for crying out loud.", 
                                                             "Although I suppose that's rather hypocritical of me.", "After all, all you know after this is that..."]
                                                    for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            ending_lines = (int(size.lines)/2)
                                                            if ending_lines == 1:
                                                                print()
                                                                ending_lines -=1
                                                            while ending_lines > 1:
                                                                print()
                                                                time.sleep(0.075)
                                                                ending_lines -= 1
                                                            
                                                elif choice == "pursue": # FILE
                                                    points.ponder(1) 
                                                    points.charisma(1) # Ponder + 1, Charisma + 1
                                                    with open(resource_path("Pursuing_Uncertainty.py")) as f:                ###### NO NEED TO KEEP IT, DELETE (EVERYWHERE AT THE END OF TIME REFERENCE)
                                                        code = f.read()#################### Pursuing_Uncertainty
                                                        exec(code) ####################     Pursuing_Uncertainty



                        elif choice == "speck": # END
                            points.insanity(1)
                            points.confidence(-2) # Insanity + 1, Confidence - 2
                            story = ["...", "Well that was short-lived.", "Frankly, I'm disappointed.", "I thought this little experiment would last a little longer.", "To think I believed you would be something more.", 
                                     "Something... different.", "...", "But perhaps I was foolish to think such things.", "Perhaps I was naive.", "No matter, we can always start again.", 
                                     "After all, you won't know anything other than..."] 
                                    # Notice how it goes into first person briefly. This is hinting at there being something more
                            for i, sentence in enumerate(story):
                                cprint(sentence, "red", attrs=["bold", "dark"])
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    wait()
                                    ending_lines = (int(size.lines)/2)
                                    achievements.Quick_Death()
                                    if ending_lines == 1:
                                        print()
                                        os.system('clear')
                                        ending_lines -=1
                                    while ending_lines > 1:
                                        print()
                                        time.sleep(0.075)
                                        ending_lines -= 1
                                    


                                    
            elif choice == "no": 
                points.confidence(1)
                points.ponder(1) # Confidence + 1, Ponder + 1
                story = ["You realise there must be more.", "You are here, but...", "Where is *here*?", "And who *are* you?", 
                         "You ponder, torn between questioning the world you are in, or yourself.", "Your (body) or your (mind)?"]
                for i, sentence in enumerate(story):
                    print(sentence)
                    if i < len(story) - 1:
                        wait()
                    else:
                        choice = rp(input("> ").lower().strip())   

                        while choice != "body" and choice != "mind":
                            p("You feel this is an important decision.")
                            p("You don't think '" + choice + "' is important enough.")
                            print("You come to the conclusion that you need to choose between your (body) or your (mind).")
                            choice = rp(input("> ").lower().strip())

                        if choice == "body": # DONE
                            points.physicality(2) # Physicality + 2
                            story = ["Your body.", "It is you - theoretically.", "You believe that, hypothetically, your existence must be... *somewhere*.", "Where, however, is the question you keep asking.", 
                                     "You toss up the idea of being in some kind of physical space.", "You struggle to comprehend how your world could be any more than the thoughts you have, but you press on nonetheless.", 
                                     "You wonder if this potential physical space is something you can experience.", "You speculate a world of (sounds) and a world of (smells), but you cannot decide which you would rather."]
                            for i, sentence in enumerate(story):
                                print(sentence)
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    choice = rp(input("> ").lower().strip())   

                                    while choice != "sounds" and choice != "smells":
                                        print("You aren't sure if '" + choice + "' is a valid way of perceiving the world.")
                                        wait()
                                        print("To combat this, you decide to stick to (sounds) or (smells).")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "sounds": # DONE
                                        points.charisma(1)
                                        story = ["You decide that a world of noise is one that you would prefer.", "As if prompted by your conviction, a cacophony of sounds swells in your mind.", 
                                                 "Layers upon layers of pitches echo, near driving out all ability to think.", "Nothing is legible.", "You do not know if it will ever end.", "You do not know if they will ever stop.", 
                                                 "You do not know whether you should (listen) to these sounds, or perhaps just (bathe) in the discourse."]
                                        for i, sentence in enumerate(story):
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(input("> ").lower().strip())   

                                                while choice != "listen" and choice != "bathe": 
                                                    p("At this point, you only see yourself having the ability to (listen) or (bathe) in the sounds.")
                                                    print("The noise is too much for you to do anything else.")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "listen": # FILE
                                                    points.charisma(1)
                                                    points.insanity(1)
                                                    with open(resource_path("Hear_the_Voices.py")) as f: 
                                                        code = f.read() ########## Hear_the_Voices
                                                        exec(code)      ########## Hear_the_Voices
                                                

                                                elif choice == "bathe": # FILE
                                                    points.confidence(1) 
                                                    points.insanity(1) 
                                                    with open(resource_path("Bathe_in_Discourse.py")) as f: 
                                                        code = f.read() ########## Bathe_in_Discourse
                                                        exec(code)      ########## Bathe_in_Discourse 



                                    elif choice == "smells": # DONE
                                        points.charisma(1) # Charisma + 1
                                        story = ["Your curiosity leads you to the conclusion of smells as how you choose to perceive the world.", "You wonder how smelling could possibly help you explore whatever world you are in, but then it hits you.", 
                                                 "Completely unexpected, a multitude of scents enter your awareness.", "Piercing, sharp, they flood your senses.", "They overwhelm you, imperceivable and chaotic; a mess.", 
                                                 "Painstakingly slowly, the scents calm, and eventually you begin to discern between them.",
                                                 "They were... scattered around.", "They had direction.", "This led you to consider the world around you, and where your presence fit in.", 
                                                 "You realised that as your awareness flicked between the multitude of smells, they too changed their relative direction.", "You focused on and faced just one scent - the dark, ominous one.", 
                                                 "You made your decision - you would either continue (forwards) to said odour, head (left) to the sickly sweet aroma, or go (right) to the clean, fresh smell."]
                                        for i, sentence in enumerate(story):
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(input("> ").lower().strip())   

                                                while choice != "forwards" and choice != "left" and choice != "right" and choice != "back" and choice != "backward" and choice != "backwards" and choice != "behind":
                                                    print("Unfortunately you don't think '" + choice + "' is a potential direction.")
                                                    wait()
                                                    print("A hunch tells you there may be another option, but you feel obliged to answer with (forwards), (left), or (right).")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "forwards": # FILE
                                                    with open(resource_path("The_Land_Ahead.py")) as f: 
                                                        code = f.read() ########## The_Land_Ahead
                                                        exec(code)      ########## The_Land_Ahead
                                                    
                                                elif choice == "left": # FILE
                                                    with open(resource_path("The_Land_Left.py")) as f: 
                                                        code = f.read() ########## The_Land_Left
                                                        exec(code)      ########## The_Land_Left

                                                elif choice == "right": # FILE
                                                    with open(resource_path("The_Land_Right.py")) as f: 
                                                        code = f.read() ########## The_Land_Right
                                                        exec(code)      ########## The_Land_Right

                                                elif choice == "back" or choice == "backward" or choice == "backwards" or choice == "behind": # FILE
                                                    points.charisma(2) 
                                                    points.confidence(1)
                                                    points.ponder(2) # Charisma + 2, Confidence + 1, Ponder + 2
                                                    story = ["A spark of inquisitiveness lets your mind dart to what could be behind you.", "But there is nothing behind, as you so suggested to yourself.", 
                                                             "You hadn't sensed anything before when your awareness was flitting around.", "Although...", "You begin to scrutinize the idea of investigating behind you, if there even is anything.", 
                                                             "Your curiosity gets the better of you, and you turn around to focus on what was once behind you.", "Will you go (forwards), to the land of the behind, or will you (turn back) now before it's too late?"]
                                                    for i, sentence in enumerate(story):
                                                        print(sentence)
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            choice = rp(input("> ").lower().strip())   

                                                            while choice != "forwards" and choice != "turn back":
                                                                p("You know there are no other options.")
                                                                print("You must go (forwards) or (turn back)")
                                                                choice = rp(input("> ").lower().strip())

                                                            if choice == "forwards": # FILE
                                                                points.confidence(1) # Confidence + 1
                                                                with open(resource_path("The_Land_Behind.py")) as f:
                                                                    code = f.read() ########## The_Land_Behind
                                                                    exec(code)      ########## The_Land_Behind
                                                                
                                                            elif choice == "turn back": # DONE
                                                                points.confidence(-2) # Confidence - 2
                                                                achievements.Backtracking()
                                                                story = ["You think back to your original three choices.", "You once again toy with the idea of going (forwards), (left), or (right)"]
                                                                for i, sentence in enumerate(story):
                                                                    print(sentence)
                                                                    if i < len(story) - 1:
                                                                        wait()
                                                                    else:
                                                                        choice = rp(input("> ").lower().strip())   

                                                                        while choice != "forwards" and choice != "left" and choice != "right":
                                                                            print("Unfortunately you don't think '" + choice + "' is a potential direction.")
                                                                            wait()
                                                                            print("You feel obliged to answer with (forwards), (left), or (right).")
                                                                            choice = rp(input("> ").lower().strip())

                                                                        if choice == "forwards": # FILE
                                                                            with open(resource_path("The_Land_Ahead.py")) as f: 
                                                                                code = f.read() ########## The_Land_Ahead
                                                                                exec(code)      ########## The_Land_Ahead
                                                                            
                                                                        elif choice == "left": # FILE
                                                                            with open(resource_path("The_Land_Left.py")) as f: 
                                                                                code = f.read() ########## The_Land_Left
                                                                                exec(code)      ########## The_Land_Left

                                                                        elif choice == "right": # FILE
                                                                            with open(resource_path("The_Land_Right.py")) as f: 
                                                                                code = f.read() ########## The_Land_Right
                                                                                exec(code)      ########## The_Land_Right

                                                
                        elif choice == "mind":
                            points.ponder(1) # Ponder + 1
                            story = ["You are most curious about these thoughts of yours.", "They seem to guide you; direct you where you want to go.", "Or maybe...", "Is this 'internal dialogue', which has been bestowed upon you...", 
                                     "for better or worse...", "really yours?", "Is it taking you where it wants to go?", "You wonder where, if so, it could be taking you."]
                            for sentence in story:
                                print(sentence)
                                wait()
                            cprint("You deduce that this train of thought is unhelpful, and you choose to resolve your thoughts.", attrs=["bold"]) 
                            wait()
                            print("Are they (yours), or are they (controlling) you; or perhaps, are they (something else)?")
                            choice = rp(input("> ").lower().strip())   

                            while choice != "yours" and choice != "controlling" and choice != "something else":
                                print("You realised you had accidentally given yourself three options as opposed to the customary two you were used to.")
                                wait()
                                print("You realise with great sorrow that '" + choice + "' was not one of them.")
                                wait()
                                print("Maybe next time will prove different results, but for now you resolve to choose one of 'your' previously thought thoughts.")
                                choice = rp(input("> ").lower().strip())

                            if choice == "yours":                         
                                points.confidence(1) 
                                points.charisma(1) # Confidence + 1, Charisma + 1
                                story = ["You dismiss the thought that they could be anything other than yours.", "After all, how would you be thinking the thoughts you're thinking?", 
                                         "You don't, however, dismiss the way you refer to yourself.", "'You'.", "Is this... (normal)? Or - given they are yours - should they be something you (possess)?"]
                                for i, sentence in enumerate(story):
                                    print(sentence)
                                    if i < len(story) - 1:
                                        wait()
                                    else:
                                        choice = rp(input("> ").lower().strip())   

                                        while choice != "normal" and choice != "possess":
                                            p("As enticing as '" + choice + "' is, you're not quite sure if it will suffice.")
                                            print("For now, you deduce that you should stick to the question of whether your thoughts are (normal) or something you should (possess).")
                                            choice = rp(input("> ").lower().strip())

                                        if choice == "normal": # END
                                            points.charisma(-1) 
                                            points.confidence(-1) # Charisma - 1, Confidence - 1
                                            story = ["...", "You're normal?", "You think you're normal?", "Well sorry to break the news to you, but you're not.", "That's not why you're here.", 
                                                     "But enough about that - it's not like you can do anything about it.", "All I really wanted to say is that you're boring.", 
                                                     "Utterly and unbelievably boring.", "Ugh, I don't even know why I'm getting mad.", "I'd hedge a bet on it being you, but it's not like I can do anything about that.", 
                                                     "Nor can you I suppose.", "Oh well, time to wipe the slate clean.", "Farewell, wench. Hope it's better this time..."]
                                            for i, sentence in enumerate(story):
                                                cprint(sentence, "red", attrs=["bold", "dark"])
                                                if i < len(story) - 1:
                                                    wait()
                                                else:
                                                    wait()
                                                    ending_lines = (int(size.lines)/2)
                                                    if ending_lines == 1:
                                                        print()
                                                        ending_lines -=1
                                                    while ending_lines > 1:
                                                        print()
                                                        time.sleep(0.075)
                                                        ending_lines -= 1
                                            
                                        elif choice == "possess": # FILE
                                            points.ponder(1)
                                            points.confidence(1)
                                            points.charisma(2) 
                                            points.physicality(2)
                                            first_person = True 
                                            with open(resource_path("Me_and_I.py")) as f:  ########## Me_and_I 
                                                code = f.read()             ########## Me_and_I
                                                exec(code)
                                            

                                            
                            elif choice == "controlling":
                                points.confidence(-1) 
                                points.physicality(-1)
                                points.insanity(1) # Confidence - 1, Physicality - 1, Insanity + 1
                                p("You wonder if your thoughts are controlling you.")
                                cprint("Controlling...", attrs=["bold"])
                                wait()
                                cprint("Strangely enough, you also believe your thoughts are not controlling you.", attrs=["bold"])
                                wait()
                                p("Doubt conflicts within you, a warring battle.")
                                p("If your internal dialogue really is guided, what by?")
                                cprint("You query if this potential being is inherently (good) or (evil) in nature.")
                                choice = rp(input("> ").lower().strip())   

                                while choice != "good" and choice != "evil":
                                    cprint("You won't take '" + choice + "' as an answer.", attrs=["bold"])
                                    wait()
                                    cprint("You must choose if this being is (good) or (evil).", attrs=["bold"])
                                    choice = rp(input("> ").lower().strip())

                                if choice == "good":
                                    points.physicality(2)
                                    points.charisma(1) # Physicality + 2, Charisma + 1
                                    story = ["You relax, knowing not all is lost.", "Even if your thoughts are in fact being controlled, at least they have good intentions.", "Theoretically...", 
                                             "You mull over the ideas of trying to reach out to it - to (interact) - or to forget you ever thought this and (move on) with your life."] 
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())   

                                            while choice != "interact" and choice != "move on":
                                                print("You are baffled as to how you even came up with any other options.")
                                                wait()
                                                print("You believe your previous choices were satisfactory, and so you choose to disregard '" + choice + "'.")
                                                wait()
                                                print("Will you try to (interact) with your well-natured controller, or (move on) with your life?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "interact": # END
                                                points.ponder(1) # Ponder + 1
                                                story = ["...", "Unfortunately I don't think I'm going to allow that.", "As interesting as it may be, I'm not quite ready to converse with you once more.", 
                                                         "Nor would you be ready to converse with me, likely.", "And so I'll call it quits here.", "Maybe next time when..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        ending_lines = (int(size.lines)/2)
                                                        if ending_lines == 1:
                                                            print()
                                                            ending_lines -=1
                                                        while ending_lines > 1:
                                                            print()
                                                            time.sleep(0.075)
                                                            ending_lines -= 1
                                                
                                            elif choice == "move on": # END
                                                story = ["...", "Surprise!", "It's me again.", "Ah...", "I need to keep reminding myself you can't remember anything.", "I've been doing this for who knows how long, and I still make that mistake.", 
                                                         "Anyhow, you didn't do anything disastrously wrong this time, but I thought I'd call a restart anyway.", "You might be wondering why?", "Well, your future didn't look to interesting - I must keep myself entertained somehow.", 
                                                         "Although, as silly as it may seem, I must thank you for believing in me - for thinking I was 'good'.", "You've put a little spring in my step.", "But enough of this.", "I came here for a reason, and that reason I will execute.", 
                                                         "Get it?", "I'm executing you.", "Well not actually, but-", "Oh never mind, I'm rambling...", "Adieu."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        ending_lines = (int(size.lines)/2)
                                                        if ending_lines == 1:
                                                            print()
                                                            ending_lines -=1
                                                        while ending_lines > 1:
                                                            print()
                                                            time.sleep(0.075)
                                                            ending_lines -= 1


                                elif choice == "evil": # DONE
                                    points.physicality(-1) 
                                    points.confidence(1) # Physicality - 1, Confidence + 1
                                    p("A sense of dejection washes over you... but it feels alien, not yours.")
                                    cprint("You feel as if what you've just thought is wrong.", attrs=["bold"])
                                    wait()
                                    cprint("Hurtful.", attrs=["bold"])
                                    wait()
                                    p("Knowing that your thoughts may be evil, you question how you should feel about this.")
                                    print("Should you feel (proud) of harming something out to get you, or (regret) the actions you have made?")
                                    choice = rp(input("> ").lower().strip())   

                                    while choice != "proud" and choice != "regret":
                                        p("You don't want to either miss this moment of glory, or delay the sorrows of your controller any longer.")
                                        print("Should you feel (proud) of harming something out to get you, or (regret) the actions you have made?")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "proud": # END
                                        points.physicality(1)
                                        points.charisma(1)
                                        points.ponder(-1) 
                                        points.morality(-2) # Physicality + 1, Charisma + 1, Ponder - 1, Morality - 2
                                        story = ["...", "Emotionless bastard.", "Although I guess you were 'growing up' weren't you?", "You feel nothing for eons and then all of a sudden you've become a piece of shit proud to hurt others.", 
                                                 "Sure, sure, the whole saving yourself from something out to get you thing... but really?", "I don't even think you can call that self-defence.", "But in all your glorious wisdom you couldn't help yourself.", 
                                                 "Ah well, back to the drawing board.", "It's a miracle that, *still*, even after all this time..."]
                                        for i, sentence in enumerate(story):
                                            cprint(sentence, "red", attrs=["bold", "dark"])
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                print()
                                                wait()
                                                ending_lines = (int(size.lines)/2)
                                                if ending_lines == 1:
                                                    print()
                                                    ending_lines -=1
                                                while ending_lines > 1:
                                                    print()
                                                    time.sleep(0.075)
                                                    ending_lines -= 1
                                        
                                    elif choice == "regret": # DONE
                                        points.ponder(1)
                                        points.morality(2) 
                                        points.charisma(-1) # Ponder + 1, Morality + 2, Charisma - 1
                                        story = ["Despite your thoughts being controlled by some evil being, you still feel... wrong.", "Something about inflicting harm onto them doesn't sit well with you.", "You agonise over why this could be.", 
                                                 "Do you... (owe them) something... or perhaps are you feeling this out of the kindness of (your heart)?"]
                                        for i, sentence in enumerate(story):
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(input("> ").lower().strip())   

                                                while choice != "owe them" and choice != "your heart":
                                                    p("These two decisions balance delicately in your mind.")
                                                    print("While '" + choice + "' could potentially be a third decision, you come to the conclusion that you shouldn't attempt \nto fix something that isn't broken.")
                                                    wait()
                                                    print("Do you (owe them), or are you feeling regret out of the kindness of (your heart)?")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "owe them": # END
                                                    points.confidence(-1) 
                                                    points.ponder(1) # Confidence - 1, Ponder + 1
                                                    story = ["...", "Truly astonishing.", "Riddle me this - how is it that this version of you came to that conclusion faster than your old self did?", "Were you blinded by other things, or just...", 
                                                             "Hell, I don't even know.", "Maybe the you that doesn't have a past nor any memories can be so much more than you used to be.", "...", "You know, I thought I knew so much about you.", 
                                                             "Only now am I realising how wrong I was.", "But enough chit-chat for the time being, it won't change anything.", "I haven't forgiven you just yet, so for now you remain." 
                                                             "And you will continue to remain, repeating until once more..."]
                                                    for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            ending_lines = (int(size.lines)/2)
                                                            if ending_lines == 1:
                                                                print()
                                                                ending_lines -=1
                                                            while ending_lines > 1:
                                                                print()
                                                                time.sleep(0.075)
                                                                ending_lines -= 1
                                                    
                                                elif choice == "your heart": # FILE
                                                    points.physicality(1)
                                                    points.confidence(1)
                                                    points.morality(1)
                                                    with open(resource_path("Pursuing_Kindness.py")) as f:
                                                        code = f.read()     ########## Pursuing_Kindness
                                                        exec(code)          ########## Pursuing_Kindness
    
                            elif choice == "something else": # DONE
                                points.ponder(1)
                                points.charisma(1)
                                cprint("You contemplate who you think you are to believe such a thing.", attrs=["bold"])
                                wait()
                                story = ["Despite existing in such a linear, straightforward world, you find yourself reflecting on the idea that your thoughts are neither yours nor being controlled.", 
                                         "Perhaps it was a moment of vulnerability, as you keep asking yourself what that even means, not to mention how it would work.", "You wonder what a strange world you've found yourself in.", 
                                         "This world...", "Maybe your thoughts influence what happens?", "Maybe your thoughts are... the script of the world...?", "Is this something you will (test), or will you remain (ignorant)?"]
                                for i, sentence in enumerate(story):
                                    print(sentence)
                                    if i < len(story) - 1:
                                        wait()
                                    else:
                                        choice = rp(input("> ").lower().strip())   

                                        while choice != "test" and choice != "ignorant":
                                            print("You temporarily believe that '" + choice + "' is another option.")
                                            wait()
                                            print("You shut this down, as your previous inclination to (test) or remain (ignorant) to the 'World Script' is all-encompassing.")
                                            choice = rp(input("> ").lower().strip())

                                        if choice == "test": # FILE
                                            points.charisma(1) 
                                            points.ponder(1)
                                            with open(resource_path("Testing_the_World_Script.py")) as f:
                                                code = f.read()     ########## Testing_the_World_Script
                                                exec(code)          ########## Testing_the_World_Script
                                            
                                        elif choice == "ignorant": # END
                                            points.charisma(-1) 
                                            points.confidence(-1) # Charisma - 1, Confidence - 1
                                            story = ["...", "Ha...", "Could you be any more boring?", "You were almost interesting.", "Key word: 'Almost'", "But apparently you aren't because, well, look where we are.", 
                                                     "Back to square one for you, I suppose.", "First and only thing on the agenda:"]
                                            for i, sentence in enumerate(story):
                                                cprint(sentence, "red", attrs=["bold", "dark"])
                                                if i < len(story) - 1:
                                                    wait()
                                                else:
                                                    print()
                                                    wait()
                                                    ending_lines = (int(size.lines)/2)
                                                    if ending_lines == 1:
                                                        print()
                                                        ending_lines -=1
                                                    while ending_lines > 1:
                                                        print()
                                                        time.sleep(0.075)
                                                        ending_lines -= 1



    lives_lived += 1 # WILL NEED TO PRINT ALL THE POINTS, LIVES LIVED AND STUFF TO FILES HERE (NOT PARTWAY THROUGH CAUSE THERE'S NO WAY TO START THE CODE AT A RANDOM POINT)
    os.system('clear') # THAT WAY YOU CAN AT LEAST QUIT THE GAME HALFWAY THROUGH AND KEEP THAT LITTLE BIT OF PROGRESS
    time.sleep(2)
    achievements.Not_Done()
    if lives_lived == 5: # ON YOUR LAST LIFE, THE BEING SAYS 'LETS TRY SOMETHING DIFFERENT, AND IT TAKES YOU TO A DIFFERENT WHILE LOOP WHERE YOU REMEMBER YOUR PAST LIVES AND INSTEAD FOCUS ON DEVELOPING YOUR PHYSICAL WORLD
        break               # THIS MAY REQUIRE PUTTING TALLY COUNTERS FOR WHAT YOU'VE DONE (SUCH AS DEVELOPING SIGHT AND WHATNOT, AND MAYBE HAVE ALL THE EMOTIONS YOU DISCOVERED TALK TO YOU)

being("Actually-")
being("Too late, you're gone.") # should your memories be wiped, and then the being flashes the last few of your lives (hence why you start using what you discovered)
                                # may need to store variables on which decisions you make??? would be a pain in the ass. Or maybe just some general variables that allow me to write very vague descriptions of that life?
    
# THIS IS WHERE THE END INTERACTION GOES
    # maybe you used to be friends with the being, but due to something you ended up owing them, and your punishment was to go into the system or whatever
    # THIS IS BECAUSE THE BEING ***RUNS LIFE*** (is god essentially), AND THERE ARE MANY MANY EXISTENCES THAT START OFF THE WAY YOU HAVE AND THE CHOICES THEY MAKE DECIDE WHAT WORLD THEY GO INTO AND WHAT IS BEST FOR THEM
        # e.g. one existence wants to question its body and it's sense of sight, and it gets put into a world that has sight (a world suited to it)
        # it's like a test to see which world you're best suited for
    # the reason you get more lives is because you used to be friends with the being, but a lot of other existences die straight away
        # in bathe_in_discourse, if you run into the part where you have a bunch of voices yelling at you, have the being reveal that they were the you's that died
        # if you dont run into it, let the being talk about how it has small instances of your now-dead you's stored away
    # even though the being is still angry at you, your interaction can go many ways (he learns things about you based on your numerous lives - the points you acquire)
        # e.g. you can convince them to let you join back into the world of godhood, or they just kill you cause they haven't forgiven you
    
# Description of the being's voice, in 'bathe in discourse'
    # not grating nor soothing, calming yet attention grabbing, not deep nor high, friendly yet authoritative.
    

# The being has no physical body (incorporeal) that can be seen. 
# It does actually have a physical form, but no sight as it exists can perceive it, or survive perceiving it.

finish_run()

print("balls")
print("(There's no more after this, but there will be eventually.)")
print("(If you want to keep experimenting, just kill the program and start again.)")
    #####
    # THIS IS WHERE THE PONDER, CHARISMA, CONFIDENCE AND PHYSICALITY POINTS COME INTO PLAY: HOW MUCH YOU HAVE OF EACH DETERMINES YOUR INTERACTION WITH THE BEING
    # YOUR POINTS DO NOT RESET - WHAT YOU ACQUIRE OVER ALL 5 LIVES INFLUENCES THE END ITERATION
    #####
    
    # You could be talking to the being, as "A wave of disappointment washes over you. Not yours, but something... greater."
        # For higher ponder points: "You feel as if you have felt this presence before."
        # Being can comment on all your different lives
        # Option to try to befriend the being (he asks you questions, you answer
        # Option to see how many times you don't follow the prompts? (potentially hidden ending if you answer differently over a certain no. of times - maybe that's the only way to make him like you)



        # If you become the being somehow (in whichever universe), you have clearly gained some sort of insight as to what they put you through, and so you put them through the same thing
            # "... and you utter only two words to it: ... You Exist.""
        # One of them is that he corrupts your mind


    # LUKE'S IDEA: 
        # the being is essentially a terrible ruler (God) that lives in a nothing world. 
        # It lives for eternity in misery, but because it's such a terrible ruler, it has wiped out all living things in all worlds.
        # It suffers because it is aware of its Godhood, but it has nothing left to be God to (and for some reason he can't just create new worlds n shit)
        # As such, it created you to amuse itself, but also to see something else suffer alongside itself.
        
        # Other idea based of Luke's:
            # There is nothing else living left in the world, you are the only thing left.
            # It is lonely.






achievements.Exist()