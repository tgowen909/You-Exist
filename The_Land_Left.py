# Path: no > body > smells > left

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



story = ["You decide - to the sickly sweet smell.", "Why, you do not know, but you turn towards the left.", "You falter.",
         "One crucial step you had not accounted for was how to move.", "You realise this problem is rather... inconvenient.", 
         "You give it a quick shot, but to no avail.", "Although it isn't what you planned or wanted to, you wonder whether you should (give up). Either that or show some (resilience)."]

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "give up" and choice != "resilience":
            print("Maybe you didn't connect the dots between what you were thinking and feeling.")
            wait()
            print("In case that was going on, you remind yourself that resilience is your grit, your perseverance.")
            wait()
            print("With newfound confidence in this knowledge, you consider whether you should (give up) or show some (resilience).")
            choice = rp(input("> ").lower().strip())

        if choice == "give up": # END
            points.confidence(-1)
            points.charisma(-1) 
            points.ponder(-1) # Confidence - 1, Charisma - 1, Ponder - 1
            story = ["...", "What a remarkably mundane imbecile you are.", "Stale, even.", "No long speech or anything from me, but just try again this time.", 
                     "Maybe a bit harder - use that exquisite brain of yours to its full capacity.", "Well, off you go.", "Maybe this time will be different..."]
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

        elif choice == "resilience":
            points.charisma(1)
            points.physicality(1)
            story = ["You don't know what you're doing, but you try again anyway.", "You think of it not like you moving towards the scent, but rather... moving it towards you.", 
                     "To your utter surprise, it works.", "The sickly sweet smell draws closer.", "As you approach it, two feelings conflict within you:", 
                     "One of comfort and one of unease.", "You are tempted to give in to this sense of comfort, but you have a hunch this won't bode well.", 
                     "So alluring...", "Despite not having smelt much in your brief existence, you cannot imagine a more sweetly captivating scent.", 
                     "You struggle to think about anything other than moving forwards, closer and closer to this mesmerising fragrance.", "You feel... safe.", 
                     "Soothed.", "As you work your way further, you begin to distinguish individual objects that make up such a collection of essence.", "Almost like... little bulbs - pods - all sitting around the same height.", 
                     "They're intoxicating.", "You need it.", "You wonder - is there any way to make it a part of you?", "Take it into your 'body'; experience it in ways other than smell.", 
                     "With excitement, you ask yourself if you should (commit) to such a decision, or perhaps attempt to (inspect) this 'pod' before doing so."]
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "commit" and choice != "inspect":
                        p("You get distracted with the idea of '" + choice + "' before reminding yourself that your options are rather limited.")
                        print("Will you (commit) to such a decision, or perhaps attempt to (inspect) this 'pod' before doing so?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "commit": # END
                        points.insanity(1)
                        points.ponder(-1)
                        story = ["Without a second thought you do what only feels natural, and... eat it.", "Although you are unsure as to how exactly you 'eat' it, you begin to feel its effect.",
                                 "Swirling, prancing, strange colours sporadically appear, painting a story in an indescribable way as they flash in your mind.", 
                                 "But... maybe it isn't just in your mind?", "Your vision begins to take shape, meaning assigned to the mess of lines and colours filling your perspective.", 
                                 "You can see...", "Rows upon rows of colourful, illusory flowers swaying perfectly in unison to and fro enter your vision.", 
                                 "The mesmerising dance is accompanied by the sickly sweet aroma from before, adding to its majestic touch.",
                                 "It's beautiful...", "Just as you begin to truly appreciate it's captivating grace, your vision fades.", "Your sight - quiet, black, empty - no more.",
                                 "You are met with the nothingness your life was prior to this experience.", "...", "You must have more.", "How could you live without such a thing, your sight?", 
                                 "You eat another.", "And another.", "And another.", "Desperate to experience the enrichment of the view, of seeing, your devour as many as you can.", "It returns.",
                                 "More colours and bright lights swirl and dance across your vision, the individuality of smell and colour dissipating, merging into an explosion of senses.",
                                 "Your thoughts lose meaning, an incoherent mess of exotic jargon.", "Nothing is legible, and yet...", "It all makes sense.", 
                                 "The lights, smells, get brighter with each passing moment.", "You reach out, and it pulls you in.", "You feel a flash of satisfaction within yourself before your thoughts too join the void, and you lay down your life...", ""]
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i == 0:
                                achievements.LSD_Overdose()
                                wait()
                            elif i == 5:
                                achievements.Vision()
                                wait()
                            elif i < len(story) - 1:
                                wait()
                            else:
                                wait()
                                story = ["...", "Well that was interesting.", "Certainly not the ending I was expecting.", "Although I don't suppose I can call this an 'ending'.", 
                                         "You'll just go back to being the same old, boring you.", "Actually scratch that - you're not boring.", "Certainly not interesting - but that ending, well...", 
                                         "Anyway, enough rambling.", "Didn't your mother ever tell you not to eat strange things?", "Lesson learnt, then.", "So long, and farewell..."]
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

                                                
                    elif choice == "inspect":
                        points.ponder(1)
                        points.physicality(1)
                        story = ["You don't really know what you were thinking, as you run into another unexpected problem.", 
                                 "How were you planning to inspect it?", "All at your disposal was the ability to think and smell - not ideal for getting a better idea of what these pods are.",
                                 "After much consideration, you feel as if you have only 2 options.", "You can either (feel) it or... (become it)."]
                        for i, sentence in enumerate(story):
                            print(sentence)
                            if i < len(story) - 1:
                                wait()
                            else:
                                choice = rp(input("> ").lower().strip())

                                while choice != "feel" and choice != "become it":
                                    p("You've racked your mind for this decision, and '" + choice + "' wasn't one of the ideas you came up with.")
                                    p("Unfortunately, you don't think it will work.")
                                    print("Instead, will you (feel) it or (become it)?")
                                    choice = rp(input("> ").lower().strip())

                                if choice == "feel": # DONE
                                    points.physicality(1)
                                    story = ["To feel it...", "You feel as if this strange pod must have an outside to encase it.",
                                             "By the same logic, so would you, no?", "Something to hold you together, to store your existence and place it within the physical world.",
                                             "As if prompted by your thoughts, you feel the cool touch of wind brush up against your skin.",
                                             "You feel the fluctuations in the air, bathing in the new sensory experience.","Even fluctuations in the air amaze you, a revolutionary perception of the world.",
                                             "The air around you feel predominantly... thick.", "Like something is bogging down the world around you.",
                                             "You have skin, and you can feel - both of which are ground-breaking discoveries, and yet...",
                                             "You can't help but wonder what the odd pod feels like.","You slowly reach out, excitedly nervous for what it feels like.",
                                             "When you do end up touching it, a smooth, silky tactile experience blesses your skin.","Divine...",
                                             "The strange pod is even more alluring to the touch than by scent, more so than you could ever imagine.",
                                             "You imagine being wrapped in such a material would be so angelic it would endanger your life, never able to live normally again...",
                                             "Amazed by it's incredible touch, you wonder if you should (continue exploring) the rest of the irresistible pod, or stick with what you have and (consider) what you can do it."]
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i == 4:
                                            achievements.Touch()
                                        elif i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "continue exploring" and choice != "consider":
                                                p("You're completely focussed on the irresistible pod, and '" + choice + "' isn't in your mind's interests.")
                                                print("You believe you should stick to what you've got and (consider) what you can do with the pod, or (continue exploring) it.")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "continue exploring": # END
                                                points.ponder(1)
                                                story = ["Somewhat begrudgingly, you leave behind the divine touch and work your way down the rest of the extraordinary petals.",
                                                         "Unfortunately, as you begin exploring what appears to be the stem that holds up the pod, a sharp pain pricks your skin, a throbbing pain following quickly in suit.",
                                                         "You quickly draw back, the pain an unknown experience to your newly developed skin.",
                                                         "All feelings of safety and love for the abnormal plant dropped in a flash.","The throbbing pain spreads, moving up your limb, crawling underneath your skin.",
                                                         "A freezing numbness emerges from the pricked spot, quickly following suit by spreading.",
                                                         "It continues to spread throughout your body, swelling and swelling, and you feel like you're splitting at the seams.",
                                                         "The poison, coursing through you body, permeating its ice-cold numbing and swelling of death, tears you between feeling nothing and agonizing pain.",
                                                         "Until finally, you burst.", "The poison did its work, and you die, exploding into a fiery blaze of glory...", ""]
                                                for i, sentence in enumerate(story):
                                                    p(sentence)
                                                story = ["...", "WOAH!", "That was awesome...", "*ahem*", "I mean... I, uh...", "Sorry for your loss?",
                                                         "Ah what do I care.", "If you were me you'd think your 'fiery blaze of glory' was pretty damn epic too.",
                                                         "And plus, I doubt you care either.", "I'm just a strange, overbearing being who shows up momentarily every now and then.", 
                                                         "And then you forget straight after!", "Pretty convenient for me, if I must say so myself.", "I practically have no restrictions on what I say and do.", 
                                                         "Then again, I don't see why I would feel the need to place restrictions on myself even if you *did* remember.", "I'm practically god, after all.", 
                                                         "Now, back to your explosive death.", "I gotta say, pretty unlucky way to go. Looked painful.", "Luckily however, there won't be any long-standing trauma or anything...", 
                                                         "I think...", "Enough said.", "I wish you well in your new, PTSD-free life.", "Farewell, for now..."] 
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

                                            elif choice == "consider":
                                                points.charisma(-1)
                                                story = ["You feel as if the more important part of this strange plant is what you've already explored, like everything else is less relevant.",
                                                         "Despite the divine petals you're already aware of, something feels... off.",
                                                         "You can't quite pick it, but perhaps this pod isn't quite as spectacular as you originally thought?",
                                                         "Unsure of how you should approach it, you wonder if you should (protect) or (destroy) it."]
                                                for i, sentence in enumerate(story):
                                                    print(sentence)
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        choice = rp(input("> ").lower().strip())

                                                        while choice != "protect" and choice != "destroy":
                                                            p("Your focus needs more focus, as your mind seems to have drifted to '" + choice + ".'")
                                                            print("Should you (protect) it or (destroy) it?")
                                                            choice = rp(input("> ").lower().strip())

                                                        if choice == "protect": ### PROTECT
                                                            points.morality(1)
                                                            points.charisma(-1)
                                                            story = ["The silky embrace of its petals are something you believe should be kept safe for all of eternity.",
                                                                     "Nothing could be worse than the loss of the blissful touch gracing your skin.",
                                                                     "And so, you encase it, protecting it by sacrificing your own skin to any and all that may try to harm it.",
                                                                     "Deep inside your soul you promise to protect it.","You become the witness to every coming and going that occurs, an indomitable wall to the passage of time.",
                                                                     "Time itself loses meaning as you hyperfocus only on its protection.",
                                                                     "Passing smells and fleeting changes in the air become a blur, fading out of importance so long as they don't endanger your child.",
                                                                     "As this so called 'time' passes, flashes of colour begin to enter your mind, often accompanied by a tactile change on your weathered skin.",
                                                                     "These flashes of colour increase in frequency, heightening in detail with more colours as time flows.",
                                                                     "Flashes of colour become steadfast, no longer temporary, and shapes begin to make themselves clear, forming a solid image in your mind.",
                                                                     "Sight.", "You can see.", "You snap yourself back to the present, experiencing the time in the moment.",
                                                                     "This incredible sensation is now yours, allowing you to truly experience the things around you.",
                                                                     "Your attention is drawn towards that which you are protecting - a flower.",
                                                                     "A delicate rose of swirling greens, pinks, blues, the acidic colours merging and swelling in a disturbingly beautiful way.",
                                                                     "It's just as incredible as you felt and smelt, only more so.","The visual experience is leagues beyond anything smell and touch could provide.",
                                                                     "Turning your attention back to the flower, you slowly trace your sight down the flower, inspecting the stem it grows from.",
                                                                     "The stem is... severely lacking in grace compared to its counterpart.","It's grey, spindly, and has intimidating thorns seeping a sickly yellow liquid all over it.",
                                                                     "It looks... wrong.","Like the exquisite flower with silken petals above it is a lure.",
                                                                     "That thought does not sit well in your mind, given you'd spent eons protecting it.",
                                                                     "Because of this, you wonder if you should (escape) from this place, or (stay) and keep true to your timeless promise of protection."]
                                                            for i, sentence in enumerate(story):
                                                                print(sentence)
                                                                if i == 11:
                                                                    achievements.Vision()
                                                                if i < len(story) - 1:
                                                                    wait()
                                                                else:
                                                                    choice = rp(input("> ").lower().strip())

                                                                    while choice != "escape" and choice != "stay":
                                                                        p("You don't want to betray the wonderful flower any more with '" + choice + "' in this difficult decision.")
                                                                        print("Should you (escape) from this place, or (stay) and keep true to your timeless promise of protection?")
                                                                        choice = rp(input("> ").lower().strip())

                                                                    if choice == "escape": # END
                                                                        points.ponder(1)
                                                                        points.morality(-1)
                                                                        story = ["These flowers seem off, and you're willing to give up on your promise.",
                                                                                 "You look around to determine the best course of action, and see rows upon rows of these eerie, illusory flowers spread out as far as you can see, cresting the horizon.",
                                                                                 "That is, except from behind you, the direction you came from so long ago.","Leaving the flowery expanse behind you, your march onwards.",
                                                                                 "You begin to smell vaguely familiar scents.",
                                                                                 "To your left is the dark, ominous aroma; straight ahead is the clean, fresh scent; and of course, behind you is the sickly sweet smell you know so well.",
                                                                                 "As you draw closer, distant images appear in your sight to accompany the fragrances.",
                                                                                 "An expansive, lush, grassy plain stretches into the distance ahead of you, and towards the left lies a vast mountain range, the peaks of which loom over you from even such a distance.",
                                                                                 "However, the longer you travel for, the more you vision becomes less refined.","It blurs, the distant mountains now a greyscale silhouette, the grassy plain a green mess.",
                                                                                 "The lights dim, lines and colours losing their shape, before you're finally plunged into darkness.","Your sight is gone.","Gone.",
                                                                                 "The incredible ability to see the world around you, to immerse yourself in it, has been whisked away from you.",
                                                                                 "Panic sets in.","How can you live without such a thing?",
                                                                                 "How are you meant to make your way around?","You feel, well, blinded. Empty and vulnerable, without your vision.",
                                                                                 "You come to the conclusion that the eerie flower expanse was the source of your vision.",
                                                                                 "Perhaps *something* had seeped through your skin, gotten into your body and graced you with the gift of sight.",
                                                                                 "You have to go back.","You need to see again. Desperately.",
                                                                                 "You turn yourself around again, and pick up on the sickly sweet fragrance, attempting to pull yourself towards it.",
                                                                                 "You... struggle.","You had become dependent on your vision, but now uncertainty has crept into your mind, leaving you weak.",
                                                                                 "Fortunately, you are still capable of movement, and the alluring aroma draws closer.",
                                                                                 "You find yourself in the midst of the flowers once more, and, somewhat regretfully, you default back to protecting your flower.",
                                                                                 "You even made sure to get the right one - you knew its scent so well by now.",
                                                                                 "If being here is required for you to have vision, then you're content to be around the sinister flowers.",
                                                                                 "You wait, and wait.","Slowly, the colours return. Flashes at a time, but soon the familiar shapes and patterns make themselves clear.",
                                                                                 "And once again is the one right in front of you, it's delicate petals supported by the nightmarish stem.",
                                                                                 "The one that you've been with all this time.","You continue to protect it from anything that could potentially harm it, just like in the beginning.",
                                                                                 "Time once again becomes a blur, the flicker of light and dark as a foreign ball of intense bright light rises from one horizon and falls at the other.",
                                                                                 "You see these eerie plants wilt and die, and new ones sprout from the ground in an impressive feat of nature, a time-lapse of life.",
                                                                                 "Your vision becomes more crisp, every nook and cranny visible in utmost detail.",
                                                                                 "At one point, an incorporeal being of mist and shadow materialises itself in the corner of your sight, grotesquely staring at you.",
                                                                                 "Or more rather, at your plant.","It menacingly creeps forwards and proceeds to speak in your mind, injecting its thoughts over the top of your own.",
                                                                                 "It wants your flower.","But it's yours! You vowed to protect it at the start, and you can hardly go back on that promise now.",
                                                                                 "A distorted growl echoes in your mind.","It certainly isn't pleased with your decision, and lashes out at you, black mist trailing behind its limbs.",
                                                                                 "You flinch, expecting a physical blow, but are instead met with a staggering pain that burns within your mind.",
                                                                                 "You stare at it ludicrously as it temporarily repeats, knowing it's just waiting to let you make a decision yourself.",
                                                                                 "But you already know what you want to do.","Protect it.","Protect the flower at all costs.",
                                                                                 "As if reading your mind, and perhaps it was, the shadow wraith splits itself into eight, each circling you with fierce intensity.",
                                                                                 "They all bombard your mind with thoughts to surrender the flower, their voices cascading into a tumultuous barrage of grotesque shouts.",
                                                                                 "You strive to protect, and them to destroy, their superimposed thoughts ripping apart your mind, the conflict tearing your soul in half.",
                                                                                 "The voices swell.", "Your mind breaks.", "You fall apart...", ""]
                                                                        for i, sentence in enumerate(story):
                                                                            p(sentence)
                                                                        story = ["...", "What an incredible way to meet your wits' end.", "And your wits' end it was! Cause that shit was *not* real.",
                                                                                 "Quite literally a figment of your find.", "So how should I log this one?", "Schizo loves a flower a little too much?", 
                                                                                 "Yeah... seems suitable.", "But hey, props to you. You got a lot done this time around.", "Smell, touch, sight... quite the trinity if I must say so myself.",
                                                                                 "The question is... can you do it again..."]
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
                                                                        
                                                                    elif choice == "stay": # END
                                                                        points.morality(1)
                                                                        points.ponder(-1)
                                                                        story = ["You decide that your promise to keep this flower safe stretches beyond your unease.",
                                                                                 "Content with your decision, you turn your attention to what's around you, beyond just this flower...",
                                                                                 "And you see rows upon rows of these illusory flowers spread out as far as you can see, cresting the horizon.",
                                                                                 "All of this... is yours.","But no. All that matters to you is this one right in front of you.",
                                                                                 "The one that you've been with all this time.","And you continue to protect it from anything that could potentially harm it, just like in the beginning.",
                                                                                 "Time once again becomes a blur, the flicker of light and dark as a foreign ball of intense bright light rises from one horizon and falls at the other.",
                                                                                 "You see these eerie plants wilt and die, and new ones sprout from the ground in an impressive feat of nature, a time-lapse of life."
                                                                                 "Your vision becomes more crisp, every nook and cranny visible in utmost detail.",
                                                                                 "At one point, an incorporeal being of mist and shadow materialises itself in the corner of your sight, grotesquely staring at you.",
                                                                                 "Or more rather, at your plant.","It menacingly creeps forwards and proceeds to speak in your mind, injecting its thoughts over the top of your own.",
                                                                                 "It wants your flower.","But it's yours! You vowed to protect it at the start, and you can hardly go back on that promise now.",
                                                                                 "A distorted growl echoes in your mind.","It certainly isn't pleased with your decision, and lashes out at you, black mist trailing behind its limbs.",
                                                                                 "You flinch, expecting a physical blow, but are instead met with a staggering pain that burns within your mind.",
                                                                                 "You stare at it ludicrously as it temporarily repeats, knowing it's just waiting to let you make a decision yourself.",
                                                                                 "But you already know what you want to do.","Protect it.","Protect the flower at all costs.",
                                                                                 "As if reading your mind, and perhaps it was, the shadow wraith splits itself into eight, each circling you with fierce intensity.",
                                                                                 "They all bombard your mind with thoughts to surrender the flower, their voices cascading into a tumultuous barrage of grotesque shouts.",
                                                                                 "You strive to protect, and them to destroy, their superimposed thoughts ripping apart your mind, the conflict tearing your soul in half.",
                                                                                 "The voices swell.", "Your mind breaks.", "You fall apart...", ""]
                                                                        for i, sentence in enumerate(story):
                                                                            p(sentence)
                                                                        story = ["...", "What an incredible way to meet your wits' end.", "And your wits' end it was! Cause that shit was *not* real.",
                                                                                 "Quite literally a figment of your find.", "So how should I log this one?", "Schizo loves a flower a little too much?", 
                                                                                 "Yeah... seems suitable.", "But hey, props to you. You got a lot done this time around.", "Smell, touch, sight... quite the trinity if I must say so myself.",
                                                                                 "The question is... can you do it again..."]
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


                                                        elif choice == "destroy": # DONE
                                                            points.charisma(1)
                                                            points.morality(-1)
                                                            story = ["Unsettled by the strange feeling, you decide to crush the pod in an attempt to destroy it.",
                                                                     "You reach out to the eerily pleasant plant and grasp it, taking a moment to soak in it's silky exterior.",
                                                                     "With some resentment but determination, you crush it, the delicate petals turning to dust within your clutches.",
                                                                     "You feel the powdered petals drift away from your skin, permeating around you as they're carried by the currents in the air.",
                                                                     "A strange scent enters your perception, penetrating your thoughts as if attempting to burrow itself within your mind.",
                                                                     "As the aroma from the alluring plant grows more pungent than ever, you begin to question your past choices.",
                                                                     "Was destroying it such a great idea?","Will the scents piercing your mind bring about your untimely demise?",
                                                                     "Should you (continue) to destroy these plants, or perhaps attempt to (escape)?"]
                                                            for i, sentence in enumerate(story):
                                                                print(sentence)
                                                                if i < len(story) - 1:
                                                                    wait()
                                                                else:
                                                                    choice = rp(input("> ").lower().strip())

                                                                    while choice != "continue" and choice != "escape":
                                                                        p("Pressed for time by a potentially untimely demise, '" + choice + "' won't solve this problem.")
                                                                        print("Will you (continue) in your path of destruction, or perhaps attempt to (escape)?")
                                                                        choice = rp(input("> ").lower().strip())

                                                                    if choice == "continue": # DONE
                                                                        points.charisma(-1)
                                                                        story = ["You doubt a simple smell could do harm to you and thus decide to continue with your destructive actions.",
                                                                                 "Full confidence in your immunity to the strange pod's incense, you begin crushing numerous of these delicate petals.",
                                                                                 "The feeling of power runs rampant within you, devastating one after the other as they are annihilated at your touch.",
                                                                                 "As you continue, the fragrance only builds in intensity, seeping into your mind.",
                                                                                 "Slowly, you begin to feel your body fail to respond to what you want it to do.","At first it was just a delay in movement, but now...",
                                                                                 "Now you can't move.","Although you have still retained your sense of smell and touch, which you are thankful for at least, it's impossible for you to satiate your murderous bloodlust.",
                                                                                 "You struggle for quite some time, desperately trying to reach out to the nearest silk petals and demolish them in your clasp.",
                                                                                 "Eventually, you feel fallen petals beneath you shift and swell with a unified motive as they conjure up the strength to carry you.",
                                                                                 "They appear to be carrying you further into the depths of this uncanny field, and strangely enough you find yourself doing the opposite of resisting.",
                                                                                 "Instead, your body accepts this movement, almost eager to find out what happens.",
                                                                                 "Your mind is strongly against the idea, however.","An alien clash of mind and body wars within you, tearing you apart.",
                                                                                 "During this ongoing tension, a powerful smell of a foreboding scent washes over you.",
                                                                                 "It's much like these pods here, but infinitely more potent.","You come to the conclusion that the origins of this authority cannot bode well for you.",
                                                                                 "You wonder if you should (fight) against it somehow, or (accept) your fate."]
                                                                        for i, sentence in enumerate(story):
                                                                            print(sentence)
                                                                            if i < len(story) - 1:
                                                                                wait()
                                                                            else:
                                                                                choice = rp(input("> ").lower().strip())

                                                                                while choice != "fight" and choice != "accept":
                                                                                    p("You're too pressed for time to consider '" + choice + ".'")
                                                                                    print("Should you (fight) against it, or (accept) your fate?")
                                                                                    choice = rp(input("> ").lower().strip())

                                                                                if choice == "fight": # END
                                                                                    points.charisma(1)
                                                                                    story = ["Your will to live still outweighs this seemingly crushing defeat.","But despite your efforts, nothing you seem to do can prevent you from being drawn ever closer to impending doom.",
                                                                                             "With time running out, a wild plan forms in your mind.","You aim to be drawn near, lull this almighty being into a false sense of comfort, and strike at it when it least expects it.",
                                                                                             "It all rides on it not noticing your actions, the sudden change in your acceptability.", "You press on with the idea.",
                                                                                             "As the overpowering aroma draws scarily close you cease your resistance, intending to fool it, to 'play dead'.",
                                                                                             "Just as you're about to set everything into action, you feel an elegant, silky ribbon wrap itself around you.",
                                                                                             "Despite its unbelievably pleasant texture, it begins to constrict around you with fierce intensity.","More ribbons dart in from all directions and you're swamped.",
                                                                                             "Your already-restricted movement becomes completely immobilised as you're held with a deadly iron grip, all area of your skin cut off from the outside world.",
                                                                                             "You are cocooned, the bands of petals seeping all life from you in an overwhelming way.",
                                                                                             "Your body is finally ripped from your mind, the separation instantly ending your life - both your body's and your soul's...", ""]
                                                                                    for i, sentence in enumerate(story):
                                                                                        p(sentence)
                                                                                    story = ["...", "Ah, yikes.", "Looked painful.", "You know, that's the cruel thing about this whole fiasco.", "When everything else meets their horrid, ghastly end in a brutal manner, they just... die.",
                                                                                             "No chance for redemption, but I suppose that's for the good.", "You on the other hand... you're a special case",
                                                                                             "Forced into a timeless loop of life and death, glory and pleasure, pain and suffering.", "And I get to see it all!",
                                                                                             "The mystery of birth and your curiosity to discover yourself - a classic.", "Your development of smell and touch, the revolutionary new perceptions of the world.",
                                                                                             "The glee and power you felt as you crushed the life out of those poor, uncanny flowers.",
                                                                                             "Your subsequent ignorance of the dangers you faced, reluctance to meet with the truth.",
                                                                                             "And lastly - and most spectacularly - your demise.", "Isn't it beautiful? What we have here, together?",
                                                                                             "And we get to do it all again!", "You, down in the fields. And me, always watching.", "Enjoy these fleeting moments..."]
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
                                                                                    
                                                                                elif choice == "accept": # END
                                                                                    points.charisma(-1)
                                                                                    points.physicality(-1)
                                                                                    story = ["This overwhelming command reigns high above you in power, and there's virtually nothing you can do to prevent the following course of action.",
                                                                                             "You cease resistance and let yourself be carried by the flow of fallen petals."
                                                                                             "You drift peacefully, the intensifying aroma not posing a threat to your sanity, embracing what is to come.",
                                                                                             "Expansive, eloquent, silky ribbons gently ease and wrap themselves around your body.","They cover your entirety in the bliss of the silk petals.",
                                                                                             "As you are cocooned, you slowly lose control of yourself, and your thoughts ease to darkness.",
                                                                                             "Your body is gingerly detached from your mind and soul in a painless manner, and without the two living in harmony your existence swiftly flickers out...", ""]
                                                                                    for i, sentence in enumerate(story):
                                                                                        p(sentence)
                                                                                    story = ["...", "How... dramatic.", "I never took you as theatrical. Who knew?", "But hey, life does that to people.",
                                                                                             "And for you no doubt. You get so many lives!", "So many chances to changed forever.", 
                                                                                             "...and by forever I mean a limited amount of time, until you inevitably die and get set back to square one.",
                                                                                             "So while your theatrics were so incredibly moving, unfortunately, they've got to go.", "You and your dramatic tendencies will be but down, only aware that..."]
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


                                                                    elif choice == "escape": # END
                                                                        points.ponder(1)
                                                                        story = ["You realise you need to escape from this place, lest the scents invading your mind will take control.",
                                                                                 "You move back in the direction you came from, away from the eerie aroma.","As you near the edge of the field of these off-putting plants, they shift in unison, seemingly growing, blocking your way.",
                                                                                 "They form an impenetrable wall, the gentle touch of the silky petals vastly different from the iron defence that's preventing you from escaping.",
                                                                                 "You try and get through numerous times, but continue to fail.","It's almost as if the plants are a hive mind, intentionally preventing you from escaping.",
                                                                                 "Just as you think this, the sickly sweet smell swells, overloading your olfactory sense and burrowing deeper into your mind.",
                                                                                 "Then, the dark abyss of emptiness welcomes you in its open grasp.","You vaguely remember having thoughts, smells, touch... but they slowly lose meaning, replaced by something... waiting."
                                                                                 "Your sense of self, dissipating with every moment as the aroma plagues your mind.",
                                                                                 "A flicker of true terror flashes within you, before it too vanishes as your body is taken possession of, your soul exorcised against your will...", ""]
                                                                        for i, sentence in enumerate(story):
                                                                            p(sentence)
                                                                        story = ["...", "Well, the plan was great, but the execution was not.", "And as much as I'd like to say there was, there wasn't much you could do about that, if anything.",
                                                                                 "So you can rest well knowing that you were destined to die in the end.", "There's almost no point, is there?", "Fated to die, fated to repeat.",
                                                                                 "From my perspective, it's incredible you continue.", "From your perspective, well...", "Let's just say that ignorance is bliss..."]
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


                                elif choice == "become it": # DONE
                                    points.charisma(1)
                                    points.physicality(1)
                                    points.insanity(1)
                                    story = ["You ponder, realising that becoming it is the best plan of action for inspecting it.", "After all, if you're *it*, then theoretically you would know yourself.",
                                             "Theoretically...", "And so, you attempt to morph yourself into the alluringly sweet pod in front of you.", "Although you don't explicitly feel it, you sense some subtle changes occurring to you.",
                                             "The smells surrounding you draw higher - or perhaps you move closer to the ground.", "You... shrink.", 
                                             "Your existence somehow becomes smaller than it was previously, though your own size has never crossed your mind before.",
                                             "As the changes occurring to you cease, a bath of sensory information washes over you.", "Your smell stretches outwards expansively, so much more aware of the eerily pleasant aroma from before.",
                                             "But, something's different.", "It's... you.", "You are a flower.", "You are the flowers.", "Upon your existential change, you notice the subtle yet swift departure of another existence.",
                                             "It seemed to be... inhabiting the flowers, just like you are now.", "Puzzled, you mull over what it could have possibly been, but fail to think of anything.",
                                             "Instead, you move on to exploring what you are - a flower, yes, but what else?", "Beautiful on the outside, deadly on the inside.",
                                             "You feel as if 'you', the flowers, were made to deceive with charm, lure to kill.", 
                                             "Satisfied with your discovery of the true intentions behind the flowers, you make to revert back to your original form... whatever that may be...",
                                             "Only to find that you cannot.", "You're locked in.", "The trapper becomes the trapped.", "Ironic really.",
                                             "You cannot seem to pull your conscious from the collective of flowers and back in to what you were previously.", "This worries you, but the cogs have already started turning in your mind.",
                                             "That fleeting existence from before, from when you had just 'become' the flowers, appeared to leave just as you had transformed, seemingly inhabiting these flowers prior.",
                                             "Perhaps if something else were to inhabit you, or rather the flowers, then you too would be able to leave?", "Suddenly, it makes sense.",
                                             "This is why you - the deadly flowers - are so deceptively beautiful.", "You are made to lure in prey to liberate yourself.",
                                             "Although you can't confirm it, you have a hunch that being the cause of a victim's death would also free your existence.", "Things do not seem so bleak and hopeless now.",
                                             "You have a plan, and now only need another existence to execute it.", "Another existence...", "You have no choice but to wait, hoping something much like yourself will wander by and become captivated.",
                                             "Time passes.", "A lot of time.", "Finally, you feel the relieving tremble of an approaching existence through the ground.",
                                             "Your roots, splayed far and wide, feel each movement of the being with stark detail.", "This is... another form of sense.", "Touch - limited, however.",
                                             "The being continues to approach, seemingly marvelling at what it's discovered - you.", "It pauses, and after some time - almost as if it was making a decision - you feel a gentle force against one of your petals.",
                                             "The plan is going well as of yet. Now you just need it to be infatuated with you, to explore dangerously close...", "But it doesn't move on immediately, continuing to caress your petals.", 
                                             "How could it not, with them being so silky?", "Either way, you wonder if it will (explore) the rest of the flower, or (continue) to admire your divine petals."]
                                    
                                    for i, sentence in enumerate(story):
                                        print(sentence)
                                        if i < len(story) - 1:
                                            wait()
                                        else:
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "explore" and choice != "continue":
                                                p("It hasn't made its decision yet, but...")
                                                p("You know for sure that '" + choice + "' isn't going to be one of its options.")
                                                print("Will it (explore) the rest of the flower, or (continue) to admire your divine petals?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "explore": # END
                                                points.confidence(1)
                                                story = ["You're convinced it will move on, and lo and behold it eventually does, though somewhat begrudgingly.", "It continues to trace it's touch down your flower pod, continuing until it reaches the stem.",
                                                         "You feel this movement the whole time, its touch sending odd, rippling shivers along your body.", "But this doesn't hinder your goals.", "In fact, the being's exploration is exactly what you wanted.",
                                                         "After all, you're aware of the poison coursing through the stem of the flowers, as well as the budding thorns itching to dart out and prick the being.",
                                                         "It carries on, unaware of the latent danger and imminent death approaching it.", "It passes its limb over one of the thorns yet to grow, and you instinctively jut it out at blinding speeds, giving it no chance to retract.",
                                                         "You feel the thorn meet resistance, but you persist and it punches through the creature's skin.", "You shoot out the liquid poison into its body, ecstatic at your nearing freedom.",
                                                         "It quickly draws back, but not fast enough.", "You feel it stumble around, its flailing movement sending shockwaves along your roots.", 
                                                         "It swells and swells, the growing of its misery aligned with the surging of your happiness.", "One final shudder ripples through the ground as it seems to burst, its life ending in a dramatic, explosive fashion.",
                                                         "...", "But while its physical body may have died, its soul does not.", "It immediately draws close, it too 'entering' the flowers to join you.", 
                                                         "You feel yourself being pushed out, as if there isn't enough room for two.", "This is it...", "A golden warmth permeates across your senses, and you feel yourself lurch upwards, detaching from the sickly sweet flowers.",
                                                         "Up and up and up you float, leaving behind the mortal coil that kept you captive.", "Your existence peacefully fizzles out, your life coming to an end...", ""]
                                                
                                                for i, sentence in enumerate(story):
                                                    p(sentence)

                                                story = ["...", "Well, that was exciting.", "A moment of innovation from you - what a plan!", "Brilliantly executed no less.", "The real shame is that I can't even pretend this is bad for you.", 
                                                         "It's exactly what you wanted...", "But don't you feel bad?", "Assuming empathy is even a thing in your mind, you've just left that poor existence to the same fate that you were left to.", "Alone and trapped for all eternity.",
                                                         "I mean hell, for all you know, that existence could've been you.", "...", "Anyway, who am I to get all caught up on the ethics of life.", "And what would you care?", "Soon you'll be left a husk of yourself, aware only that..."]
                                                
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
                                                

                                            elif choice == "continue": # DONE
                                                points.confidence(-1)
                                                story = ["Just as you expected, the being continues to marvel at your petals.", "That is until it hesitates, pulling back slightly.", "It stays like that for some time, with what appears to be no intentions to come back.",
                                                         "Does it not find you alluring anymore?", "Has it seen through your trap?", "You realise it must be trying to make a decision.", "As for what decision that is... well, you can only wonder if it will be (beneficial) or (detrimental) for you."]
                                                
                                                for i, sentence in enumerate(story):
                                                    print(sentence)
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        choice = rp(input("> ").lower().strip())

                                                        while choice != "beneficial" and choice != "detrimental":
                                                            p("Once again, a binary decision throws you for a loop.")
                                                            p("You think you'll try again this time. You're sure to be successful... right?")
                                                            print("Alright. (Beneficial) or (detrimental)? You've got this.")
                                                            choice = rp(input("> ").lower().strip())

                                                        if choice == "beneficial": # END
                                                            points.charisma(1)
                                                            story = ["A surge of excitement fills you as you realise it has bad intentions towards you.", "This was exactly what you wanted.", "Perfectly planned, perfectly executed.",
                                                                     "It moves towards you, seeping malice so thick it's palpable.", "Seemingly abandoning all caution, it makes to rip off your petals in a blind rage.", "But your talon-like thorns catch it, poisoning it with evil to match its own.",
                                                                     "Euphoria floods your body as you stare death - and consequently freedom - down.", "You soon feel it start to stumble around, its flailing movement sending shockwaves along your roots.", 
                                                                     "It swells and swells as the toxin courses through its system, the growing of its misery aligned with the surging of your happiness.", "One final shudder ripples through the ground as it seems to burst, its life ending in a dramatic, explosive fashion.",
                                                                     "...", "But while its physical body may have died, its soul does not.", "It immediately draws close, it too 'entering' the flowers to join you.", "You feel yourself being pushed out, as if there isn't enough room for two.",
                                                                     "This is it...", "A golden warmth permeates across your senses, and you feel yourself lurch upwards, detaching from the sickly sweet flowers.", "Up and up and up you float, leaving behind the mortal coil that kept you captive.",
                                                                     "Your existence peacefully fizzles out, your life coming to an end...", ""]
                                                            
                                                            for i, sentence in enumerate(story):
                                                                p(sentence)

                                                            story = ["...", "Wow.", "Just wow.", "That was so exhilarating!", "Bam! Then splat! And finally POW!", "And then it was dead.", "And then you were free.", "And then you were dead.", "And- no. You're still dead.", "But *soon*...", 
                                                                     "Soon you'll be alive again!", "And then dead.", "Then alive again!", "Then dead...", "Man, I'm starting to see how this could get you down...", "But wait!", "You're lucky, you know that?", "No, of course you don't",
                                                                     "You're lucky because you won't remember the ever-repeating cycle of life and death and life again.", "And death again.", "No. Instead, all you'll know is that..."]
                                                            
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
                                                            


                                                        elif choice == "detrimental": # DONE
                                                            points.confidence(-1)
                                                            story = ["You're not brimming with confidence when it comes to this unknown existence.", "After torturous amounts of consideration, it finally moves.",
                                                                     "You feel a flash of happiness as it seems to encapsulate you, aiming to protect you.", "Then, however, you realise this not, in fact, a good thing.", "The opposite, really.",
                                                                     "Your aim was to essentially die, at least this flower version of yourself, and for you to return to your old self.", "But that's much less likely to happen if the existence's sole aim is protection.",
                                                                     "And it doesn't happen.", "Displaying an incredible feat of patience, it becomes an indomitable wall to the passage of time.", "Time itself loses meaning as it hyperfocuses only on your protection.",
                                                                     "After eons of waiting, it begins to flinch every so often, startled by something in its thoughts.", "More and more frequently it does this, being apparently startled for increasing periods of time.",
                                                                     "At some point its moments of surprise blend into one another, then all of a sudden it stops, aware.", "It can... see.", "You don't know how you know this, but it has a... level of sentience it didn't have before.",
                                                                     "It knows what you look like.", "It knows what you're trying to do.", "It backs away slightly, realising your intentions and coming to a decision on what to do with you.",
                                                                     "You wonder if it will (escape) from you, or perhaps - against all you would think - it will (stay)?"]
                                                            
                                                            for i, sentence in enumerate(story):
                                                                print(sentence)
                                                                if i < len(story) - 1:
                                                                    wait()
                                                                else:
                                                                    choice = rp(input("> ").lower().strip())

                                                                    while choice != "escape" and choice != "stay":
                                                                        p("Escape, stay. Stay, escape. " + choice + "? No...")
                                                                        print("(Escape) or (stay), that's for sure.")
                                                                        choice = rp(input("> ").lower().strip())

                                                                    if choice == "escape": # END
                                                                        points.confidence(-1)
                                                                        story = ["Just as you thought, the existence begins to moves away - you feel it through your primitive sense of touch.", "However, it falters.",
                                                                                 "You were right. It can't see anymore.", "After being here for so long, it developed sight, but...", "But now, after leaving, it lost it.", "You give it sight.",
                                                                                 "Without you, it can't see.", "A surge of excitement rushes through you again as you realise it will come back.", "And it does.", 
                                                                                 "It doesn't seem happy about it and takes some time making the decision, but it comes trudging back, it's weight heavy on your network of roots.", "You feel it pause in front of you...",
                                                                                 "So many decisions to make; you wish it would hurry up.", "Eventually it moves towards you, seeping with malice.", "Seemingly abandoning or blind to its past caution, it rips off your petals in desperation to regain its sight.",
                                                                                 "You think it's going to consume you... which would kill it.", "Euphoria flows through you as you stare death and freedom down.", "You feel it stumble around, its flailing movement sending shockwaves along your roots.",
                                                                                 "It swells and swells, the growing of its misery aligned with the surging of your happiness.", "One final shudder ripples through the ground as it seems to burst, its life ending in a dramatic, explosive fashion.",
                                                                                 "...", "But while its physical body may have died, its soul does not.", "It immediately draws close, it too 'entering' the flowers to join you.", "You feel yourself being pushed out, as if there isn't enough room for two.",
                                                                                 "This is it...", "A golden warmth permeates across your senses, and you feel yourself lurch upwards, detaching from the sickly sweet flowers.", "Up and up and up you float, leaving behind the mortal coil that kept you captive.",
                                                                                 "Your existence peacefully fizzles out, your life coming to an end...", ""]
                                                                        
                                                                        for i, sentence in enumerate(story):
                                                                            p(sentence)

                                                                        story = ["...", "Well, that was exciting.", "Your plan went disastrously wrong, and then disastrously right!", "In the end, you win.", "The real shame is that I can't even pretend this is bad for you.", 
                                                                                 "It's exactly what you wanted...", "But don't you feel bad?", "Assuming empathy is even a thing in your mind, you've just left that poor existence to the same fate that you were left to.", "Alone and trapped for all eternity.",
                                                                                 "I mean hell, for all you know, that existence could've been you.", "...", "Anyway, who am I to get all caught up on the ethics of life.", 
                                                                                 "And what would you care?", "Soon you'll be left a husk of yourself, aware only that..."]
                                                                        
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



                                                                    elif choice == "stay": # END
                                                                        points.confidence(1)
                                                                        story = ["It...", "Huh. It decides to stay.", "This is *not* ideal.","This being's persistence is beyond what you would think possible, and it once again turns its attention back to you.", 
                                                                                 "It becomes a statue against time, rigid and unmoving, impassable.", "...", "At some point, a plan hatches within your mind.", "You can grow.", 
                                                                                 "During this past rush of time, all you've done is replenish what you naturally lose, a subconscious process.", "But with a lot of time to ponder, you've realised that you can direct your growth.",
                                                                                 "You hone your thoughts in. Time slows.", "Imperceptibly gradual, you gingerly extend your limbs, forming new parts of yourself to grow.", "Far too much time passes for you to keep track of your efficiency, but you don't care.",
                                                                                 "It's working.", "You cautiously wrap yourself around the being, not yet touching it, but almost grazing it.", "And then, when all is ready, you strike.",
                                                                                 "You constrict your vines, twisting a deathly grip around it, and your vile thorns stab into it.", "You feel it thrash and struggle against your bindings.",
                                                                                 "It swells and swells, the growing of its misery aligned with the surging of your happiness.", "One final shudder ripples through the ground as it seems to burst, its life ending in a dramatic, explosive fashion.",
                                                                                 "Gross...", "But while its physical body may have died, its soul does not.", "It immediately draws close, it too 'entering' the flowers to join you.", "You feel yourself being pushed out, as if there isn't enough room for two.",
                                                                                 "This is it...", "A golden warmth permeates across your senses, and you feel yourself lurch upwards, detaching from the sickly sweet flowers.", "Up and up and up you float, leaving behind the mortal coil that kept you captive.",
                                                                                 "Your existence peacefully fizzles out, your life coming to an end...", ""]
                                                                        
                                                                        for i, sentence in enumerate(story):
                                                                            p(sentence)
                                                                        
                                                                        story = ["...", "Wowsers.", "What a plan!", "Perfectly planned, perfectly executed.", "A real killer, you are.", "I mean, that was just so thrilling to watch.", "Bam! Then splat! And finally POW!", "And then it was dead.", 
                                                                                 "And then you were free.", "And then you were dead.", "And- no. You're still dead.", "But *soon*...", "Soon you'll be alive again!", "And then dead.", "Then alive again!", "Then dead...", 
                                                                                 "Man, I'm starting to see how this could get you down...", "But wait!", "You're lucky, you know that?", "No, of course you don't", "You're lucky because you won't remember the ever-repeating cycle of life and death and life again.", 
                                                                                 "And death again.", "No. Instead, all you'll know is that..."]

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


                                                                        

