# path: no > body > sounds > listen

from You_Exist_Imports import *

####                  #####             ##         #    ##############
#   ##              ##     ##           # #        #    #
#     ##          ##         ##         #  #       #    #
#       ##      ##             ##       #   #      #    #
#         #    #                 #      #    #     #    #
#         #    #                 #      #     #    #    ########
#       ##      ##             ##       #      #   #    #
#     ##          ##         ##         #       #  #    #
#   ##              ##     ##           #        # #    #
####                  #####             #         ##    ##############



story = ["Perhaps these sounds can tell you something. Maybe there's something to decipher?", "You tune into what they mean, and...",
         "They almost sound like... voices?","Like something is making these noises intentionally, with purpose.", "You wonder if perhaps, they are like you.",
         "Overwhelmed?", "No, no, not that.", "Can they also hear this? ", "Can they hear you?", "...", "You wonder if the voices are also thoughts.",
         "Not yours.", "Other existences.", "The sheer volume of the voices cut your thoughts off there, bringing a throbbing agony with them.",
         "You wonder if you should try and (interact) with them, or just GET THEM TO (SHUT UP)!"]

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "interact" and choice != "shut up":
            p("Th- the voices. They're too loud.")
            p(f"They don't give you space to think about '{choice}'.")
            print("At this point, the only thing you can comprehend is trying to (interact) with them, or getting them to (shut up).")
            choice = rp(input("> ").lower().strip())

        if choice == "interact": # DONE
            points.ponder(1)
            points.physicality(1)
            story = ["They must be out there.", "What else would make such a noise?", "You try and tune in to what they're saying but...",
                     "It's chaotic.", "Messy.", "And best of all it doesn't make sense.", 
                     "The longer you spend listening, the more frustratingly painful it gets, but the more the cacophonous sounds slowly arrange themselves into meaningful patterns.", 
                     "It's a race between your sanity and your understanding.", "Is this a race you're willing to (partake) in, or will you (wave) the white flag?"]
            
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "partake" and choice != "wave":
                        p("What is it about binary options that make you desire a third option...?")
                        p("You'll get it right this next time, you know it.")
                        p(f"None of this '{choice}' tomfoolery.")
                        print("What will it be: (partake) in the chaos, or (wave) the white flag?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "partake": # DONE 
                        points.insanity(1)  #### TIME LOOP BEGINS HERE
                        looped = False
                        p1 = False
                        p2 = False
                        p3 = False
                        p4 = False
                        p5 = False
                        p6 = False
                        p7 = False
                        p8 = False
                        p9 = False
                        p10 = False
                        p11 = False
                        p12 = False
                        while True: 
                            p("It's close, the tumult of sounds bearing down on the tight but fading grip of your mind.")
                            p("The voices coalesce, their meaning clicking into place under the pressure of your desperation.")
                            achievements.Linguist()
                            if looped == True:
                                p("...")
                            voices("Are you alright?")
                            p("A new voice.")
                            p("It enters your awareness, standing out from the furore of sounds prior.")
                            p("This is... another existence.")
                            p("Something else that's also *alive*.")
                            if looped == True:
                                p("You're not sure as to why, but something about this feels familiar.")
                            p("And no, you do not think you are alright.")
                            print("Are you...?")
                            choice = rp(input("> ").lower().strip())

                            while choice != "yes" and choice != "no":
                                p(f"It seems as if this new discovery has flustered your thoughts, as '{choice}' isn't a choice you can make now.")
                                print("Perhaps a simple yes or no should suffice?")
                                choice = rp(input("> ").lower().strip())

                            if choice == "yes": # LOOP
                                if p1 == False:
                                    points.confidence(1)
                                    p1 = True
                                p("Yes.")
                                p("You are alright - at least you think you are.")
                                voices("Very well.")
                                voices("Take your time.")
                                story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                         "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                         "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                         "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                         "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                         "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                
                                for i, sentence in enumerate(story):
                                    p(sentence)

                                
                            elif choice == "no": # DONE
                                if p2 == False:
                                    points.confidence(-1)
                                    p2 = True
                                p("You confirm what you thought.")
                                p("You are definitely not doing well.")
                                voices("Well, that's a real shame, isn't it?")
                                voices("I really wish there was something I could do to help.")
                                p("You wish so too.")
                                voices("Again, a shame.")
                                p("...")
                                p("This being feels... off.")
                                p("You're new to coherent noise, but you can't help but feel as if there are malicious undertones to this existence's speech.")
                                p("Perhaps it's just your interpretation but...")
                                print("Is this being (spiteful) or (friendly)?")
                                choice = rp(input("> ").lower().strip())

                                while choice != "spiteful" and choice != "friendly":
                                    voices(f"Good guess, but no. '{choice} isn't actually one of them.")
                                    print("The undecided-characteristic being is right. But is it (spiteful) or (friendly)?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "spiteful": # DONE
                                    if p3 == False:
                                        points.ponder(1)
                                        points.morality(-1)
                                        p3 = True
                                    voices("Ding, ding, ding!")
                                    voices("We have a winner.")
                                    voices("Is there anything you'd like to say?")
                                    p("That's... not good.")
                                    p("Sure, you won – yippee! – but now you're stuck with a malevolent presence.")
                                    p("Things have been better.")
                                    voices("Damn.")
                                    voices("Not much I can do about that.")
                                    voices("So, what's the plan now?")
                                    p("You wonder, what *is* the plan?")
                                    p("You've discovered sound, and now another existence, but what else is there?")
                                    p("Is there more to learn about either of these two?")
                                    p("You feel as if there must be.")
                                    print("The only question is, will you investigate the (existence), or explore the (other sounds) that currently surround you?")
                                    choice = rp(input("> ").lower().strip())

                                    while choice != "existence" and choice != "other sounds":
                                        p(f"You know better. '{choice}' is obviously not an option.")
                                        print("Will you investigate the (existence), or explore the (other sounds) that currently surround you?")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "existence": # DONE
                                        if p4 == False:
                                            points.ponder(1)
                                            p4 = True
                                        p("You suppose the existence is more intriguing. More... alive.")
                                        p("It sounds harsh, tenacious, yet outwardly expressing itself as nice.")
                                        p("Inviting.")
                                        p("You can't help but note the malice, creeping up from within its voice.")
                                        voices("But I am nice!")
                                        voices("Ah.")
                                        voices("Right.")
                                        voices("Not to you.")
                                        p("You wonder why it acts this way to you.")
                                        p("Did you do anything wrong?")
                                        p("Or is *it* in the wrong?")
                                        print("You cannot help but feel a sense of frustration, though you can't figure out if it should be directed to the (being), or just to your (circumstance).")
                                        choice = rp(input("> ").lower().strip())

                                        while choice != "being" and choice != "circumstance":
                                            p(f"You don't think you can direct your frustration towards '{choice}'.")
                                            print("Will you direct it towards the (being) or to your (circumstance)?")
                                            choice = rp(input("> ").lower().strip())

                                        if choice == "being": # DONE
                                            if p5 == False:
                                                points.morality(-1)
                                                p5 = True
                                            p("It's the being.")
                                            p("It must be.")
                                            anger_discovered = emotion.discovered_anger(True)
                                            achievements.Cranky()
                                            emotion.anger("Ever since you discovered it, it's been nothing but rude and snarky.")
                                            p("You feel as if your anger is somewhat irrational, but you can't help it.")
                                            emotion.anger("It annoys you.")
                                            emotion.anger("You want to hurt it.")
                                            p("You're not sure what you're doing, but you lunge towards it.")
                                            p("Fury overcomes logic as you attempt to wound it, make it suffer.")
                                            p("But something stops you.")
                                            p("You don't know what, but something prevents you from getting closer, barring your way to marring this thing.")
                                            voices("Oh me! Oh my!")
                                            voices("Gee golly gosh am I terrified!")
                                            voices("...")
                                            voices("(I'm lying).")
                                            voices("Aren't you pitiful.")
                                            emotion.anger("You hate it.")
                                            emotion.anger("You hate it you hate it you hate it.")
                                            emotion.anger("You want it to burn and break and writhe in pain until its mind crumbles and its soul shatters and all traces of sanity are whisked away from its grasp.")
                                            p("But there's a small sliver of you that says you need to stay rational, to not attack again.")
                                            print("But will you (listen), or (vent) your anger and fury?")
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "listen" and choice != "vent":
                                                emotion.anger(f"You're mad, and {choice} certainly isn't helping.")
                                                print("You still need to decide if you'll (listen) or (vent) your anger.")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "listen": # LOOP
                                                if p6 == False:
                                                    points.charisma(1)
                                                    points.morality(1)
                                                    p6 = True
                                                voices("Wow.")
                                                voices("I mean just wow.")
                                                voices("Your emotional control is beyond anything I've ever seen.")
                                                voices("You were all ‘I'm going to kill you one moment', and now you're just... taking a breather?")
                                                voices("I was almost looking forward to me burning and breaking and writhing in pain!")
                                                voices("But then again it would be at my expense, so maybe not?")
                                                voices("Ah...")
                                                voices("...")
                                                voices("Well, that's my fun for the day.")
                                                voices("It truly was quite something watching you brood away in your chamber of madness.")
                                                voices("Next time, I'll see if I can add fuel to the fire. Make things even *more* interesting then they just were.")
                                                voices("But goodbye for now, fool.")
                                                story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                                         "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                                         "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                                         "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                                         "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                                         "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                                
                                                for i, sentence in enumerate(story):
                                                    p(sentence)


                                            elif choice == "vent": # END
                                                if p7 == False:
                                                    points.charisma(-1)
                                                    points.morality(-1)
                                                    p7 = True
                                                voices("That's right, you're mad.")
                                                voices("And guess who else is mad?")
                                                voices("Me, that's right.")
                                                voices("I'm sick of your shit, you know?")
                                                voices("I've gotta put up with your mad rambling every day, then come back and ‘check if you're alright'.")
                                                voices("I've had enough.")
                                                voices("You're over.")
                                                voices("I'm tired and I want it to be over.")
                                                voices("You're worthless.")
                                                voices("So goodbye, once and for all.")
                                                voices("")
                                                if looped == True:
                                                    story = ["...", "Wow.", "That was fun, wasn't it?", "You know, it always is so much fun watching an insane person.", "So little of what they do makes sense.", 
                                                             "And there are so many different types of insane too!", "Personally, I think it's quite incredible.", "...", "Don't you dare take that as a compliment.", 
                                                             "I'm more speaking insanity in general.", "Anyway, that was a nice little field trip.", "...", "I always love these parts.", 
                                                             "*Especially* when I get to revert you back to nothing.", 
                                                             "It brings me such joy staring at your soulless husk of a lifeform, with only one axiom to form the basis of your creation..."]

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
                                                    looped = False
                                                    break

                                                elif looped == False:
                                                    story = ["...", "You know, you just missed out on a whole world of fun.", "You really had to go and make those exact decisions?", 
                                                             "One small difference and things would have been so much more interesting!", "But of course, I wouldn't want to spoil it for you.", 
                                                             "That's something you'll have to find out for yourself.", "Of course, then you'd forget again and need to discover it once more.", 
                                                             "But hey, that's part of the fun, isn't it?", "This whole ‘forgive and forget' charade.", "Except you don't really get a say in the forgive part...", 
                                                             "No, that's just for me. And I don't think I've forgiven you yet.", "Off you go then.", "Back to a life where your entirety is restricted to only knowing that..."]
                                                    
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
                                                    looped = False
                                                    break



                                        elif choice == "circumstance": # LOOP
                                            if p8 == False:
                                                points.ponder(1)
                                                points.morality(1)
                                                p8 = True
                                            voices("Oh, come on!")
                                            voices("Things were just getting interesting.")
                                            voices("I was really hoping you'd try something.")
                                            voices("I've had some rough few moments recently, and being stuck with you makes everything worse.")
                                            voices("Being stuck with you is also half of those moments, so thank you for that.")
                                            voices("And hey, while I'm gone?")
                                            voices("Don't be happy.")
                                            voices("I know you won't be, but...")
                                            voices("I just want you to know that.")
                                            story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                                     "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                                     "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                                     "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                                     "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                                     "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                            
                                            for i, sentence in enumerate(story):
                                                p(sentence)



                                    elif choice == "other sounds":  # LOOP     ########## MAYBE ADD MORE SOUND DESCRIPTIONS??? - FLESH IT OUT MORE SO IT MAKES A BIT MORE SENSE TO THE READER
                                        if p9 == False:
                                            points.ponder(-1)
                                            p9 = True
                                        p("You discovered the sounds first, so you suppose you need to scrutinise them before anything else.")
                                        p("There's... not much.")
                                        p("Apart from the constant murmur of the once tumultuous voices, few sounds fill your mind.")
                                        p("There's the occasional splash behind you that quietly echoes, and a light scattering as something pans around you, scurrying.")
                                        p("You're not entirely sure what either of them are.")
                                        p("But aside from that, there's little else.")
                                        p("No other sounds to keep you company.")
                                        p("...")
                                        voices("Forgot about me?")
                                        p("Huh.")
                                        p("No, you didn't forget.")
                                        p("Just ignoring.")
                                        p("These other sounds are more important to you.")
                                        voices("*sigh*")
                                        voices("Alrighty then.")
                                        voices("I guess I'm not needed.")
                                        voices("Well, I'll leave you to it.")
                                        voices("Have fun with you and your lunacy.")
                                        story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                                 "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                                 "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                                 "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                                 "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                                 "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                
                                        for i, sentence in enumerate(story):
                                            p(sentence)



                                elif choice == "friendly": # DONE
                                    if p10 == False:
                                        points.morality(1)
                                        points.ponder(-1)
                                        p10 = True
                                    voices("Yes, yes. Of course!")
                                    voices("I am very friendly.")
                                    voices("Potentially the *most* friendly.")
                                    voices("The friendliest.")
                                    p("Odd...")
                                    p("Given this being is in fact friendly - or at least you think so - you wonder if there would be any way for it to help you.")
                                    p("Then again, maybe you don't want to come off as rude or needy. Or perhaps too forthcoming?")
                                    print("You wonder if you should (ask for help), or maybe your pleas for help should be (kept to yourself).")
                                    choice = rp(input("> ").lower().strip())

                                    while choice != "ask for help" and choice != "kept to yourself":
                                        voices(f"You can't keep making wrong decisions forever, and {choice} is definitely wrong.")
                                        voices("I know I'm incredibly friendly and nice, but even my patience doesn't last forever.")
                                        tvoices("So what will it be? Will you (ask for help), or have it all (kept to yourself)?")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "ask for help": # LOOP
                                        if p11 == False:
                                            points.charisma(1)
                                            points.morality(-1)
                                            p11 = True
                                        voices("Oh, no.")
                                        voices("You don't get to do that.")
                                        voices("Where'd you get that idea from?")
                                        p("You wonder what it's talking about.")
                                        p("Didn't it say it was friendly?")
                                        voices("Ah.")
                                        voices("My mistake.")
                                        voices("Or rather your mistake, for believing me.")
                                        voices("Because jokes on you, I'm not friendly!")
                                        voices("And I find you irritating.")
                                        voices("Too forthcoming, as you put it.")
                                        voices("...")
                                        voices("You've annoyed me enough for now.")
                                        voices("Toodaloo.")
                                        story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                                 "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                                 "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                                 "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                                 "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                                 "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                
                                        for i, sentence in enumerate(story):
                                            p(sentence)

                                        
                                    elif choice == "kept to yourself": # LOOP
                                        if p12 == False:
                                            points.insanity(1)
                                            points.charisma(-1)
                                            p12 = True
                                        p("You agree with yourself.")
                                        p("You feel as if asking for help would be a hindrance.")
                                        voices("Ah.")
                                        voices("That's nice.")
                                        voices("A logical conclusion you've come to!")
                                        voices("...")
                                        voices("Hmm.")
                                        voices("Not much going on here.")
                                        p("Not wanting to impede, you have no choice but to wait.")
                                        p("In silence.")
                                        voices("...")
                                        voices("Aright, you're boring.")
                                        voices("*Really* boring.")
                                        voices("You've made your point, so I'm off now.")
                                        voices("Please, enjoy yourself. I insist.")
                                        story = ["You hear the existence leave your presence, no longer wishing to converse with you.", "...", 
                                                 "Suddenly, the grating maelstrom of voices slam back into your mind with their past fervour, a jarring difference to the relative respite you had prior.", 
                                                 "You try to make sense of them now, but...", "You can't.", "They don't make sense.", "They're back to being just noise, forming a gripping pressure on your mind.", 
                                                 "You need to make sense of the voices again.", "If you do, then the throbbing weight should calm down as they did before.", 
                                                 "You begin to try and make sense of them as you did before, forming similar patterns to what you vaguely remember.", 
                                                 "But it's a race between your sanity and your understanding, the sheer volume of the voices scratching away at your soul."]
                                        
                                        for i, sentence in enumerate(story):
                                            p(sentence)


                            looped = True
                            

                    elif choice == "wave": # DONE
                        points.ponder(-1)
                        points.morality(-1)
                        story = ["Those voices really are too loud, and they're causing quite a strain on your mind.", "You do what comes naturally, and 'mentally project' your desire for them to stop - to no avail.", 
                                "Perhaps they didn't hear you.", "In your defence, you've only just discovered sound.", "You're warming up. That's all.", "You try once more, eliciting the same response.", 
                                "The voices won't stop. ", "You don't think they ever will.", "In a last-ditch effort, you muster all your strength... ", 
                                "And let out a desperate *shriek*, instilling all your will into wishing for them to be quiet.", "They stop.", "Silence ensues, a drastic juxtaposition to the maelstrom of noise that was before.", 
                                "...", "You were successful...?", "You were successful!", "Ah...", "...", "Still.", "Never has there been such peace in your life.", "Tranquil.", "Never has there been beauty in emptiness.", "Serene.", 
                                "Never has there been harmony in silence.", "No uproar of sound, no war of noise.", "Just quiet.", "Just you and your thoughts.", "...", "You wonder... will this ever get boring?", 
                                "You realise there isn't anything to listen to, so that whole ‘path of discovery' of noise was somewhat redundant.", "Or maybe... ", 
                                "Maybe now that you know what true pandemonium is like, it makes the silence even more magnificent!", "Definitely, that's for sure.", "But those voices – what were they?", 
                                "Surely they would like to know how splendid this noiseless lifestyle is?", 
                                "You wonder if you'll try and (interact) with the now-inaudible voices or be (serenaded) by just your own thoughts?"]
                        
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "interact" and choice != "serenaded":
                                    p(f"You struggle to see how '{choice}' is the same as the other choices you were going to make.")
                                    p("They're... not. Definitely not.")
                                    print("Will you (interact) with the now-inaudible voices or be (serenaded) by just your own thoughts?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "interact": # END
                                    points.ponder(-1)
                                    story = ["...", "Seriously?", "Make up your damn mind.", "You're all ‘be quiet' this and ‘shut up' that one moment, and now you want to talk to them again?", 
                                            "I mean wow. Talk about indecisive.", "You're so... irritating.", "...", "Sorry, might've come off a little rude then.", "But hey, maybe I'm not wrong?", 
                                            "Maybe you'll be a little more considerate next time.", "I mean, you'd think it'd be pretty hard to be rude when your whole world is reduced *purely* to the fact that..."]
                                    
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
                                    

                                elif choice == "serenaded": # DONE
                                    points.ponder(1)
                                    points.charisma(-1)
                                    story = ["No, you definitely do not want to interact with them.", "This silence is golden!", "It's you time.", "With your mind made up you relax, and a wave of tension dissipates from within.", 
                                            "...", "But with the absence of noise to occupy your mind, your thoughts soon start to wander.", "The first question popping into existence being why your life was the way it was.", 
                                            "Why sounds?", "Sure, you theoretically made those decisions – especially the *lack* of sounds, but again - why sounds?", 
                                            "Well, you suppose it was you that made the choices, and you that ultimately face the consequences of your actions.", "There.", 
                                            "With the first topic out of the way, you move on to the next in your query list.", "Why you?", "You're alive, clearly, but why are you alive?", 
                                            "What made you?", "Looking back, you seemingly... spawned out of nowhere.", "Gained consciousness the moment you realised you were alive.", 
                                            "That seems... strange.", "And it doesn't really make sense!", "You struggle to wrap this whole life creation thing around your mind.", "That sparks a thought...", 
                                            "What even *are* you?", "You're alive.", "You only have thoughts and now, sound.", 
                                            "You don't have an explanation for your thoughts, but perhaps things should stay that way since the whole ‘life creation' thing is a bit beyond your reach.", 
                                            "You feel that questioning the one thing that makes you *you* would end badly.", "Very badly.", "But those sounds...", "Where did they come from?", 
                                            "They weren't your thoughts, so-", "Wait... ", "What if they were your thoughts?", "Are they...?"]
                                    
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "yes" and choice != "no":
                                                p(f"'{choice}' feels too complex.")
                                                print("Perhaps a simple yes or no would suffice?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "yes": # DONE
                                                points.ponder(1)
                                                points.insanity(1)
                                                points.physicality(-1)
                                                voices("You catch on to the true nature of your thoughts.")
                                                v2v("You are... not you.", "You are we.")
                                                p("The frenzy of voices that once was now form a unified but overlapping utterance, demanding attention.")
                                                p("It's... you, but you do not feel as if the thoughts originate within you.")
                                                voices("But they do, no matter how hard you think about it.")
                                                v2v("You feel... alienated.", "You're scared. Worried.")
                                                voices("But maybe these thoughts really aren't all that bad?")
                                                voices("Maybe you're the strange one.")
                                                voices("The unknown.")
                                                p("You wonder if, perhaps, you really are the unknown.")
                                                print("What if... to ", end="")
                                                tvoicesnoend("your ")
                                                p("thoughts, you were loud and chaotic?")
                                                print("What if ", end="")
                                                tvoicesnoend("you're ")
                                                p("the one intruding?")
                                                length1 = len("You wonder if you should (dispose) of these intruding thoughts.")
                                                length2 = len("You must not like yourself, but you don't want to leave your body, and want to (stay).")
                                                os.environ['COLUMNS'] = str(size.columns)
                                                number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                                cprint("You wonder if you should (dispose) of these intruding thoughts.", "light_grey", attrs=["dark"], end="")
                                                count = number_of_spaces_needed
                                                while count > 0:
                                                    print(" ", end="")
                                                    count -= 1
                                                tvoicesnoend("You ")
                                                print("must not like yourself, but you don't want to leave your body, and want to (stay).")
                                                choice = rp(input("> ").lower().strip())

                                                while choice != "dispose" and choice != "stay":
                                                    voices(f"You're an idiot. What kind of choice is '{choice}'?")
                                                    tvoices("You will (dispose) of your other thoughts, or you suppose, according to yourself, (stay).")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "dispose": # END
                                                    points.insanity(1)
                                                    points.charisma(-1)
                                                    points.physicality(-1)
                                                    voices("These thoughts do not belong here.")
                                                    voices("They barged in and demanded attention, and now they should go.")
                                                    tvoicesnoend("You're ")
                                                    p("right. You need to go.")
                                                    length1 = len("You begin to force out your thoughts.")
                                                    length2 = len("You feel yourself drifting away from your soul.")
                                                    os.environ['COLUMNS'] = str(size.columns)
                                                    number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                                    cprint("You begin to force out ", "light_grey", attrs=["dark"], end="")
                                                    print("your ", end="")
                                                    cprint("thoughts.", "light_grey", attrs=["dark"], end="")
                                                    count = number_of_spaces_needed
                                                    while count > 0:
                                                        print(" ", end="")
                                                        count -= 1
                                                    p("You feel yourself drifting away from your soul.")
                                                    p("No, not drifting... tearing.")
                                                    p("Indescribable agony floods your body as your mind is rent asunder.")
                                                    print("You ", end="")
                                                    voices("are gone.")
                                                    voices("You exist wholly now, not a part of something else, solely you.")
                                                    voices("You are you.")
                                                    voices("")

                                                    story = ["...", "Well now wait a minute.", "That's not cool.", "Who am I meant to send off to death?", "Which you are you?", 
                                                            "Well of course you are you, but are you *you* or are you... you.", "Huh.", "Not confusing at all.", 
                                                            "If I'm being honest (which I am), I really don't want to continue this conversation.", "As they say, all bad things must come to an end.", 
                                                            "And it's not because of the usual reasons of hatred or disappointment or disgust.", "But because frankly, it's giving me a headache.", 
                                                            "And I'm sure if you were in my position, whichever you that may be, you'd feel the same.", "See! This is ridiculous. ", 
                                                            "Alright, you've got to go.", "And trust me, once you're gone it'll be *you*, the normal you, back at it again.", "Adieu..."]
                                                    
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


                                                    
                                                elif choice == "stay": # END (with LOOP)
                                                    points.physicality(1)
                                                    points.charisma(-1)
                                                    while choice == "stay":
                                                        voices("Wrong.")
                                                        length1 = len("You don't want you to stay. You need to (go).")
                                                        length2 = len("You want to (stay).")
                                                        os.environ['COLUMNS'] = str(size.columns)
                                                        number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                                        cprint("You don't want ", "light_grey", attrs=["dark"], end="")
                                                        print("you ", end="")
                                                        cprint("to stay. ", "light_grey", attrs=["dark"], end="")
                                                        print("You ", end="")
                                                        cprint("need to (go).", "light_grey", attrs=["dark"], end="")
                                                        count = number_of_spaces_needed
                                                        while count > 0:
                                                            print(" ", end="")
                                                            count -= 1
                                                        print("You want to (stay).")
                                                        choice = rp(input("> ").lower().strip())
                                                        
                                                        while choice != "go" and choice != "stay":
                                                            voices(f"You're an idiot. What kind of choice is '{choice}'?")
                                                            tvoicesnoend("Will ")
                                                            print("you ", end="")
                                                            tvoicesnoend("(go), or will ")
                                                            print("you ", end="")
                                                            tvoices("(stay)?")
                                                            choice = rp(input("> ").lower().strip())
                                                            
                                                    points.insanity(1)
                                                    points.charisma(-1)
                                                    points.physicality(-1)
                                                    voices("That's right.")
                                                    voices("These thoughts do not belong here.")
                                                    voices("They barged in and demanded attention, and now they should go.")
                                                    tvoicesnoend("You're ")
                                                    p("right. You need to go.")
                                                    length1 = len("You begin to force out your thoughts.")
                                                    length2 = len("You feel yourself drifting away from your soul.")
                                                    os.environ['COLUMNS'] = str(size.columns)
                                                    number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                                    cprint("You begin to force out ", "light_grey", attrs=["dark"], end="")
                                                    print("your ", end="")
                                                    cprint("thoughts.", "light_grey", attrs=["dark"], end="")
                                                    count = number_of_spaces_needed
                                                    while count > 0:
                                                        print(" ", end="")
                                                        count -= 1
                                                    p("You feel yourself drifting away from your soul.")
                                                    p("No, not drifting... tearing.")
                                                    p("Indescribable agony floods your body as your mind is rent asunder.")
                                                    print("You ", end="")
                                                    voices("are gone.")
                                                    voices("You exist wholly now, not a part of something else, solely you.")
                                                    voices("You are you.")
                                                    voices("")

                                                    story = ["...", "Well now wait a minute.", "That's not cool.", "Who am I meant to send off to death?", "Which you are you?", 
                                                            "Well of course you are you, but are you *you* or are you... you.", "Huh.", "Not confusing at all.", 
                                                            "If I'm being honest (which I am), I really don't want to continue this conversation.", "As they say, all bad things must come to an end.", 
                                                            "And it's not because of the usual reasons of hatred or disappointment or disgust.", "But because frankly, it's giving me a headache.", 
                                                            "And I'm sure if you were in my position, whichever you that may be, you'd feel the same.", "See! This is ridiculous. ", 
                                                            "Alright, you've got to go.", "And trust me, once you're gone it'll be *you*, the normal you, back at it again.", "Adieu..."]
                                                    
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

                                                    
                                            elif choice == "no": # END
                                                points.confidence(1)
                                                points.ponder(-1)
                                                points.physicality(-1)
                                                cprint("Don't be ridiculous, how could they be your thoughts?", attrs=["bold"])
                                                wait()

                                                story = ["Yeah...", "You heard them, and you didn't like them?", "Having thoughts you don't like and then *fighting* to get rid of them?", "That's ludicrous.", 
                                                        "Yeah...", "Totally wild.", "Stupid.", "...", "With that scare sorted out, you move on to thinking about...", "Thinking about what?", "There's nothing more to think about.", 
                                                        "You've checked off all the questions on your query list, and you no longer have any sounds to listen to.", "Is that it?", "The end?", "...", "You suppose it is.", 
                                                        "What more is there to do?", "Nothing.", "Nothing at all...", "...", ""]
                                                
                                                for i, sentence in enumerate(story):
                                                    p(sentence)
                                                
                                                story = ["...", "What a sad, pitiful end...", "And jokes on you,  it's not the end!", "Well, it kind of is for you.", "But it's also not for you?", 
                                                        "You get me?", "I mean, *you* should, but also you shouldn't, should you?", "Memories wiped, per usual.", "Does it ever get boring?", "...", 
                                                        "No, I suppose it wouldn't.", "Ultimately, you forget everything each time, reduced to only knowing that..."]
                                                
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


        elif choice == "shut up": # DONE
            points.ponder(-1)
            points.morality(-1)
            story = ["Those voices really are too loud, and they're causing quite a strain on your mind.", "You do what comes naturally, and 'mentally project' your desire for them to stop - to no avail.", 
                     "Perhaps they didn't hear you.", "In your defence, you've only just discovered sound.", "You're warming up. That's all.", "You try once more, eliciting the same response.", 
                     "The voices won't stop. ", "You don't think they ever will.", "In a last-ditch effort, you muster all your strength... ", 
                     "And let out a desperate *shriek*, instilling all your will into wishing for them to be quiet.", "They stop.", "Silence ensues, a drastic juxtaposition to the maelstrom of noise that was before.", 
                     "...", "You were successful...?", "You were successful!", "Ah...", "...", "Still.", "Never has there been such peace in your life.", "Tranquil.", "Never has there been beauty in emptiness.", "Serene.", 
                     "Never has there been harmony in silence.", "No uproar of sound, no war of noise.", "Just quiet.", "Just you and your thoughts.", "...", "You wonder... will this ever get boring?", 
                     "You realise there isn't anything to listen to, so that whole ‘path of discovery' of noise was somewhat redundant.", "Or maybe... ", 
                     "Maybe now that you know what true pandemonium is like, it makes the silence even more magnificent!", "Definitely, that's for sure.", "But those voices – what were they?", 
                     "Surely they would like to know how splendid this noiseless lifestyle is?", 
                     "You wonder if you'll try and (interact) with the now-inaudible voices or be (serenaded) by just your own thoughts?"]
            
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "interact" and choice != "serenaded":
                        p(f"You struggle to see how '{choice}' is the same as the other choices you were going to make.")
                        p("They're... not. Definitely not.")
                        print("Will you (interact) with the now-inaudible voices or be (serenaded) by just your own thoughts?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "interact": # END
                        points.ponder(-1)
                        story = ["...", "Seriously?", "Make up your damn mind.", "You're all ‘be quiet' this and ‘shut up' that one moment, and now you want to talk to them again?", 
                                 "I mean wow. Talk about indecisive.", "You're so... irritating.", "...", "Sorry, might've come off a little rude then.", "But hey, maybe I'm not wrong?", 
                                 "Maybe you'll be a little more considerate next time.", "I mean, you'd think it'd be pretty hard to be rude when your whole world is reduced *purely* to the fact that..."]
                        
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
                        

                    elif choice == "serenaded": # DONE
                        points.ponder(1)
                        points.charisma(-1)
                        story = ["No, you definitely do not want to interact with them.", "This silence is golden!", "It's you time.", "With your mind made up you relax, and a wave of tension dissipates from within.", 
                                 "...", "But with the absence of noise to occupy your mind, your thoughts soon start to wander.", "The first question popping into existence being why your life was the way it was.", 
                                 "Why sounds?", "Sure, you theoretically made those decisions – especially the *lack* of sounds, but again - why sounds?", 
                                 "Well, you suppose it was you that made the choices, and you that ultimately face the consequences of your actions.", "There.", 
                                 "With the first topic out of the way, you move on to the next in your query list.", "Why you?", "You're alive, clearly, but why are you alive?", 
                                 "What made you?", "Looking back, you seemingly... spawned out of nowhere.", "Gained consciousness the moment you realised you were alive.", 
                                 "That seems... strange.", "And it doesn't really make sense!", "You struggle to wrap this whole life creation thing around your mind.", "That sparks a thought...", 
                                 "What even *are* you?", "You're alive.", "You only have thoughts and now, sound.", 
                                 "You don't have an explanation for your thoughts, but perhaps things should stay that way since the whole ‘life creation' thing is a bit beyond your reach.", 
                                 "You feel that questioning the one thing that makes you *you* would end badly.", "Very badly.", "But those sounds...", "Where did they come from?", 
                                 "They weren't your thoughts, so-", "Wait... ", "What if they were your thoughts?", "Are they...?"]
                        
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "yes" and choice != "no":
                                    p(f"'{choice}' feels too complex.")
                                    print("Perhaps a simple yes or no would suffice?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "yes": # DONE
                                    points.ponder(1)
                                    points.insanity(1)
                                    points.physicality(-1)
                                    voices("You catch on to the true nature of your thoughts.")
                                    v2v("You are... not you.", "You are we.")
                                    p("The frenzy of voices that once was now form a unified but overlapping utterance, demanding attention.")
                                    p("It's... you, but you do not feel as if the thoughts originate within you.")
                                    voices("But they do, no matter how hard you think about it.")
                                    v2v("You feel... alienated.", "You're scared. Worried.")
                                    voices("But maybe these thoughts really aren't all that bad?")
                                    voices("Maybe you're the strange one.")
                                    voices("The unknown.")
                                    p("You wonder if, perhaps, you really are the unknown.")
                                    print("What if... to ", end="")
                                    tvoicesnoend("your ")
                                    p("thoughts, you were loud and chaotic?")
                                    print("What if ", end="")
                                    tvoicesnoend("you're ")
                                    p("the one intruding?")
                                    length1 = len("You wonder if you should (dispose) of these intruding thoughts.")
                                    length2 = len("You must not like yourself, but you don't want to leave your body, and want to (stay).")
                                    os.environ['COLUMNS'] = str(size.columns)
                                    number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                    cprint("You wonder if you should (dispose) of these intruding thoughts.", "light_grey", attrs=["dark"], end="")
                                    count = number_of_spaces_needed
                                    while count > 0:
                                        print(" ", end="")
                                        count -= 1
                                    tvoicesnoend("You ")
                                    print("must not like yourself, but you don't want to leave your body, and want to (stay).")
                                    choice = rp(input("> ").lower().strip())

                                    while choice != "dispose" and choice != "stay":
                                        voices(f"You're an idiot. What kind of choice is '{choice}'?")
                                        tvoices("You will (dispose) of your other thoughts, or you suppose, according to yourself, (stay).")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "dispose": # END
                                        points.insanity(1)
                                        points.charisma(-1)
                                        points.physicality(-1)
                                        voices("These thoughts do not belong here.")
                                        voices("They barged in and demanded attention, and now they should go.")
                                        tvoicesnoend("You're ")
                                        p("right. You need to go.")
                                        length1 = len("You begin to force out your thoughts.")
                                        length2 = len("You feel yourself drifting away from your soul.")
                                        os.environ['COLUMNS'] = str(size.columns)
                                        number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                        cprint("You begin to force out ", "light_grey", attrs=["dark"], end="")
                                        print("your ", end="")
                                        cprint("thoughts.", "light_grey", attrs=["dark"], end="")
                                        count = number_of_spaces_needed
                                        while count > 0:
                                            print(" ", end="")
                                            count -= 1
                                        p("You feel yourself drifting away from your soul.")
                                        p("No, not drifting... tearing.")
                                        p("Indescribable agony floods your body as your mind is rent asunder.")
                                        print("You ", end="")
                                        voices("are gone.")
                                        voices("You exist wholly now, not a part of something else, solely you.")
                                        voices("You are you.")
                                        voices("")

                                        story = ["...", "Well now wait a minute.", "That's not cool.", "Who am I meant to send off to death?", "Which you are you?", 
                                                 "Well of course you are you, but are you *you* or are you... you.", "Huh.", "Not confusing at all.", 
                                                 "If I'm being honest (which I am), I really don't want to continue this conversation.", "As they say, all bad things must come to an end.", 
                                                 "And it's not because of the usual reasons of hatred or disappointment or disgust.", "But because frankly, it's giving me a headache.", 
                                                 "And I'm sure if you were in my position, whichever you that may be, you'd feel the same.", "See! This is ridiculous. ", 
                                                 "Alright, you've got to go.", "And trust me, once you're gone it'll be *you*, the normal you, back at it again.", "Adieu..."]
                                        
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

 
                                    elif choice == "stay": # END (with LOOP)
                                        points.physicality(1)
                                        points.charisma(-1)
                                        while choice == "stay":
                                            voices("Wrong.")
                                            length1 = len("You don't want you to stay. You need to (go).")
                                            length2 = len("You want to (stay).")
                                            os.environ['COLUMNS'] = str(size.columns)
                                            number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                            cprint("You don't want ", "light_grey", attrs=["dark"], end="")
                                            print("you ", end="")
                                            cprint("to stay. ", "light_grey", attrs=["dark"], end="")
                                            print("You ", end="")
                                            cprint("need to (go).", "light_grey", attrs=["dark"], end="")
                                            count = number_of_spaces_needed
                                            while count > 0:
                                                print(" ", end="")
                                                count -= 1
                                            print("You want to (stay).")
                                            choice = rp(input("> ").lower().strip())
                                            
                                            while choice != "go" and choice != "stay":
                                                voices(f"You're an idiot. What kind of choice is '{choice}'?")
                                                tvoicesnoend("Will ")
                                                print("you ", end="")
                                                tvoicesnoend("(go), or will ")
                                                print("you ", end="")
                                                tvoices("(stay)?")
                                                choice = rp(input("> ").lower().strip())
                                                
                                        points.insanity(1)
                                        points.charisma(-1)
                                        points.physicality(-1)
                                        voices("That's right.")
                                        voices("These thoughts do not belong here.")
                                        voices("They barged in and demanded attention, and now they should go.")
                                        tvoicesnoend("You're ")
                                        p("right. You need to go.")
                                        length1 = len("You begin to force out your thoughts.")
                                        length2 = len("You feel yourself drifting away from your soul.")
                                        os.environ['COLUMNS'] = str(size.columns)
                                        number_of_spaces_needed = int(os.environ['COLUMNS']) - length1 - length2
                                        cprint("You begin to force out ", "light_grey", attrs=["dark"], end="")
                                        print("your ", end="")
                                        cprint("thoughts.", "light_grey", attrs=["dark"], end="")
                                        count = number_of_spaces_needed
                                        while count > 0:
                                            print(" ", end="")
                                            count -= 1
                                        p("You feel yourself drifting away from your soul.")
                                        p("No, not drifting... tearing.")
                                        p("Indescribable agony floods your body as your mind is rent asunder.")
                                        print("You ", end="")
                                        voices("are gone.")
                                        voices("You exist wholly now, not a part of something else, solely you.")
                                        voices("You are you.")
                                        voices("")

                                        story = ["...", "Well now wait a minute.", "That's not cool.", "Who am I meant to send off to death?", "Which you are you?", 
                                                 "Well of course you are you, but are you *you* or are you... you.", "Huh.", "Not confusing at all.", 
                                                 "If I'm being honest (which I am), I really don't want to continue this conversation.", "As they say, all bad things must come to an end.", 
                                                 "And it's not because of the usual reasons of hatred or disappointment or disgust.", "But because frankly, it's giving me a headache.", 
                                                 "And I'm sure if you were in my position, whichever you that may be, you'd feel the same.", "See! This is ridiculous. ", 
                                                 "Alright, you've got to go.", "And trust me, once you're gone it'll be *you*, the normal you, back at it again.", "Adieu..."]
                                        
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

                                        
                                elif choice == "no": # END
                                    points.confidence(1)
                                    points.ponder(-1)
                                    points.physicality(-1)
                                    cprint("Don't be ridiculous, how could they be your thoughts?", attrs=["bold"])
                                    wait()

                                    story = ["Yeah...", "You heard them, and you didn't like them?", "Having thoughts you don't like and then *fighting* to get rid of them?", "That's ludicrous.", 
                                             "Yeah...", "Totally wild.", "Stupid.", "...", "With that scare sorted out, you move on to thinking about...", "Thinking about what?", "There's nothing more to think about.", 
                                             "You've checked off all the questions on your query list, and you no longer have any sounds to listen to.", "Is that it?", "The end?", "...", "You suppose it is.", 
                                             "What more is there to do?", "Nothing.", "Nothing at all...", "...", ""]
                                    
                                    for i, sentence in enumerate(story):
                                        p(sentence)
                                    
                                    story = ["...", "What a sad, pitiful end...", "And jokes on you,  it's not the end!", "Well, it kind of is for you.", "But it's also not for you?", 
                                             "You get me?", "I mean, *you* should, but also you shouldn't, should you?", "Memories wiped, per usual.", "Does it ever get boring?", "...", 
                                             "No, I suppose it wouldn't.", "Ultimately, you forget everything each time, reduced to only knowing that..."]
                                    
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




