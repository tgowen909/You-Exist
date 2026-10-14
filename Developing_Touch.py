# Path: yes > more > body > feel

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



story = ["You realise that the 'now' is more important to you, that you need to experience things as they come, not fret over what may be.", 
         "This hypothetical body of yours... what encases it?", "What holds you together, stores your existence and prevents you from slipping away?",
         "You are convinced there must be an 'outside' to your body, a skin of sorts.", "As you hone your ideas, a spark of development emerges, and you feel... new.",
         "This skin of yours appears to exist, cool surroundings gently pressing against you.", "This... you realise this must be touch, your first sensation of the outside world."]

for i, sentence in enumerate(story):
    p(sentence)
    if i == len(story) - 2:
        achievements.Touch()

story = ["Just as quickly as your excitement for this revelation appears, so too does it disappear.", 
         "In its stead is fear, fear for the sliver that crawls along your skin as it eerily brushes along, sending ripples of shivers on its touch.",
         "You haven't the slightest clue what it is or what its intentions are, yet the crawling touch against your fleshy membrane elicits a sense of unease.", 
         "Unsure of what this existence is trying to accomplish, you are torn between two possibilities.", "Is it something you should (fear) or perhaps (embrace) instead?"]
for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "fear" and choice != "embrace":
            p("The strange existence's caressing does not cease, and you doubt it will as you contemplate '" + choice + "' either.")
            print("You knuckle down on your decision: will you (fear) or (embrace) it?")
            choice = rp(input("> ").lower().strip())

        if choice == "fear": ### DONE
            points.confidence(-1)
            story = ["Shivers course through your body, a tingling sensation rippling across your skin.", "You wonder what is lurking in the dark.",
                     "Despite not knowing what it is, it still instils in you a primal sense of fear.", "Perhaps this is the 'fear of the unknown'?",
                     "The eerie caressing continues amidst your thoughts, increasing in frequency and intensity.", "You feel the situation becoming more dire.", 
                     "Do you (fight back) or (run away)?"]
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "fight back" and choice != "run away":
                        p("'" + choice + "' doesn't seem to be a viable option.")
                        print("Do you (fight back) or (run away)?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "fight back": ### DONE
                        points.confidence(1)
                        points.physicality(1)
                        story = ["You whip out instinctually, meeting resistance.", "The caressing stops for the moment, but your delivered blow sends a flash of pain up your limb... whatever it was that you hit with.",
                                 "Then all of a sudden, a crushing weight bears down on you - not physical, but mental.","An intense aura that doubles your existing fear.",
                                 "You have doubts about your chance of fighting it, but there's no chance to back out now.","A cold, blunt force collides with your skin, and you're sent flying back.",
                                 "You feel... damaged.", "Despite your weakened state, you're aware that things aren't going to get much better if you don't do anything.",
                                 "You ready yourself, poised and waiting for anything that could indicate an attack.", "And there it is, a brush of the wind.", 
                                 "Moving in ways you have never imagined possible, let along practised, you swiftly slide out of the way and feel the flicker of icy death flash past your skin.",
                                 "You whip around and lash out at where you presume the opposing existence is.", "Given your lack of experience in the fighting field, you question whether you'll (connect) your attack or (miss)."]
                        # ⁡⁢⁡⁢⁣⁢​‌‌‌(MAYBE IN THE FUTURE ADD A SMALL CHANCE FOR YOU TO WIN - RNG)​⁡
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "connect" and choice != "miss":
                                    p("It seems your idea of '" + choice + "' doesn't match the binary possibilities you gave yourself.")
                                    print("Perhaps you should just decide if you believe it will (connect) or (miss).")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "connect": ### DONE
                                    points.charisma(1)
                                    story = ["Even though you're new to it, you believe in your instincts.", "Lo and behold, you find resistance and hit it.",
                                             "But the resistance was strong and you feel the punch as it ricochets off, a throbbing pain spreading across your skin.",
                                             "Despite this, it still comforts you.","Although your attack appears to have hurt you more than it, at least you know you can hit it.",
                                             "There's a chance you can win.","You steady yourself again, ready for an incoming assault.", "Things weren't the same this time, however.",
                                             "You don't sense anything coming, yet you find yourself falling and a sharp pain piercing the lower part of your skin.",
                                             "There is no gentleness in this touch, and you almost find yourself missing the eerie brushing, no matter how terrifying.",
                                             "But you aren't given the time to ponder over things as more pain erupts behind you, your skin freezing over from the touch of this ghastly being.",
                                             "Things are not looking good for you, with pain radiating all over your body and no way to tell where the next attack will come from.",
                                             "More attacks land, hitting you where you least expect it, battering your body again and again with no end in sight.",
                                             "Occasionally you find an opportunity to lash back and connect with the fleeting being, but by no means does it appear to injure your attacker as the assault prevails.",
                                             "But you hold on, desperately wanting to survive.", "You do want to survive... don't you?"]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "yes" and choice != "no":
                                                p("Sometimes complexity only serves to make things confusing, more so than necessary.")
                                                print("You think you should just stick to the basics. Perhaps a simple yes or no will suffice?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "yes": ### END
                                                points.charisma(1)
                                                story = ["Survival is in fact your number one priority, but you don't know how possible it is.", 
                                                         "The being doesn't stop, blow after blow raining down on you as the icy cold of approaching death grows closer, permeating across your skin.",
                                                         "You tried.", "You tried, but you couldn't make it.","Against all intuition of yours, you give up.","This is the end...",""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...","Huh.","Wasn't expecting that one.","And I'm sure you weren't either!", "That whole 'fighting back' thing really backfired on you, didn't it.",
                                                         "I would call you a suicidal prick, but you still wanted to survive.","So I guess it was just bad luck, then.",
                                                         "On the bright side, you won't be moping about your misfortune soon.","On the not-so-bright side, that's because you won't remember anything.",
                                                         "Only one sentence will echo in your mind..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/yes")
                                        
                                            elif choice == "no": ### END
                                                points.confidence(-1)
                                                points.insanity(1)
                                                story = ["you don't.", "Why bother trying to survive when your attempts are futile?","If it's going to end in death, why would you drag it out and extend your suffering?",
                                                         "You let go, and accept death.",""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)
                                                
                                                story = ["...","Well, that was quite the disappointing end.","Whatever happened to all that bravado? The whole 'fighting back' thing?",
                                                         "I mean , you had so much *spirit* I was practically rooting for you.","Ha, imagine that.","*Me*, rooting for *you*.",
                                                         "Never would I think I'd see the day...","But I've gotta give it to you.","You held out for quite some time.","Most of you fail practically instantly.",
                                                         "I'm sure you've failed too, some time in the past.","Not that you'll know what the past is, but maybe one day you will.",
                                                         "Only temporarily, of course.","After all, in just a second all you'll comprehend is that..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/no")
                                                
                                elif choice == "miss": ### DONE
                                    points.confidence(-1)
                                    story = ["You've never done something like this before, so you don't hold much confidence in your abilities.", "Unexpectedly, you don't hit anything solid.",
                                             "And yet... your skin passes through *something*.","The icy cold sensation from before when you were hit spreads across your skin.",
                                             "Is this existence, the seemingly evil being out for your life, incorporeal?","Is it able to shift between solid and... not?",
                                             "These thoughts flash through your mind, urgently trying to find a solution for a seemingly impossible problem.", 
                                             "But you were distracted.","A sharp pain pierces the centre of your skin.","You fall, shudders rippling throughout you, and you feel your life seep from your grasp.",
                                             "The once deafening pain permeates, numbing you.","You're aware a life-ending attack is imminent, and that you have virtually no chances of surviving, but...",
                                             "You can't help but wonder if dodging is possible.","If your attacker can turn incorporeal, what's stopping you from doing so?",
                                             "You focus in on the ambient feeling on your skin, ignoring the epicentre of pain and looking for the last minute evidence for an incoming attack.",
                                             "With luck on your side you detect a slight disturbance, and you know this is it.","Moments before it hits you, ending your life, you attempt to phase your body out of the physical realm.",
                                             "With your life riding on this idea, you wonder if it (will) or (won't) work."]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "will" and choice != "wont":
                                                p("This is no time for jokes, and although '" + choice + "' isn't very funny, you realise it certainly isn't serious.")
                                                print("Your life depends on this decision. (Will) or (won't) it work?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "will": ### END
                                                points.physicality(-1)
                                                story = ["...", "Unfortunately, it didn't work.","You'll be glad to know I've spared you from experiencing your own death.",
                                                         "*sigh*","If only I could receive some kind of thanks for it...","Well, I'm sure it won't be the last time, and it certainly wasn't the first.",
                                                         "With all this time, and all these lives to come, I'm sure I'll find myself being compassionate again.","You on the other hand, well...",
                                                         "you won't even know what compassion is.","All you'll know is that..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/will")

                                            elif choice == "wont": ### END
                                                points.charisma(-1)
                                                points.confidence(-1)
                                                story = ["You know it was a feeble cling at survival, a desperate attempt to cope with the disaster of the end of your existence.", 
                                                         "You accept your fate, resign to what's to come, and as one last impact obliterates your skin and body your thoughts fade and turn to black...",""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...","What an astute display of realisation and self awareness.","Shame it had to end in such a pitiful way.",
                                                         "You tried, I suppose, but that's not something you can win against.","Not now, at least.","And likely not ever, unless you actually get somewhere.",
                                                         "But what would be the fun it that?","That's not why you're here.","Well, back to the drawing board for you. Time to start over.",
                                                         "And the only thing on this clean slate of yours will be..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/wont")

                    elif choice == "run away": ### DONE
                        points.ponder(1)
                        points.confidence(-1)
                        story = ["Your urge to survive outweighs any notion of pride, your only motive to get away from this ghoulish being.", 
                                 "You throw yourself in any direction in an attempt to escape, wind harshly biting against your novel skin.",
                                 "Despite your reckless movement, the sinister brushing does not stop, growing and growing until it becomes a scratch.",
                                 "It begins to rip you apart, breaking your manifested skin, scraping and tearing away at it.",
                                 "If you had the time to you would consider this pain, a physical emotion of sorts.","But you do not have the time.",
                                 "Your desperate attempts for freedom continue.","Will these attempts be (futile), or will you prove to be (successful) in your escape?"]
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "futile" and choice != "successful":
                                    p("You struggle to answer this simple good or bad, yes or no question, instead opting for '" + choice + ".'")
                                    p("You realise this won't do, and you need to revise your original response.")
                                    print("Will your attempts for freedom prove to be (futile) or (successful)?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "futile": ### END
                                    points.charisma(-1)
                                    story = ["...","Well how was that?","Your first experience of the outside world.",
                                             "Well, 'first' isn't quite right - perhaps only first for *this* you.", "Not the previous one, or the countless others before it.",
                                             "At least you know your place. How could a being with only skin as defence fight against something like that?",
                                             "Life's not easy for everyone, but I don't expect you to know that.","*This* wasn't exactly made as a comfortable, cruisy adventure.",
                                             "But hey, you can dream. Maybe your next life will end differently.","Though I doubt it, as history is bound to repeat itself.",
                                             "You'll just start over from the exact same place again, only aware that..."]
                                    for i, sentence in enumerate(story):
                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            wait()
                                            die("Developing_Touch/futile")

                                elif choice == "successful": ### END
                                    points.confidence(1)
                                    story = ["...", "Shame. I don't think it will be successful.","As it would turn out, you've just met your demise.",
                                             "I've saved you the trouble of the whole 'death' thing, but you can thank me later.","But otherwise, how was that?",
                                             "Your first experience of the outside world.","Well, 'first' isn't quite right - perhaps only first for *this* you.", 
                                             "Not the previous one, or the countless others before it.","At least you know your place. How could a being with only skin as defence fight against something like that?",
                                             "Life's not easy for everyone, but I don't expect you to know that.","*This* wasn't exactly made as a comfortable, cruisy adventure.",
                                             "But hey, you can dream. Maybe your next life will end differently.","Though I doubt it, as history is bound to repeat itself.",
                                             "You'll just start over from the exact same place again, only aware that..."]
                                    for i, sentence in enumerate(story):
                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            wait()
                                            die("Developing_Touch/successful")
                                    
        elif choice == "embrace": # DONE
            points.charisma(1)
            points.insanity(1)
            story = ["You don't see a reason to be afraid of this existence, and you decide to embrace it.",
                     "The caressing increases, covering your entire body with it's eerie touch as you prevent yourself from resisting.",
                     "An internal conflict rages in your mind and you have to fight against your urge to escape.", "The feeling of suffocation swamps you.",
                     "After much struggle and torment you reach a stable stage; things have appeared to calm down.",
                     "There are a few subtle changes you feel, one of which is that you're more... aware. Sensitive of your surroundings.",
                     "The other is the sensation of strength, as if fortified by the merging of your body and the strange being.",
                     "The next thing that comes to attention is your point of contact with the... ground.", "You seemingly have limbs that reach down, touching the rough, rocky land below you.",
                     "But this isn't what interests you.", "Instead, you're curious about where you are, or if anything like the existence from before is around.",
                     "As such, you wonder which you should investigate first: the (physical world) around you or the potential for other (existences)."]
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "physical world" and choice != "existences":
                        p("You realise that '" + choice + "' just isn't interesting enough.")
                        print("Would you rather investigate the (physical world) or the potential for other (existences)?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "physical world":
                        points.physicality(1)
                        story = ["You feel as if the physical space around you is a more interesting topic of discovery.",
                                 "You find yourself wandering around, exploring by bumping into walls as you slowly trace the world around you.",
                                 "After some time, you discover that there's a split in the path, with walls surrounding you.", "You wonder if you'll go (left) or (right)."]
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "left" and choice != "right":
                                    p("After going in the '" + choice + "' direction, you're met with wall.")
                                    p("You feel embarrassed, as you already knew this was going to happen.")
                                    print("This time, you'll decide if you're going to go (left) or (right)")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "left": # END
                                    points.ponder(1)
                                    story = ["You turn to the left, and continue to explore the winding path.",
                                             "The ground underneath you does not seem to change much, the rough surface remaining a source of mild discomfort.",
                                             "Boredom sets in after quite some time.", "Your mind wanders as you monotonously trudge onwards, guiding yourself with the touch of the wall.",
                                             "These thoughts are broken as you trip, stumbling forwards.", "You expect to be met with the tough surface of the ground in moments, but this does not happen.",
                                             "Your feet leave the ground and you continue falling, rapidly picking up speed.", 
                                             "The harsh bite of the air rushing past you picks up, and the small specks of dust residing in the air become projectiles that bury themselves in your skin.",
                                             "You hit the distant ground and your thoughts go dark, the pain failing to register as death cuts you off first...", ""]
                                    for i, sentence in enumerate(story):
                                        p(sentence)
                                    
                                    story = ["...", "What a shame huh.", "Really should've been looking where you were going, honestly.", "Pay attention next time, and maybe you won't fall down a hole like that.",
                                             "But despite that, there was bit of world exploration for you.", "Pretty cool, right? Even if it did end in somewhat of an abrupt manner.", 
                                             "I must say though, it was quite entertaining for me.", "Anyhow, I'll keep this short - just like your life!", "Wouldn't want to keep you from all the mishaps you'll find yourself in.",
                                             "Stay interesting, why don't you..."]
                                    for i, sentence in enumerate(story):
                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            wait()
                                            die("Developing_Touch/left")

                                elif choice == "right":
                                    points.ponder(1)
                                    story = ["You turn to the right, and continue to explore the winding path.",
                                             "The ground underneath you does not seem to change much, the rough surface remaining a source of mild discomfort.",
                                             "Boredom sets in after quite some time.", "Your mind wanders as you monotonously trudge onwards, guiding yourself with the touch of the wall.",
                                             "At some point you reach a dead end, walls on all sides bar where you came from.", 
                                             "You wonder if you should (turn around) or find some way (through) it."]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "turn around" and choice != "through":
                                                p("Unfortunately, '" + choice + "' isn't an option you can take in this scenario.")
                                                print("How about this time you (turn around) or find some way (through) it?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "turn around": # END
                                                story = ["You begrudgingly walk back in order to take the other path, tracing the same walls for the second time.",
                                                         "The small outcropping, the smooth part, the indent - you pass all the noticeable features you remember.",
                                                         "Eventually you make it back to the split in the path, and take other direction.",
                                                         "Much of the same, recognisable rough ground and winding paths pass, and boredom once again sets in."
                                                         "You can't help it as your mind drifts away, thoughts sporadically popping up as you trundle along.",
                                                         "But these thoughts are broken as you trip, stumbling forwards.", "You expect to be met with the tough surface of the ground in moments, but this does not happen.",
                                                         "Your feet leave the ground and you continue falling, rapidly picking up speed.",
                                                         "The harsh bite of the air rushing past you picks up, and the small specks of dust residing in the air become projectiles that bury themselves in your skin.",
                                                         "You hit the distant ground and your thoughts go dark, the pain failing to register as death cuts you off first.", ""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...", "What a shame huh.", "Really should've been looking where you were going, honestly.", "Pay attention next time, and maybe you won't fall down a hole like that.",
                                                         "But despite that, there was bit of world exploration for you.", "Pretty cool, right? Even if it did end in somewhat of an abrupt manner.", 
                                                         "I must say though, it was quite entertaining for me.", "Anyhow, I'll keep this short - just like your life!", "Wouldn't want to keep you from all the mishaps you'll find yourself in.",
                                                         "Stay interesting, why don't you..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/turn-around")


                                            elif choice == "through":
                                                points.charisma(1)
                                                p("You aren't going to let a simple wall stop you, so you're determined to find a way through it.")
                                                chance = random.random()
                                                if chance < 0.5:
                                                    first_path = True
                                                elif chance >= 0.5:
                                                    first_path = False

                                                if first_path == True: # END
                                                    story = ["After much searching and feeling around the wall, you stumble across a large indent in the wall.",
                                                             "While there had been other indents in the wall, none of them were so... purposeful.",
                                                             "You explore this hollow in the wall, and a section at the back of the wall acts as a button when you push on it.",
                                                             "As this occurs, you feel a tremble nearby as a section of the wall pulls back to reveal a secret room.",
                                                             "This surprises you, and spikes your curiosity.", "Where exactly *are* you? What's around you?",
                                                             "Why would there be a hidden entrance?", "You cautiously move forwards, unsure of how to approach this.",
                                                             "As you grow more confident and walk into the room, sharp pains erupt from you as a large spike impales itself in your body.",
                                                             "You just walked forwards into a spike...", "Somewhat embarrassed but mostly in pain, you try and extricate yourself from the spike.",
                                                             "As you attempt to pull yourself away, a searing pain radiates throughout your body from the removal of the spike.", 
                                                             "Before you fully extract yourself from the situation, you feel a similar agony pierce you from behind.",
                                                             "You now find yourself wedged between two spikes, skewered from both sides, and in a whole other world of pain.",
                                                             "You try and find if there's any way to escape to either of your sides, but you are only met with more spikes when you extend your body.",
                                                             "Panic sets in.", "You're surrounded on all sides by spikes, piercing even your reinforced skin with minimal resistance.",
                                                             "There's no possible way for you to get out without ripping yourself to shreds.",
                                                             "To make matters worse, you begin to feel the spikes to your side inch forwards ever so slowly.",
                                                             "Trapped in a box of spikes, getting smaller and smaller.", "The spikes to your side reach the point of your skin, and you find yourself frozen in place.",
                                                             "Any movement would cause them to puncture you, but...", "You don't have to wait long, unfortunately.",
                                                             "They break your skin, thousands of spikes ranging from tiny to large enclosing you, driving you to the brink of insanity.",
                                                             "You almost miss the suffocation from the existence before, as this time there's real, physical pain.",
                                                             "The spikes continue to push in, bringing with them a myriad of suffering.",
                                                             "Just as you feel as if this torture would never end, the spiky jaws of slam shut with a close, and you die...", ""]
                                                    for i, sentence in enumerate(story):
                                                        p(sentence)

                                                    story = ["...", "Eugh, that was awful.", "Quite a haunting way to go, if I'm honest.","Luckily for you, as always, you won't remember a thing.",
                                                             "A blessing and a curse, that is.", "Then again, if you don't actually know about it, how can it be a blessing or a curse?",
                                                             "Things get very psychological very quickly when talking about this, and for fear of boring you I'll spare it.",
                                                             "Huh. Being bored post-mortem...", "That'd honestly be rather impressive.","Well, I'll leave you to it now.", "Enjoy your 'new discoveries'..."]
                                                    for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Developing_Touch/through/secret-room")

                                                else: # END
                                                    story = ["After much searching and feeling around the wall, you stumble across an outcropping that you believe could support you.",
                                                             "It appears that up is the direction you're planning on going.", "You clasp the rough handhold pull yourself up and continue the search for other handholds.",
                                                             "After a bit of searching you discover one nearby, and you pull yourself up.",
                                                             "This process continues for some time, and numerous times you fall as you adjust yourself to this kind of activity.",
                                                             "Eventually you find a ledge and pull yourself up to it, but you're immediately met with an intense heat that singes your skin.",
                                                             "You reel back, not expecting the pain, but are only met with a similar immense heat behind you.",
                                                             "You feel for the gap you just climbed through to escape back down, but it's... gone.",
                                                             "Only the same old rocky texture meets your skin.", "You move to the sides in an attempt to find another way to escape, but you also feel the searing heat there too."
                                                             "Panic sets in.", "You're surrounded, with nowhere to go.", "You begin to feel the scalding heat encroaching from above you, slowly falling down.",
                                                             "With no way to go horizontally or vertically, you're forced to crouch to avoid being cooked alive by the indomitable flame.",
                                                             "Your skin begins to pop and blister, despite your laying flush to the ground.",
                                                             "The pain grows more and more intense until it touches you.", "A blinding pain erupts at the point of contact, and soon thereafter you're encased in the flame.", ""]
                                                    for i, sentence in enumerate(story):
                                                        p(sentence)

                                                    story = ["...", "Eugh, that was awful.", "Quite a haunting way to go, if I'm honest.","Luckily for you, as always, you won't remember a thing.",
                                                             "A blessing and a curse, that is.", "Then again, if you don't actually know about it, how can it be a blessing or a curse?",
                                                             "Things get very psychological very quickly when talking about this, and for fear of boring you I'll spare it.",
                                                             "Huh. Being bored post-mortem...", "That'd honestly be rather impressive.","Well, I'll leave you to it now.", "Enjoy your 'new discoveries'..."]
                                                    for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Developing_Touch/through/climb")

                                                
                    elif choice == "existences":
                        points.ponder(1)
                        story = ["You wonder about the possibility of other existences, and consider exploring them.",
                                 "With the heightened sensitivity of your skin, you try and 'reach out', feeling for slight disturbances in the air around you in an attempt to track movement.",
                                 "After a moment of searching, you find traces of small movement nearby.", "Something small, weak, timidly testing what it can move.",
                                 "You feel as if this could have been you before you merged with the strange, unknown being - frail and unsure.",
                                 "Now however, with your heightened abilities, you feel as if you could destroy this 'alternate you'.",
                                 "You wander closer to it, roughly painting its outline using the disturbances in the air.",
                                 "It seemingly notices your overbearing presence, as it stiffens and ceases all movement.",
                                 "Although now it appears to have disappeared according to your sense of touch, you are aware it's still there remaining as still as possible.",
                                 "You are eager to test out your newfound sense of fortification and strength, but a sliver of doubt and moral obligation creeps into your mind.",
                                 "Should you (prey) on this weak, puny being, or instead (leave it) in peace?"]
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "prey" and choice != "leave it":
                                    p("Come on. A binary choice.")
                                    p("And guess what? '" + choice + "' isn't one of them.")
                                    print("Now grow up and choose. (Prey) on it or (leave it) in peace?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "leave it":
                                    points.morality(1)
                                    story = ["While you feel as if you should leave it be, your rational thoughts are pushed aside by a primal need to destruction.",
                                             "You weren't aware of this side of your being, believing yourself to be one that sticks to their rational decisions.",
                                             "But this... well, maybe you just need a vent for your power.", "Only once, so..."]
                                    for i, sentence in enumerate(story):
                                        p(sentence) # MERGES INTO 'PREY'

                                elif choice == "prey":
                                    points.morality(-1)
                                story = ["You let your strange, evil desires take over and decide to attack it.",
                                         "Perhaps ending its life will reap other rewards for you, not just joy and entertainment.",
                                         "Either way you would be happy.", "You lash out just once to test how it would react."]
                                for i, sentence in enumerate(story):
                                    p(sentence)

                                if confidence > 3: # it fights back
                                    story = ["Before you can, however, it quickly shifts to the side and launches an attack at you.",
                                             "You feel a blunt force strike your body.", "Fortunately for you, your reinforced skin easily shakes it off, and you barely feel any pain.",
                                             "Clearly this was an act of self-defence from the existence, but not a very effective one at that.",
                                             "And yet, you can't help the enragement brought about by its defiant actions.",
                                             "Fuelled and blinded by anger you rush in, aiming to kill.", "Although you sense its attempt to dodge, you quickly readjust to strike it in its centre.",
                                             "An overwhelming sense of glee fills your body as you feel it fly away from the impact, shivers of enjoyment spreading tingles all over your skin.",
                                             "You know it's severely injured as it weakly tries to limp away from you.",
                                             "You menacingly walk over, taking your time as you bathe in the in the power you feel from preying on the weak.",
                                             "You didn't think this would be something you would enjoy, but things have changed now.",
                                             "This power complex is definitely for you.", "You stop just before reaching it, soaking in all that's good with this situation.",
                                             "After thoroughly bathing in triumph, you decide to end it.", "You gather your strength and kill it in one fell swoop, giddy with joy.",
                                             "Your first kill.", "The wicked euphoria it brings is unlike anything you've felt before.",
                                             "You're on top of the world.", "The only question is, do you want to kill more?",
                                             "Should you pursue this life of (destruction), or (quit) while you're ahead?"]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "destruction" and choice != "quit":
                                                p("Sadly, '" + choice + "' isn't something you can do at the moment.")
                                                print("Instead, you should stick to the life of (destruction), or (quit) while you're ahead.")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "destruction": # END
                                                points.insanity(1)
                                                points.morality(-1)
                                                story = ["More.", "You need more to kill.", "You spend quite some time wandering about, searching for disturbances in the air.",
                                                         "After a while, you sense a slow rise and fall appear in front of you, somewhat in the air.",
                                                         "With arrogance disguised as confidence you purposefully move towards it, mustering up the most imposing appearance you can manage.",
                                                         "All of a sudden, the being exerts an indomitable presence that instantly freezes you in your tracks, the strong aura of death pressing down on you.",
                                                         "You struggle to stay standing, let alone move out of the way.", "Gone is your confidence, instead replaced by terror.",
                                                         "In a desperate cling for survival, you abandon the idea of escape and attempt to make yourself appear as small as possible.",
                                                         "Alas, it seems it still noticed you, as the overbearing pressure only grows.",
                                                         "You briefly notice it flash forwards at a ludicrous speed before your thoughts go dark, the pain failing to register.", ""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...", "You see, that one was kind of on me.", "I didn't really feel like watching a bunch of death and slaughter and misery.",
                                                         "Not to mention you being giddy with joy. That I just couldn't let slide.", "And so I added that... thing.", 
                                                         "Hell, even I don't really know what it is.", "Think of it as me killing you off but with less guilt on my end.",
                                                         "Ah yes, guilt. An emotion.", "Sorry for using terms that you won't understand.","Maybe one day, in *a* life of yours, you'll understand.",
                                                         "By that time though, you won't have the slightest clue that this 'conversation' even happened.", 
                                                         "It could even be your next life, and yet all you'll be aware of is that..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/fights-back/destruction")

                                            elif choice == "quit": # END
                                                points.morality(1)
                                                points.charisma(-1)
                                                story = ["...", "Oh, come on now.", "Be interesting!", "You'd gotten so deep into this whole 'god complex' thing - funny that - but you gave up?",
                                                         "I do suppose those immoral thoughts weren't entirely yours, but...", "Ah well.", "It's fun to dislike you.", "At least it was fun while it lasted.",
                                                         "Quite the spectacle.", "Now back to the drawing board for you; wouldn't want to keep you waiting.", "First and only thing on the agenda..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/fights-back/quit")

                                elif confidence < 4 and charisma > -1: # it runs away
                                    story = ["Before you connect, it dashes away in a desperate attempt for survival.",
                                             "Your glee only grows; now you can make it a chase, toy with your food.",
                                             "You follow slightly behind it, making it appear as if you are struggling to catch up.",
                                             "The air rushes past you, its cold bite digging into your skin, and you struggle to restrain yourself from ending its life.",
                                             "After much torment, you finally make the call.", "You make one last dash forwards and crush it with brute force.",
                                             "A tingling sensation ripples through your body as you watch its lifeless corpse be flung away from you.",
                                             "Your first kill.", "It feels incredible.", "The wicked euphoria it brings is unlike anything you've felt before.",
                                             "You're on top of the world.", "The only question is, do you want to kill more?",
                                             "Should you pursue this life of (destruction), or (quit) while you're ahead?"]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "destruction" and choice != "quit":
                                                p("Sadly, '" + choice + "' isn't something you can do at the moment.")
                                                print("Instead, you should stick to the life of (destruction), or (quit) while you're ahead.")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "destruction": # END
                                                points.insanity(1)
                                                points.morality(-1)
                                                story = ["More.", "You need more to kill.", "You spend quite some time wandering about, searching for disturbances in the air.",
                                                         "After a while, you sense a slow rise and fall appear in front of you, somewhat in the air.",
                                                         "With arrogance disguised as confidence you purposefully move towards it, mustering up the most imposing appearance you can manage.",
                                                         "All of a sudden, the being exerts an indomitable presence that instantly freezes you in your tracks, the strong aura of death pressing down on you.",
                                                         "You struggle to stay standing, let alone move out of the way.", "Gone is your confidence, instead replaced by terror.",
                                                         "In a desperate cling for survival, you abandon the idea of escape and attempt to make yourself appear as small as possible.",
                                                         "Alas, it seems it still noticed you, as the overbearing pressure only grows.",
                                                         "You briefly notice it flash forwards at a ludicrous speed before your thoughts go dark, the pain failing to register.", ""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...", "You see, that one was kind of on me.", "I didn't really feel like watching a bunch of death and slaughter and misery.",
                                                         "Not to mention you being giddy with joy. That I just couldn't let slide.", "And so I added that... thing.", 
                                                         "Hell, even I don't really know what it is.", "Think of it as me killing you off but with less guilt on my end.",
                                                         "Ah yes, guilt. An emotion.", "Sorry for using terms that you won't understand.","Maybe one day, in *a* life of yours, you'll understand.",
                                                         "By that time though, you won't have the slightest clue that this 'conversation' even happened.", 
                                                         "It could even be your next life, and yet all you'll be aware of is that..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/runs-away/destruction")

                                            elif choice == "quit": # END
                                                points.morality(1)
                                                points.charisma(-1)
                                                story = ["...", "Oh, come on now.", "Be interesting!", "You'd gotten so deep into this whole 'god complex' thing - funny that - but you gave up?",
                                                         "I do suppose those immoral thoughts weren't entirely yours, but...", "Ah well.", "It's fun to dislike you.", "At least it was fun while it lasted.",
                                                         "Quite the spectacle.", "Now back to the drawing board for you; wouldn't want to keep you waiting.", "First and only thing on the agenda..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Developing_Touch/runs-away/quit")

                                elif confidence < 4 and charisma < 0: # it gives up
                                    story = ["It doesn't move as your strengthened body connects with a thud, the power from your hit reverberating up your limb.",
                                             "It slides back and remains frozen, the rise and fall of its breath the only indication of life.",
                                             "Although you're committed to preying on it, something feels... wrong.",
                                             "You question whether it is (immoral) to end the life of the innocent, or if you should (continue) anyway."]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "immoral" and choice != "continue":
                                                p("You can't help but notice that '" + choice + "' does not match 'immoral' or 'continue'.")
                                                print("Perhaps you should just answer the question: is it (immoral) to take the life of the innocent, or should you (continue) anyway.")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "immoral":
                                                points.morality(1)
                                                points.ponder(1)
                                                story = ["You wonder if what you're doing is wrong but...", "Something foreign within you tells you it isn't - that you're too far in to back out now.",
                                                         "You know that what you're doing isn't entirely ethical, but the joy of this potential kill overpowers your moral compass."]
                                                for i, sentence in enumerate(story):
                                                    p(sentence) # MERGES INTO 'CONTINUE'

                                            elif choice == "continue":
                                                points.morality(-1)
                                                points.ponder(-1)
                                            story = ["What even were morals to you, anyway?", "As such, you continue with your plan of execution.",
                                                     "The fear-ridden existence stays frozen as you trundle towards it, any morals of yours left behind.",
                                                     "You menacingly walk over, taking your time as you bathe in the in the power you feel from preying on the weak.",
                                                     "You didn't think this would be something you would enjoy, but things have changed now.",
                                                     "This power complex is definitely for you.", "You stop just before reaching it, soaking in all that's good with this situation.",
                                                     "After thoroughly bathing in triumph, you decide to end it.", "You gather your strength and kill it in one fell swoop, giddy with joy.",
                                                     "Your first kill.", "The wicked euphoria it brings is unlike anything you've felt before.",
                                                     "You're on top of the world.", "The only question is, do you want to kill more?",
                                                     "Should you pursue this life of (destruction), or (quit) while you're ahead?"]
                                            for i, sentence in enumerate(story):
                                                print(sentence)
                                                if i < len(story) - 1:
                                                    wait()
                                                else:
                                                    choice = rp(input("> ").lower().strip())

                                                    while choice != "destruction" and choice != "quit":
                                                        p("Sadly, '" + choice + "' isn't something you can do at the moment.")
                                                        print("Instead, you should stick to the life of (destruction), or (quit) while you're ahead.")
                                                        choice = rp(input("> ").lower().strip())

                                                    if choice == "destruction": # END
                                                        points.insanity(1)
                                                        points.morality(-1)
                                                        story = ["More.", "You need more to kill.", "You spend quite some time wandering about, searching for disturbances in the air.",
                                                                "After a while, you sense a slow rise and fall appear in front of you, somewhat in the air.",
                                                                "With arrogance disguised as confidence you purposefully move towards it, mustering up the most imposing appearance you can manage.",
                                                                "All of a sudden, the being exerts an indomitable presence that instantly freezes you in your tracks, the strong aura of death pressing down on you.",
                                                                "You struggle to stay standing, let alone move out of the way.", "Gone is your confidence, instead replaced by terror.",
                                                                "In a desperate cling for survival, you abandon the idea of escape and attempt to make yourself appear as small as possible.",
                                                                "Alas, it seems it still noticed you, as the overbearing pressure only grows.",
                                                                "You briefly notice it flash forwards at a ludicrous speed before your thoughts go dark, the pain failing to register.", ""]
                                                        for i, sentence in enumerate(story):
                                                            p(sentence)

                                                        story = ["...", "You see, that one was kind of on me.", "I didn't really feel like watching a bunch of death and slaughter and misery.",
                                                                "Not to mention you being giddy with joy. That I just couldn't let slide.", "And so I added that... thing.", 
                                                                "Hell, even I don't really know what it is.", "Think of it as me killing you off but with less guilt on my end.",
                                                                "Ah yes, guilt. An emotion.", "Sorry for using terms that you won't understand.","Maybe one day, in *a* life of yours, you'll understand.",
                                                                "By that time though, you won't have the slightest clue that this 'conversation' even happened.", 
                                                                "It could even be your next life, and yet all you'll be aware of is that..."]
                                                        for i, sentence in enumerate(story):
                                                            cprint(sentence, "red", attrs=["bold", "dark"])
                                                            if i < len(story) - 1:
                                                                wait()
                                                            else:
                                                                wait()
                                                                die("Developing_Touch/gives-up/destruction")

                                                    elif choice == "quit": # END
                                                        points.morality(1)
                                                        points.charisma(-1)
                                                        story = ["...", "Oh, come on now.", "Be interesting!", "You'd gotten so deep into this whole 'god complex' thing - funny that - but you gave up?",
                                                         "I do suppose those immoral thoughts weren't entirely yours, but...", "Ah well.", "It's fun to dislike you.", "At least it was fun while it lasted.",
                                                         "Quite the spectacle.", "Now back to the drawing board for you; wouldn't want to keep you waiting.", "First and only thing on the agenda..."]
                                                        for i, sentence in enumerate(story):
                                                            cprint(sentence, "red", attrs=["bold", "dark"])
                                                            if i < len(story) - 1:
                                                                wait()
                                                            else:
                                                                wait()
                                                                die("Developing_Touch/gives-up/quit")
