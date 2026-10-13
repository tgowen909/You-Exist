# Path: no > body > sounds > bathe

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



story = ["Noise.", "So much noise.", "They almost sound like... voices? As if something is producing them with purpose.", "But they're jumbled.", "Deafening.", 
         "Unintelligible.", "The voices' sheer volume engulfs you.", 
         "At first you feel a surge of panic, and urge to flee from this tempest, this booming mess.", "But frozen with indecision, a part of you is drawn to the voices.",
         "Even though they may not be comprehensible, a strange allure of curiosity tugs at you.", 
         "Your time to decide is running out, the thunderous voices threatening to consume your sense of self.",
         "Should you (run away), or (listen), listen, listen..."]

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "run away" and choice != "listen":
            p("The voices engulf your choice of '" + choice + "', removing all sense of meaning from it.")
            print("All that is able to cross your thoughts are whether or not you should (run away) or (listen).")
            choice = rp(input("> ").lower().strip())

        if choice == "run away": # END
            points.confidence(-1)
            story = ["Paranoia takes an iron grip on your mind, urging you to move.", "Chaos and madness lie on the boundary of your soul and whatever it is making this noise.",
                     "Powered by fear, you run.", "You throw all your might and will into getting away, but nothing you do works.", 
                     "Despite all your efforts, they persist.", "You find yourself dashing, trying to escape the labyrinthine corridors of your own mind.",
                     "But each ‘turn' you take leads you deeper, not out, pulling you into the maelstrom of madness.",
                     "Lost in the voices, you begin to spiral, the line between your thoughts and the voices blurring with each moment that passes.",
                     "You desperately search for a beacon of sanity, anything that could lead you away from this abyss.", "To safety.",
                     "Again, your efforts were in vain.", "Your mind collapses in on itself, and your soul turns to confront your now fractured essence.",
                     "You stare the darkness down.", "Suffocating and oppressive, the darkness stares back.", 
                     "Oblivion looms over you, a final refuge from the torment of noise that has consumed you.",
                     "You embrace it, your sanity wrenched from your grasp as you look on, thoughtless...", ""]
            for i, sentence in enumerate(story):
                p(sentence)
            
            story = ["...", "How dramatic!", "I was not aware you had a taste for the arts.", "How is it that every single time you seem to get yourself into such a mess?",
                     "It's almost impressive!", "Except it's not, because I do in fact have a... minor influence.", "So I'm the impressive one!", "Perfect. Just how I like me.",
                     "But hey, props to you.", "You're always at it with such vigour. All these decisions taken with barely a second thought.", "I admire you, sometimes.", 
                     "When I forget.", "When I remember, well... that's a whole other story.", "Speaking of remembering - you won't.", "No wonder you go at everything like it's the first time.", 
                     "It essentially is, especially when all you know is that..."]
            
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


        elif choice == "listen": # DONE
            points.confidence(1)
            points.insanity(1)
            story = ["You need to listen in...", "As painful as it is, how could you not?", "They pose too much of an interest to you, your new method of experiencing life.",
                     "Maybe these voices have some meaning behind them?", "You ponder on this some more before trying to make sense out of them.",
                     "You push yourself through their brutal attack, desperate to find any implications, their shrieking cries reverberating throughout your entire self.",
                     "Eventually... those sounds... are those patterns?", "Do they have (meaning), or are they (senseless)?"]
            
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    choice = rp(input("> ").lower().strip())

                    while choice != "meaning" and choice != "senseless":
                        p("Nice. You've got for '" + choice + "' instead of the obvious two choice answer.")
                        p("you think you'll just stick to the basics next time.")
                        print("Do you think they have (meaning), or are they (senseless)?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "meaning": # DONE
                        points.ponder(1)
                        points.charisma(1)
                        p("The voices begin to arrange themselves into cohesive groups, no longer a sporadic assault of... noise.")
                        p("They still overlap one another most of the time, but every now and then an individual can be heard...")
                        keyboard_listener.start()
                        tvoices("                     RUN")
                        achievements.Linguist()
                        time.sleep(1.6)
                        tvoices("        please...")
                        time.sleep(1.4)
                        tvoices("                                                           DON'T ASK FOR HELP")
                        time.sleep(1.2)
                        tvoices("            Oh god... not again")
                        time.sleep(1)
                        tvoices("                                                                                                        NOOOOO")
                        time.sleep(0.8)
                        tvoices("                                           BREATHE")
                        time.sleep(0.6)
                        tvoices("Go behind!")
                        time.sleep(0.4)
                        tvoices("                   don't let it fin-")
                        time.sleep(0.3)
                        keyboard_listener.stop()
                        print("The voices get louder and louder, and you wonder if they'll ever stop.")
                        wait()
                        keyboard_silencer.start()
                        print("They're pushing in on your mind, surrounding you as th-")
                        time.sleep(1.7)
                        tvoices("                             We are NOT your friends")
                        time.sleep(0.9)
                        tvoices("                                                        WE KNOW YOU CAN HEAR US")
                        time.sleep(1)
                        keyboard_silencer.stop()
                        p("These voices are really getting on your nerves now, always in the way, making it difficult to think.")
                        p("It's too much for you to bear.")
                        keyboard_stopper.start()
                        print("Maybe you need to ask fo-")
                        time.sleep(0.8)
                        keyboard_stopper.stop()
                        voices("                        Don't eat the flowers!")
                        print("...ask for (help), or GET THESE DAMN VOICES TO (SHUT UP)!")

                        choice = rp(input("> ").lower().strip())

                        while choice != "help" and choice != "shut up":
                            voices("So you're dumb too?")
                            print("Encouraged by the one sensible comment, you realise you desperately need to ask for (help) or get the voices to (shut up).")
                            choice = rp(input("> ").lower().strip())

                        if choice == "help": # DONE
                            points.charisma(1)
                            points.confidence(-1)
                            p("You don't quite know what you're doing, but you need help.")
                            p("You need *help*. Urgently.")
                            p("You call out to whatever will listen.")
                            print("You need ", end="")
                            cprint("HELP", attrs=["bold"])
                            wait()
                            p("")
                            being("...")
                            being("Well look at you. Enjoying ourselves, are we?")
                            p("A new voice enters your awareness, not grating nor soothing, calming yet attention grabbing, not deep nor high, friendly yet authoritative.")
                            p("And no. You are definitely *not* enjoying life.")
                            being("Well, isn't that a shame? I give you all this, and you throw it back in my face.")
                            being("How disdainful.")
                            p("You don't quite understand who this being is or what exactly it is you're doing wrong, but at least the voices have stopped.")
                            being("Very self-centred, once again.") 
                            being("But anyway, you've asked for help, so here I am. Or would you like to take that back?")
                            p("Going back to the voices sounds like an awful plan of attack, so you're content with where you are... for now.")
                            p("Then again... this existence talking to you now doesn't exactly seem very friendly.")
                            print("Perhaps... will you (take back) your call for help, or (accept) the help you've been given?")

                            choice = rp(input("> ").lower().strip())

                            while choice != "take back" and choice != "accept":
                                being("Obviously '" + choice + "' is not the right choice.")
                                cprint("You heard yourself. Are you going to (take back) your request, or shut up and (accept) it?", "red", attrs=["bold", "dark"])
                                choice = rp(input("> ").lower().strip())

                            if choice == "take back": # END
                                points.confidence(-1)
                                points.morality(-1)
                                being("Interesting...")
                                p("The voices slam back into you, their relentless cacophony filling you with searing agony, and your soul is brutally ripped apart instantaneously, dead.")
                                p("")

                                story = ["...", "Ah...", "Back so soon?", "Man, that's funny... real funny...", "Anyway, I suppose you get what you deserve.",
                                         "You make me come all the way out here, and then you send me straight back?", 
                                         "And then I have to come *ALL* the way back again to send your infuriating-ass straight back to the very start again.", "Well, let's just get this over, I'm sick of you.",
                                         "Blah blah blah, some snide remarks about your future and memories, and *wow*, say it with me!", "'You won't remember anything except that...'"]

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
                                


                            elif choice == "accept": # DONE
                                points.confidence(1)
                                points.morality(1)
                                p("You were right. Anything is better than the voices.")
                                being("Oh goody.")
                                being("I'm glad you've come to that conclusion, because I have an offer for you.")
                                being("A deal with the devil, if you will. Cliché, too.")
                                being("But will you hear me out? I wouldn't want you to ‘take back' your request and come running back a corpse, now, would we?")
                                p("The prospect of a deal doesn't sound very enticing, but neither does corpse-hood.")
                                p("A deal it is.")
                                being("Wonderful! Now-")
                                being("You're going to die.")
                                being("I will kill you.")
                                p("So much for avoiding corpse-hood...")
                                being("You've already died so many times. More than can be recalled.")
                                being("But each time you forget, your memories are erased and restored to just to the knowledge that you exist.")
                                being("And you cycle again and again through this merry-go round of life.")
                                being("I've been bored before, killed you before - both justly and unjustly, and tossed with the idea of getting rid of you many a time before.")
                                being("The beauty of it is that you forget each time, can't hold a grudge, can't fear.")
                                being("Yet I never forgot.")
                                being("It didn't feel right, whether by morality's last-minute dash to be your saviour, or simply a cruel perversion of mine to see you unknowingly suffer.")
                                being("So my offer is this: I am willing to eradicate you, or let you go back to normal.")
                                being("If I eradicate you, you'll be permanently gone, forever, never repeating again.")
                                being("You won't exist anymore, even though you wouldn't remember either way.")
                                being("Think of it as a long-term break for your soul's soul.")
                                being("On the other hand, I'll just end the conversation here. No remaining memories, and everything returns to normal.")
                                being("Although either aren't exactly the best outcomes for you, consider it me being nice.")
                                being("A gem in the rough of my misdeeds.")
                                cprint("So choose: (obliteration) or (repetition).", "red", attrs=["bold", "dark"])
                                choice = rp(input("> ").lower().strip())

                                while choice != "obliteration" and choice != "repetition":
                                    being("Funny. Try again.")
                                    cprint("(Obliteration) or (repetition).", "red", attrs=["bold", "dark"])
                                    choice = rp(input("> ").lower().strip())

                                if choice == "obliteration": # END END (Like END end, you die for realsies, game crashes, will have to take you back to the menu)
                                    points.charisma(1)
                                    points.insanity(1)
                                    points.confidence(-1)
                                    points.physicality(-2)
                                    being("Goodbye.")
                                    os.kill(os.getppid(), signal.SIGHUP) ### MAYBE PRINT YOUR FINAL POINT STATISTICS BEFORE CLOSING THE TAB?
                                    
                                elif choice == "repetition": # END
                                    points.ponder(1)
                                    points.physicality(1)
                                    points.confidence(1)
                                    points.insanity(1)
                                    points.charisma(-1)
                                    being("See you soon.")
                                    ending_lines = (int(size.lines)/2)
                                    if ending_lines == 1:
                                        print()
                                        ending_lines -=1
                                    while ending_lines > 1:
                                        print()
                                        time.sleep(0.075)
                                        ending_lines -= 1



                        elif choice == "shut up": # DONE
                            points.charisma(1)
                            points.confidence(1)
                            points.morality(-1)
                            story = ["You shout with all your might, putting all the weight of your existence behind this cry for silence.", "Miraculously... they quieten.",
                                     "Silence.", "Peace.", "...", "You enjoy the silence for a moment, but eventually your mind starts to wander.","Where had those other voices come from?",
                                     "Perhaps they were alive, like you?", "You feel they had to be, given the 'profound' meaning behind their words.", 
                                     "Either way, they were gone now, and you were left alone in the empty silence.", "You don't have to wait long, however.", "Very slowly, new sounds begin to emerge and surround you.", 
                                     "It begins with a dull crackle, a constant supply of muffled snaps encircle you, coming from all directions.",
                                     "Your first instinct is to run, your previous encounter with any sound not ending all too well when you didn't run away.", 
                                     "But after it appeared that no malicious intent was held by the crackling, you began to acclimatise.", "More sounds accumulate.",
                                     "There's the occasional swooshing of things moving past you, blindingly quick.", "Soon, a low, sweeping, undulating tone echoes throughout your existence, its haunting cry seemingly reaching out from an imperceivable distance.", 
                                     "Fear races through your entire self.", "It was so... vast, and powerful. It makes you wonder what could have possibly made such a noise.",
                                     "You face the direction of its source, planning to seek it out, when a shrill and piercing chime rings out from behind you, making you falter.",
                                     "You whirl around to face the other way, baffled again by what could have made the noise.", "A choice now lies ahead of you.", 
                                     "Will you investigate the rumbling (tone) or the shrill (ping)?"]
                            
                            for i, sentence in enumerate(story):
                                print(sentence)
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    choice = rp(input("> ").lower().strip())

                                    while choice != "tone" and choice != "ping":
                                        p("The muted crackle doesn't pose an interest to you, and nor does '" + choice + "'.")
                                        print("The only realistic options for you are the (tone) and the (ping).")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "tone": # DONE
                                        points.ponder(1)
                                        story = ["You move to investigate the low tone, its vastness piquing your curiosity more.", "Or perhaps it was just to get away from whatever the other noise was...", 
                                                 "Either way, you begin to move in the direction you remember hearing it, the quiet swooshing of something rushing past you calls out once more.", 
                                                 "It's... constant, a low whistle as it passes you by.", "As for what it is you're not sure, so for now you accept its whisper as a mystery.", 
                                                 "Eventually, you hear the ping sound out once again behind you, this time considerably quieter and less chilling, further away.", 
                                                 "You continue onwards towards the low tone, hoping you're still moving in the right direction.", 
                                                 "After a stretch of time the behemoth tone sounds out once more, this time dulled and muted, but confirming you have your direction correct.", 
                                                 "You deduce that the body of sound is moving away from you.", "The ping wails out once more, this time considerably quieter, moving away in a similar fashion.", 
                                                 "All its coldness seems to have disappeared, and it sounds almost like a cry... calling out for one last morsel of hope.", 
                                                 "Is it asking for help, perhaps?", "You pause momentarily, but the rumble you were following does not.", 
                                                 "You need to decide quickly whether you'll (attract) the tone's attention or let it go and (answer) the cry for help."]
                                        
                                        for i, sentence in enumerate(story): # DONE
                                            print(sentence)
                                            if i < len(story) - 1:
                                                wait()
                                            else:
                                                choice = rp(input("> ").lower().strip())

                                                while choice != "attract" and choice != "answer":
                                                    p("You don't have the time for '" + choice + "', more distance growing between you and the two sounds with every delay.")
                                                    print("Will you (attract) the tone's attention or let it go and (answer) the cry for help?")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "attract": # END
                                                    points.confidence(1)
                                                    points.charisma(1)
                                                    story = ["You set your back to the ping once more.", 
                                                             "You know calling out to it is a bit of a risk, but after coming to terms with the scale of these sounds, you've been less stricken with fear.",
                                                             "What could possibly go wrong?", "So next time when it calls out, you call back.", "It cuts off.", "Silence ensues, padded only by the familiar ambient crackle.",
                                                             "Now you're left alone, and you feel the fear creeping up behind you once again.", "Dashes of noise grow ever closer, but their exact location obfuscated, changing.",
                                                             "It's closing in.", "You hear a gargantuan body circle you, the familiar swooshing boxing you in.",
                                                             "For a split second you hear it right next to you, cut off as your body is painfully crushed to smithereens, consumed by the unknown mammoth being.", ""]
                                                    
                                                    for i, sentence in enumerate(story):
                                                        p(sentence)
                                                    
                                                    story = ["...", "Wow, that looked... painful.", "Nasty way to go, if you ask me.", "You know, I was a whale once.", "Pretty boring.",
                                                             "OH! Not whale derogatory.", "Whale the creature.", "Anyway, guess how long I was a whale for?", "...", "...", "Damn, you're boring.", 
                                                             "A whole five minutes!", "Ah, good times...", "Right, sorry, I just had to go down memory lane for a moment.", "Your memory lane, however...",
                                                             "Well, it's pretty short."]
                                                    
                                                    for i, sentence in enumerate(story):
                                                        being(sentence)

                                                    cprint("It's what, " + str(math.floor(int(os.environ['LINES'])/2)) + " lines of text?", "red", attrs=["bold", "dark"])
                                                    wait()

                                                    story= ["And soon it will be all gone!", "Back to square one, as per usual.", "I wonder if you're going to get sick of that one sentence.",
                                                            "What was it again?", "Oh, that's right! It was..."]
                                                    
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


                                                elif choice == "answer": # END
                                                    points.morality(1)
                                                    points.charisma(-1)
                                                    story = ["You decide to let the tone go, it can wait for later.", "It clearly didn't want you to chase it anyway, or so you think.",
                                                             "The ping however, seems like it needs assistance.", "As for how you're going to help, well...", "That can be determined later.",
                                                             "With your mind made up, you begin to move towards the direction you last heard it.", "It wails once more, but this time... it's louder.", 
                                                             "You're getting closer.", "The pings resonate somewhat frequently, each time sounding more intensely, closer still.",
                                                             "Soon after you wonder how it could come any closer, they stop.", "Silence, bar the ever-familiar ambience of the crackling.",
                                                             "You had since stopped moving, letting it approach you - but now you aren't sure where it is.", "All of a sudden your heroic plan looks not all that well thought through.",
                                                             "The harsh tones of mechanical grinding suddenly reverberate around you, their grating sound making you cower.", "What could have possibly made that awful, rough sound?",
                                                             "And it's so close, almost on top of you.", "Just as your thoughts flicker to this *thing's* potential malice, a terrible cacophony of discordant frequencies converges into a single, unbearable shriek of sound.",
                                                             "It resounds with a primal fury, relentless dissonance so palpable it fills you with searing agony, terror and despair rushing to confront you from deep within.",
                                                             "Paralysed, helpless, your soul is ripped to shreds.", ""]
                                                    
                                                    for i, sentence in enumerate(story):
                                                        p(sentence)

                                                    story = ["...", "Huh.", "That's the power of technology right there.", "But seriously, you drew the short straw this time round.",
                                                            "I mean, no matter what you chose, you'd die!", "Crazy how that works.", "I wonder who chose to make it that way...", 
                                                            "Oh that's right!", "I did.", "Absolutely fooled you.", "And on that bombshell, it's time to say goodbye.",
                                                            "I'm sure neither of us will have to wait very long to meet again..."]

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
                                        


                                    elif choice == "ping": # END
                                        points.confidence(1)
                                        story = ["The ping, scary as it is, triggers something deep inside you.", "You begin to move towards the direction you last heard it, upon which the tinny ring wails out once more.",
                                                 "But this time... it's louder. Closer.", "The pings resonate somewhat frequently, each time sounding more intensely, closer still.",
                                                 "Soon after you wonder how it could come any closer, they stop.", "Silence, bar the ever-familiar ambience of the crackling.",
                                                 "You had since stopped moving, letting it approach you - but now you aren't sure where it is.",
                                                 "The harsh tones of mechanical grinding suddenly reverberate around you, their grating sound making you cower.", "What could have possibly made that awful, rough sound?",
                                                 "And it's so close, almost on top of you.", "Just as your thoughts flicker to this *thing's* potential malice, a terrible cacophony of discordant frequencies converges into a single, unbearable shriek of sound.",
                                                 "It resounds with a primal fury, relentless dissonance so palpable it fills you with searing agony, terror and despair rushing to confront you from deep within.",
                                                 "Paralysed, helpless, your soul is ripped to shreds.", ""]
                                        
                                        for i, sentence in enumerate(story):
                                            p(sentence)

                                        story = ["...", "Huh.", "That's the power of technology right there.", "But seriously, you drew the short straw this time round.",
                                                 "I mean, no matter what you chose, you'd die!", "Crazy how that works.", "I wonder who chose to make it that way...", 
                                                 "Oh that's right!", "I did.", "Absolutely fooled you.", "And on that bombshell, it's time to say goodbye.",
                                                 "I'm sure neither of us will have to wait very long to meet again..."]

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



                    elif choice == "senseless": # DONE
                        points.ponder(-1)
                        points.charisma(-1)
                        story = ["No, no... of course not. How could sounds have meaning? Wobbly noise is just that - wobbly noise.", "Maybe you could serenade these people too, wobble back at them!", 
                                 "You begin to make noise, forming scribbles with your voice.", "Louder and louder, you grow your shouts to match the tumultuous cadence of those around you.",
                                 "But it's too loud.", "It assaults your soul, tearing at the edges of your sanity.", "You feel your own thoughts getting further away and yet... still close.", 
                                 "Agonising pain sets in as your mind splits, ripping into pieces.", "Your heightened pain is matched by a rise in pitch and volume of your bellow, and you screech as it reaches a tipping point.", ""]
                        
                        for i, sentence in enumerate(story):
                            p(sentence)

                        centre("...")
                        centre("The voices fall silent.")
                        v2("At last, some peace.", "Finally, some peace.")
                        v2("As you calm, you sit in silence for a time, enjoying the quiet.", "You feel as if you deserve this peace you now have.")
                        centre("Observing the lack of noise, you sense a pervasive uneasiness within yourself.")
                        centre("You feel... conflicting impulses for almost every thought you feel.")
                        v2("It's as if some part of you is trying to provide an alternative to your thoughts.", "It's as if some part of you has it all backwards, thinking all the wrong things.")
                        v2("Everything you think, you think twice.", "Everything you think, there's a right thought and a wrong one.")
                        v2("There's something wrong with this... it's all off.", "Something's very off about this - you're not in control of even your own thoughts!")
                        v2("You believe... you can unify your thoughts.", "You need to be in control again. This can't continue.")
                        v2no_wait("Will you try to (heal) yourself and bring your warring sides together?", "Will you (dispose) of the other half of your mind?")
                        choice = rp(input("> ").lower().strip())

                        while choice != "heal" and choice != "dispose":
                            centre("These clashing thoughts are making it difficult to decide.")
                            centre("However, you don't believe it made you think of '" + choice + "'.")
                            v2no_wait("Will you try to (heal) yourself and bring your warring sides together?", "Will you (dispose) of the other half of your mind?")
                            choice = rp(input("> ").lower().strip())

                        if choice == "heal": # END
                            points.physicality(1)
                            points.morality(1)
                            points.charisma(-1)
                            v2("Despite some sensed hesitation, you're glad you've decided to heal yourself.", "Oh, fuck off. This is not what you wanted.")
                            v2("You don't exactly know how, but you're going to try.", "You try and resist, but there's nothing you can do.")
                            v2("Slowly but surely, you begin to weave your disjointed halves back together.", "You feel your mind being forced back into one against your will.")
                            v2("Your mind unifies, and...", "...and you're whole once more.")
                            centre("Immediately, the crazed voices start up again, this time with doubled vigour, crashing into your recently mended mind and soul in a cacophonous barrage.")
                            centre("You feel yourself being torn again, your soul and mind being brutally cleaved to pieces.")
                            centre("But it's not just in two this time. It's hundreds.")
                            centre("Thousands.")
                            centre("You struggle to comprehend both the pain and magnitude of destruction occurring right within your very mind, brought on by the vicious onslaught of the voices.")
                            centre("Luckily, you don't have to attempt to understand for very long, as your sanity is soon obliterated by thousands of iterations of yourself, and all goes dark.")
                            p("")
                            story = ["...", "Hey, that was pretty cool!", "There was two of you!", "And there was thousands at the end too, but well...", "That was less cool.", "Unoriginal.",
                                     "Hang on, hang on, Let me give it a try...", "..."]
                            
                            for i, sentence in enumerate(story):
                                being(sentence)

                            v2being("How's this?", "Look at me go!")
                            v2being("I hate you.", "Eh, you're manageable.")
                            v2being("I'm pretty awesome.", "Yup, no conflicting thoughts there.")
                            v2being("...", "...")
                            being("Eugh. That's weird.")
                            being("No wonder you died quickly, that's quite a lot of mental strain.")
                            being("Do know what isn't a strain on the mind?")
                            being("Not remembering anything.")
                            being("And I think you and I know where this is going.")
                            being("It can't be *that* hard only knowing that...")
                            ending_lines = (int(size.lines)/2)
                            if ending_lines == 1:
                                print()
                                ending_lines -=1
                            while ending_lines > 1:
                                print()
                                time.sleep(0.075)
                                ending_lines -= 1



                        elif choice == "dispose": # END
                            points.charisma(1)
                            points.physicality(-1)
                            points.morality(-1)
                            v2("You're unsure why, but you turn your attention inwards... with malice?", "You firmly believe this will solve all identity-related problems. You're invested now.")
                            v2("This was definitely not what you had in mind.", "This was definitely what you had in mind.")
                            v2("You feel as if you're being kicked out, thoughts separated from soul.", "You feel space freeing up, the other half of you being exterminated.")
                            v2("You're torn further away from what you believed you had control of, dying...", "You stand your ground further, barging the old you out until finally...")
                            centre("Ow.")
                            p("")
                            story = ["...", "Hey, that was pretty cool!", "There was two of you!", "And there was thousands at the end too, but well...", "That was less cool.", "Unoriginal.",
                                     "Hang on, hang on, Let me give it a try...", "..."]
                            
                            for i, sentence in enumerate(story):
                                being(sentence)

                            v2being("How's this?", "Look at me go!")
                            v2being("I hate you.", "Eh, you're manageable.")
                            v2being("I'm pretty awesome.", "Yup, no conflicting thoughts there.")
                            v2being("...", "...")
                            being("Eugh. That's weird.")
                            being("No wonder you died quickly, that's quite a lot of mental strain.")
                            being("Not to mention that you hated your other half...")
                            being("But anyway, do know what isn't a strain on the mind?")
                            being("Not remembering anything.")
                            being("And I think you and I know where this is going.")
                            being("It can't be *that* hard only knowing that...")
                            ending_lines = (int(size.lines)/2)
                            if ending_lines == 1:
                                print()
                                ending_lines -=1
                            while ending_lines > 1:
                                print()
                                time.sleep(0.075)
                                ending_lines -= 1

                            

