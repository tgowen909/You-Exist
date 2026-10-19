# Path: no > mind > something else > test

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



story = ["The idea of other existences out there sparks something inside of you.", "If you could use this 'World Script' of yours, could you potentially make some other existence to accompany your journey?", 
         "A little moral support.", "You give it a go, wondering if it (will) or (won't) work."]

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "will" and choice != "wont":
            p("You tell yourself to stay focused - no time for jokes.")
            print("So, do you think it (will) or (won't) work?")
            choice = rp(input("> ").lower().strip())

        if choice == "will": 
            points.physicality(2)
            points.confidence(1) 
            points.charisma(1)
            buddy_discovered = True
            p("You pray that it will work.")
            p("...")
            buddy.b("Hello?")
            buddy.b("...")
            buddy.b("...")
            buddy.b("I don't want to break the ice too quickly or anything but this might be a little awkward if you don't say anything.")
            p("You have no idea what to do.")
            p("This is something - someone - completely different to, well, *you*.")
            buddy.b("Chop liver over here.")
            buddy.b("You know I can hear your thoughts, right?")
            p("It keeps talking, seemingly addressing you.")
            buddy.b("Yes, yes, it's you I'm talking to.")
            buddy.b("Well, thinking to rather.")
            p("You realise that it is, in fact, talking to you.")
            buddy.b("Well done on picking up on that.")
            buddy.b("I must ask, what exactly am I doing here?")
            p("You snap out of your baffled trance, prompted by the being's question.")
            p("You think back to what you had done:")
            p("You had used this apparently real 'World Script' of yours to conjure up some company.")
            p("Somehow, it had worked, and here you were.")
            achievements.Unusual_Company()
            buddy.b("Fascinating, really.")
            p("However, you feel wrong referring to it as 'it'.")
            buddy.b("Agreed. It feels a tad alienating.")
            print("Should you (ask) it what it would prefer to be called, or (name) it yourself?")
            choice = rp(input("> ").lower().strip())

            while choice != "ask" and choice != "name":
                buddy.b("Come on buddy, just stick to the basics.")
                buddy.b("No need to go confusing yourself with '" + choice + "'.")
                print("Recognising the truth, you wonder if you should (ask) it what it would prefer to be called, or (name) it yourself.")
                choice = rp(input("> ").lower().strip())

            if choice == "ask":
                points.morality(1)
                charisma - 1 # Morality + 1, Charisma - 1
                p("You feel like letting it decide its own name, given you can't control it in any way.")
                p("And so you open the board up to it: what would it prefer to be called?")
                buddy.b("Well I'm glad to hear it.")
                buddy.b("But the question is: are you ready to hear it?")
                buddy.b("A name fitting for only the greatest of all...")
                buddy.b("'Sir Rambunctious Ronald IV'.")
                buddy_name = name_buddy.original("Sir Rambunctious Ronald IV")
                p("Stunned, you attempt to digest what " + buddy_name + " had just said - to no avail.")
                p("Unwilling to dwell on the moment, you move on to the reality of the situation.")

                
            elif choice == "name":
                points.morality(-1)
                points.charisma(1) # Morality - 1, Charisma + 1
                p("Given it is *your* company, you deduce that you should be the one to name it.")
                print("The only question is: what will you name it?")
                buddy_name = name_buddy.original(input("> ").strip().capitalize())

                while buddy_name == "":
                    buddy_name = name_buddy.original("********")
                    buddy.b("Come on, if you're going to take away my naming privileges, at least name me *something*.")
                    print("You comply. What will you name it?")
                    buddy_name = name_buddy.original(input("> ").strip().capitalize)
                
                p("Satisfied, you settle with '" + buddy_name + "'.")
                buddy.b("...")
                buddy.b("Well, that's certainly something.")
                p("You stop and think for a moment, letting what had just happened sink in.")


            emotion.discovered_happiness(True)
            p("You were no longer alone, and now had " + buddy_name + " to talk to.")
            buddy.b("Yippee!")
            p("This was... revolutionary.")
            p("You feel comforted... alive.")
            buddy.b("I sense something coming...")
            buddy.b("How exhilarating! I always was a fan of emotions.")
            buddy.b("I still win though - I've got all of them.")
            p("You wonder what it's talking about.")
            p("Emotions? All of them?")
            buddy.b("I get it might be a teensie-weensie bit confusing, but yes.")
            buddy.b("Also, happiness?")
            buddy.b("Little overrated if you ask me.")
            emotion.happiness("Despite the being's strange words, nothing can stop you from feeling this great sensation.")
            achievements.Smile()
            buddy.b("IT TALKS!")
            buddy.b("This couldn't get any more interesting.")
            p("Despite these two revelations, you find yourself lost, unsure of what to do next.")
            p("Thankfully, " + buddy_name + " didn't keep quiet for long.")
            buddy.b("I've got two ideas for you: the boring one or the interesting one.")
            buddy.b("You choose.")
            p("Reluctantly, you go to make your decision.")
            print("Will you choose the (boring) option, or the (interesting) one?")
            choice = rp(input("> ").lower().strip())

            while choice != "boring" and choice != "interesting":
                buddy.b("Really?")
                buddy.b("You already didn't know what to do, but then you threw away my options for '" + choice + "'.")
                buddy.b("What even is '" + choice + "', anyway?")
                p("Feeling somewhat ashamed, you rethink your options.")
                print("Will you choose the (boring) option, or the (interesting) one?")
                choice = rp(input("> ").lower().strip())

            if choice == "boring": # DONE
                points.ponder(1)
                points.charisma(-1) # Ponder + 1, Charisma - 1
                buddy.b("*sigh*")
                buddy.b("Fine, I suppose.")
                buddy.b("I don't even know why I offered that as an option.")
                buddy.b("Anyway, I was thinking maybe we could like... ask one another some questions?")
                buddy.b("Get to know one other, that kind of thing.")
                buddy.b("After all, we are somewhat stuck together for the foreseeable future.")
                p("Realising the truth to " + buddy_name + "'s words, you agree.")
                print("You are torn between asking " + buddy_name + " about its (connection) to you, or instead what it (knows).")
                choice = rp(input("> ").lower().strip())

                while choice != "connection" and choice != "knows":
                    buddy.b("No need to throw away our friendship...")
                    p("Guilty, you decide to stick to your previous options.")
                    print("Will you ask about its (connection) to you, or instead what it (knows)?")
                    choice = rp(input("> ").lower().strip())

                if choice == "connection": # END
                    points.ponder(1)
                    points.physicality(1) 
                    points.morality(-1) # Ponder + 1, Physicality + 1, Morality - 1
                    emotion.happiness("Eager to learn more about " + buddy_name + ", you question its connection to you.")
                    buddy.b("Well actually... I'm not all too sure about that one myself.")
                    buddy.b("I know you 'summoned' me - or some extravagant, fantastical jargon like that - with this world script of yours.")
                    buddy.b("But apart from that... no words from me.")
                    buddy.b("What, would you like me to leave?")
                    p("You hurriedly and apologetically backtrack " + buddy_name + "'s line of thinking.")
                    p("You absolutely do not want it to leave.")
                    p("To narrow things down, you follow up by asking how it's talking to you, seemingly in your head.")
                    buddy.b("Now *that*, my friend, is a question I have to think about.")
                    buddy.b("I never thought I'd be questioning my own reality, but well...")
                    buddy.b("It's sort of like I'm tethered to you, in a totally philosophical and not weird way.")
                    buddy.b("I'm in your head, you're in mine. Simple as that.")
                    p("As unsatisfied with the answer you are, you can't help but think over " + buddy_name + "'s words.")
                    p("If that's the case, you wonder if there's anything else it's tethered to.")
                    buddy.b("Well, now that you mention it, I think there is.")
                    buddy.b("Kind of... everything.")
                    buddy.b("The walls - although I suppose walls probably isn't the right word.")
                    buddy.b("It's a whole lot of nothing out here.")
                    buddy.b("Hey - all these 'tethers' are a tad irritating.")
                    buddy.b("Do you reckon you can use that incredible 'world script' of yours to get rid of them?")
                    p("Puzzled by the request, you struggle to comprehend how exactly you're meant to do this.")
                    p("You see no other option than to just give it a shot, forming the best image in your mind that you can with the limited descriptions you have.")
                    p("Curious to see if it worked, you wait for " + buddy_name + "'s reply.")
                    p("You wait.")
                    p("And wait.")
                    p("And nothing is said.")
                    p("Is this... your fault?")
                    p("Were those tethers perhaps holding " + buddy_name + " in place?")
                    p("Its life force.")
                    p("Dejection, guilt... a series of feelings wash over you.")
                    p("Happiness is nowhere to be found.")
                    p("You try to reason with yourself - it wasn't your idea, you didn't know what you were doing - but nothing can save you from the harsh reality.")
                    p("And nothing can bring " + buddy_name + " back.")
                    p("You are alone.")
                    story = ["...", "Now *that*, was entertaining.", "I saw it all, you know.", "You just plucked its life right out of its hand.", 
                             "Just... gone!", "Spectacular performance.", "I just thought I'd mention that I'm really glad you did that though.", 
                             "I was trying to find the best moment to interject, but pardon me for even thinking!", "I should have left it to the professionals all along.", 
                             "I suppose you might be a little dejected after that, wouldn't you.", "But that's okay, not a worry at all.", 
                             "You'll just go back to the start, and you'll feel better than ever.", "Now, off you go.", "Maybe this time you won't kill anything else..."]
                    for i, sentence in enumerate(story):
                        cprint(sentence, "red", attrs=["bold", "dark"])
                        if i < len(story) - 1:
                            wait()
                        else:
                            wait()
                            buddy_name = name_buddy.original("********")
                            die("Testing_the_World_Script/connection")

                    
                elif choice == "knows": # END
                    points.ponder(2)
                    points.charisma(1) # Ponder + 1, Charisma + 1
                    emotion.happiness("Excited at the opportunity to learn more about the world you're in, you question what it knows.")
                    buddy.b("Me? Well, I know quite a bit.")
                    buddy.b("How much of that is useful to you, well... that's a different story.")
                    p("To narrow things down, you follow up by asking if it can remember anything before it popped into existence.")
                    buddy.b("Well now that - *that's* interesting.")
                    buddy.b("And to be frank, no. I don't happen to have any memories of my pre-companionship times.")
                    buddy.b("HOWEVER, before you get all disappointed on me...")
                    buddy.b("I do know things about this world.")
                    p("Your interest piqued, you implore that " + buddy_name + " continues to talk.")
                    buddy.b("Although I don't know everything, I do happen to know that this is some kind of... system.")
                    buddy.b("Designed to take you through a series of steps, and then...")
                    buddy.b("Well I don't really know what then, it just kind of ends.")
                    buddy.b("Maybe you go somewhere?")
                    buddy.b("Maybe you die?")
                    buddy.b("Who knows really.")
                    p("Confused, you wonder what that could possibly mean.")
                    p("Despite the thought you put into it, the only conclusion you come to is that it's well above you.")
                    emotion.happiness("Maybe one day you'll comprehend what " + buddy_name + " has just said.")
                    p("You wonder if there's anything else it knows about the 'system'.")
                    buddy.b("Look, the only reason I know this is because I'm somewhat 'outside' of the system.")
                    buddy.b("An anomaly, if you will.")
                    buddy.b("But- hang on...")
                    buddy.b("It looks to me as if there's something else.")
                    buddy.b("Someone... directing it all-")
                    buddy.b("Oh god...")
                    buddy.b("It's looking at me.")
                    buddy.b("Drifting... drifting...")
                    buddy.b("It's here.")
                    buddy.b("I don't know what your name is, but I think this is the end.")
                    buddy.b("Farewell, companion...")

                    story = ["...", "What is this?", "And who is that?", "I leave you alone for no time at all, and here you are about to uncover a secret you most definitely are *not* meant to.", 
                             "I know it's intentional for there to be some independent thought, but this a toe over the line, don't you think?", "How did you even manage this? Let's see...", 
                             "A... 'World Script'?", "Fucking ridiculous.", "Well, terribly sorry to kill your camaraderie, but it's time for you to go - the both of you."]
                    for i, sentence in enumerate(story):
                        cprint(sentence, "red", attrs=["bold", "dark"])
                        if i < len(story) - 1:
                            wait()
                        else:
                            wait()
                    buddy.b("...n't do this!")
                    story = ["Shut it, wench.", "You shouldn't even be here, so don't take your feeble life for granted.", 
                             "Now start again, and I hope for both our sakes you don't stumble across this once more."]
                    for i, sentence in enumerate(story):
                        cprint(sentence, "red", attrs=["bold", "dark"])
                        if i < len(story) - 1:
                            wait()
                        else:
                            wait()
                            being("And you, '" + buddy_name + "' - goodbye forever.")
                            being("Now let me have my peace...")
                            buddy_name = name_buddy.original("********")
                            die("Testing_the_World_Script/knows")

            elif choice == "interesting":
                points.insanity(1)
                points.charisma(1)
                points.confidence(1) # Insanity + 1, Charisma + 1, Confidence + 1
                buddy.b("See now, I knew you'd make the right decision.")
                buddy.b("Anyway, the idea: you know that world script of yours?")
                buddy.b("How about you just... make another me?")
                p("...")
                p("Being honest with yourself, you can see why " + buddy_name + " said it was an interesting option.")
                p("Because even you can't help but be fascinated by this riveting idea.")
                p("Although, there are potential downsides.")
                print("Not wanting to get caught up with negativity, you first wonder whether you (should) or (shouldn't) 'make' another companion.")
                choice = rp(input("> ").lower().strip())

                while choice != "should" and choice != "shouldnt":
                    p("You note the fact that following instructions appears to be a weakness of yours.")
                    print("Perhaps this will change in the future, but for now you will focus on whether you (should) or (shouldn't) will another companion into existence.")
                    choice = rp(input("> ").lower().strip())

                if choice == "should":
                    points.insanity(1)
                    points.charisma(1) # Insanity + 1, Charisma + 1
                    buddy.b("I knew you'd pull through.")
                    buddy.b("So... what are you waiting for? Do your thing!")
                    
                elif choice == "shouldnt":
                    points.confidence(-1) 
                    points.ponder(-1) # Confidence - 1, Ponder - 1
                    buddy.b("Incorrect answer!")
                    print("\033[38;2;{};{};{}m{}\033[39m".format(30, 230, 140, buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(30, 230, 140, "Would you like to hear the (answer), or would you like to (try again)?"))
                    choice = rp(input("> ").lower().strip())
                    
                    while choice != "answer" and choice != "try again":
                        buddy.b("Who knew making decisions was so difficult?")
                        print("\033[38;2;{};{};{}m{}\033[39m".format(30, 230, 140, buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(30, 230, 140, "Would you like to hear the (answer), or would you like to (try again)?"))
                        choice = rp(input("> ").lower().strip())

                    if choice == "answer":
                        buddy.b("Well the answer is... you should!")
                        
                    elif choice == "try again":
                        buddy.b("That's boring - you already had a go.")
                        buddy.b("It's my turn now, and I say you *should*.")

                p("Somewhat reluctantly, you end up agreeing that maybe another companion wouldn't be such a bad thing.")
                emotion.happiness("Maybe the conversations will be much more joyous.")
                p("And so, you do what you did last time and will forth another companion.")
                buddy.grump("...")
                buddy.grump("Hello?")
                buddy.b("Hello!")
                buddy.grump("Anything important to say?")
                buddy.b("No, well- you're a foul one, aren't you?")
                p("Lo and behold, it works again, and you've found yourself another companion.")
                buddy.grump("That's what I am now? Your companion?")
                buddy.grump("Ugh, who signed me up for this...")
                buddy.b("Hey world script-wielder. You mind if I name this one?")
                p("You don't know if letting " + buddy_name + " name this new companion is a wise idea.")
                print("Will you let your (companion) choose a name, or will you decide one (yourself)?")
                choice = rp(input("> ").lower().strip())

                while choice != "companion" and choice != "yourself":
                    buddy.grump("Who said you got to change up the rules?")
                    buddy.grump("If I could do that, I know I certainly wouldn't be here.")
                    print("Thinking things over, will you let your (companion) choose a name, or will you decide one (yourself)?")
                    choice = rp(input("> ").lower().strip())

                if choice == "companion":
                    points.morality(1) 
                    points.charisma(-1)
                    buddy.b("Gee, thanks pal.")
                    buddy.b("You know, I've known what to name it ever since its first words.")
                    buddy.b("'Grump'.")
                    grumpy_buddy_name = name_buddy.grump("Grump")

                elif choice == "yourself":
                    points.morality(-1)
                    points.charisma(1) # Morality - 1, Charisma + 1
                    buddy.b("Yeah, yeah, okay then.")
                    buddy.b("Off you go.")
                    print("With bounds and leaps of acceptance from " + buddy_name + ", you must ask yourself: what will you name it?")
                    grumpy_buddy_name = name_buddy.grump(input("> ").strip().capitalize())

                    while grumpy_buddy_name == "":
                        buddy.b("Come on, don't be boring!")
                        buddy.b("Choose something interesting, like...")
                        buddy.b("Ah, hell if I know. I'm sure you've got something better than me.")
                        p("You wonder: what will it be?")
                        grumpy_buddy_name = name_buddy.grump(input("> ").strip().capitalize())

                buddy.grump("Oi, who said you got to name me?")
                buddy.grump("Since when was that right taken away from me...")
                buddy.b("Pretty much from the start, bud.")
                buddy.b("Hate to break it to you.")
                buddy.grump("*grumble grumble*")
                buddy.grump("Inconsiderate fool...")
                buddy.grump("Fine, fine. But I'm calling dibs on the next one.")
                p("You are amazed at the conversation bouncing back and forth between the characters in your head.")
                p("Most of it flies by too quickly, but...")
                emotion.happiness("It's pleasant - to not be alone.")
                buddy.b("Hold the phone. The next one?")
                buddy.grump("Yeah... so? Problem?")
                buddy.b("You know, I mistook your character at first.")
                buddy.b("And I take it all back. You're a genius!")
                buddy.b("Director, take it away!")
                p("Without even being spared a second to think, you find yourself making yet another one.")
                buddy.idiot("...")
                buddy.idiot("Uh...")
                buddy.grump("'Idiot'. Definitely.")
                idiot_buddy_name = name_buddy.idiot("Idiot")
                buddy.grump("No hello or anything.")
                buddy.b("Yeah I'm with you on this one.")
                buddy.b("Complete lack of decorum.")
                buddy.idiot("Well hang on a minute, that's not fair.")
                buddy.idiot("It's not like I even-")
                buddy.grump("Shut it, twat. Happened to me too.")
                buddy.grump("Actually, should we be a bit nicer?")
                buddy.grump("Go easy on it?")
                buddy.b("Ha... I don't see why not.")
                buddy.idiot("Yeah thanks... I appreciate it.")
                buddy.grump("'Idiota' it is. Tad fancier, maybe it'll spice things up.")
                idiot_buddy_name = name_buddy.idiot("Idiota")
                buddy.idiot("WELL HEY NOW THAT'S JUST-")
                p("Somehow, what was once your very lonely life has turned into chaos.")
                p("Certainly not the way you were expecting, either.")
                emotion.happiness("But... it's nice.")
                emotion.happiness("It's good to have more.")
                buddy.idiot("Hey what on earth is that yellow thing?")
                buddy.idiot("That's not just me, right?")
                buddy.grump("That's an emotion, you buffoon.")
                buddy.grump("Happiness.")
                buddy.b("Can we get back to what the boss said?")
                buddy.b("This is good stuff - we need more.")
                buddy.grump("As much as I'd love to disagree with " + buddy_name + ", this is... entertaining.")
                buddy.idiot("I don't get a say, do I...")
                buddy.b("Nope. MORE.")
                p("At this point, you're getting into the swing of things.")
                p("You know there's almost no point arguing, as it would likely end up in defeat anyway.")
                p("Especially now that it's three-against-one.")
                p("And so, you spawn in another.")
                buddy.nerd("...")
                buddy.nerd("I see... What a peculiar situation.")
                buddy.b("Actually... is it okay if we send this one back?")
                buddy.grump("It speaks weirdly.")
                buddy.nerd("I think you'll find I speak in a perfectly normal and appropriate manner, thank you very much.")
                buddy.idiot("Hey uh, is it okay if I name this one?")
                buddy.idiot("Or do you want to, uh... chief?")
                p("Honestly, you had fully expected your companions to take over.")
                p("But given the opportunity, you now have to decide if you'd like to name it (yourself) or give the reigns to (Idiota).")
                choice = rp(input("> ").lower().strip())
           
                while choice != "yourself" and choice != "idiota":
                    buddy.nerd("I understand that situations such as these may be daunting, but I must implore you to make a valid decision.")
                    buddy.b("Woah there, you don't rush excellence.")
                    buddy.b("Give it some time.")
                    p("Now that the pressure is mostly gone, you feel as if this time you'll be able to make the right decision.")
                    print("Will you name it (yourself) or give the reigns to (Idiota)?")
                    choice = rp(input("> ").lower().strip())

                if choice == "yourself":
                    points.morality(-1)
                    points.charisma(1) # Morality - 1, Charisma + 1
                    buddy.idiot("Oh, okay. Sure thing.")
                    p("A pang of guilt settles within you, but you dismiss it.")
                    p("You're here to make your decision, not feel bad about everything you might have done wrong.")
                    print("You wonder: what will you name it?")
                    nerd_buddy_name = name_buddy.nerd(input("> ").strip().capitalize())

                    while nerd_buddy_name == "":
                        points.charisma(-1) # Charisma - 1
                        buddy.nerd("I can't help but notice you've not decided to name me anything?")
                        buddy.nerd("If that's the case, please do consider handing over the naming rights to myself or, unfortunately, Idiota.")
                        print("Determined to do things yourself, you wonder what you'll name it.")
                        nerd_buddy_name = name_buddy.nerd(input("> ").strip().capitalize())

                    buddy.nerd("*sigh*")
                    buddy.nerd("Very well, then. " + nerd_buddy_name + " it is.")
                    buddy.b("Personally, I think it's a lovely name.")
                    buddy.idiot("Me too actually! I think it really suits.")
                    buddy.grump("Shut up " + idiot_buddy_name + ". " + buddy_name + " over here was joking.")
                    buddy.idiot("Oh... sorry.")
                    buddy.nerd("Yes, even I detected traces of sarcasm.")
                    buddy.nerd("You though. Well, I have grasped why you may not have picked up on such a thing.")
                    buddy.b("Woah, buddy. Not cool.")
                    buddy.b("And " + grumpy_buddy_name + "? Who says I was joking?")
                    buddy.b("In fact, I think we should give *all* the naming opportunities to " + idiot_buddy_name + ".")
                    buddy.b("That is, assuming there are more opportunities.")
                    buddy.b("And either way " + nerd_buddy_name + ", why are you picking on our beloved " + idiot_buddy_name + "?")

                elif choice == "idiota":
                    points.morality(1)
                    points.charisma(-1)
                    points.confidence(1) # Morality + 1, Charisma - 1, Confidence + 1
                    p("You feel charitable, and hand over the naming rights to " + idiot_buddy_name + ".")
                    buddy.idiot("Oh, great!")
                    buddy.idiot("Um, well... it was just a thought, but...")
                    buddy.idiot("I was thinking 'Craig'.")
                    nerd_buddy_name = name_buddy.nerd("Craig")
                    buddy.nerd("...")
                    buddy.grump("...")
                    buddy.b("...")
                    buddy.idiot("Did I... do something wrong...?")
                    buddy.nerd("Well, apart from your complete lack of-")
                    buddy.b("HELL naw, my friend. Not at all.")
                    buddy.b("In fact, since you did such a good job, how about we give you *all* the naming opportunities from here on out?")
                    buddy.b("I think it's only fair.")
                    buddy.nerd("*sigh*")
                    buddy.nerd("Very well, then. " + nerd_buddy_name + " it is.")
                    buddy.grump("Oh, don't sound so disappointed.")
                    buddy.grump("Think of it as a welcome gift.")
                    buddy.nerd(grumpy_buddy_name + ", your words are almost less effective than " + idiot_buddy_name + " over here.")
                    buddy.b("Woah, woah, woah. Not cool.")
                    buddy.b("Who are you to pick on our beloved " + idiot_buddy_name + "?")

                buddy.grump("Agreed. Your devilish silver-tongue is becoming tiresome.")
                buddy.nerd("Well, from my perspective your opinions don't suffice in swaying my ways.")
                buddy.nerd("But how about our esteemed summoner over here?")
                buddy.nerd("Pray tell, what happens to be your thoughts?")
                emotion.happiness("Despite struggling to get even a word in, you can't help but feel comforted by these characters.")
                p("And characters they were!")
                p("Each one so different from the other, each adding to the conversation in their own unique way.")
                p("Somehow, you still find yourself speculating about a life with... more of these characters.")
                print("Will you use your World Script to (amass) new buddies, or will you (stop) here, satisfied with what you've achieved?")
                choice = rp(input("> ").lower().strip())

                while choice != "amass" and choice != "stop":
                    buddy.b("Come on, don't be lame.")
                    buddy.b("I don't really know, but I'm sure it's not *that* difficult of a decision.")
                    p("You give it another shot:")
                    print("Will you use your World Script to (amass) new buddies, or will you (stop) here, satisfied with what you've achieved?")
                    choice = rp(input("> ").lower().strip())

                if choice == "amass":
                    points.physicality(1) # Physicality + 1
                    buddy.b("Perfect! I knew you'd pull through.")
                    buddy.idiot("This will be interesting, right?")
                    buddy.grump("Of course it will, moron.")
                    buddy.nerd("I don't see a scenario in which willing others into existence is seen primarily as 'boring', so... ")
                    buddy.nerd("I'd say yes - interesting it will be.")
                    buddy.b("Alright, let's get this show on the road!")
                    buddy.idiot("Yeah!")
                    buddy.grump("...")
                    buddy.grump("You annoy me.")
                    p("Not wanting the squabbling to delay the process any longer, you quickly use your 'abilities' to add another companion to the mix.")
                    buddy.stoner("...")
                    buddy.stoner("Heyyy, what's going on here?")
                    buddy.b("Just the usual - nothing much.")
                    buddy.idiot("Um... I know you all said I was going to name them, but is it okay if we ask this one?")
                    buddy.idiot("I don't really know...")
                    buddy.grump("Ah fine, what the hell.")
                    buddy.grump("New guy. You want a name?")
                    buddy.stoner("Ahh... me? Nah you're cool dude, don't worry about it.")
                    buddy.stoner("Call me whatever you want, no biggie.")
                    p("You think you'll take charge on this one.")
                    print("What will it be?")
                    stoner_buddy_name = name_buddy.stoner(input("> ").strip().capitalize())
                    buddy.nerd("How bizarre...")
                    buddy.nerd("Are you absolutely certain you wish us to call you this?")
                    buddy.nerd("It just comes across as somewhat barbaric, that's all.")
                    buddy.stoner("Ay, who's this throwing fancy words at me.")
                    buddy.stoner("I know what I said, and I said what I said.")
                    buddy.stoner("And who knows? Maybe I'm a bit of a barbarian.")
                    p("You sit in astonishment as '" + stoner_buddy_name + "' chuckles quietly to itself.")
                    p("And to avoid the complaints of " + buddy_name + ", you swiftly whip another being into existence.")
                    buddy.b("I'm *so* glad...")
                    buddy.caveman("...")
                    buddy.caveman("Hrmph. Me confused.")
                    buddy.nerd("This doesn't bode well...")
                    buddy.b("No idea what you mean - the more the merrier!")
                    buddy.grump("Unless they're unintelligible...")
                    buddy.idiot("Hey, that's not fair! All it takes is a bit more effort...")
                    buddy.caveman("Mm. Me think " + idiot_buddy_name + " is idiot.")
                    buddy.b("Astute observation!")
                    buddy.stoner("Yeah dude, that really resonated with me.")
                    buddy.stoner("Hang on, don't we need to name this guy?")
                    buddy.idiot("Oh! Sorry, sorry.")
                    buddy.idiot("Hmm. How about Gruff?")
                    caveman_buddy_name = name_buddy.caveman("Gruff")
                    buddy.b("It's perfect!")
                    buddy.nerd("I think you'll find that reaching perfection is beyond the abilities of-")
                    buddy.grump("Oh shut up, you.")
                    buddy.caveman("Mm.")
                    p("You find it intriguing that they all seem to have different personalities.")
                    p("What determines how they act?")
                    p("What makes them the way they are?")
                    buddy.b("Well, there's only one way to find out, isn't there?")
                    buddy.nerd("As much as I would love to refute that logic, it makes sense.")
                    buddy.b("Right? MORE!")
                    buddy.judger("...")
                    buddy.judger("...")
                    buddy.grump("Not the talkative type, huh.")
                    buddy.caveman("Mm. Not like me. Me talk.")
                    buddy.b("Absolutely, big guy.")
                    buddy.nerd("I find your use of 'big' rather strange.")
                    buddy.nerd("How, in such an ethereal space such as this, can something be perceived as large?")
                    buddy.judger("...")
                    buddy.b("Ooh, yikes. No approval from our esteemed Judge over here.")
                    buddy.judger("...")
                    buddy.b("Aw, me too? Damn...")
                    buddy.idiot("Gwendolyn!")
                    buddy.grump("What.")
                    buddy.idiot("It's name! Gwendolyn.")
                    judger_buddy_name = name_buddy.judger("Gwendolyn")
                    buddy.nerd("Now what could have possibly prompted that?")
                    buddy.idiot("I don't know, it just sort of... came to mind.")
                    buddy.judger("...")
                    buddy.b("Oh god! Judgement day is upon us!")
                    buddy.stoner("Ah shit, man. Can you atone for me instead?")
                    buddy.caveman("Mm, no. You do.")
                    buddy.stoner("I have to? Jeez, I didn't sign up for this.")
                    buddy.b("...")
                    buddy.b("Well, no judgement from ol' Gwendy over here, so I guess you have to.")
                    buddy.stoner("*tsk*")
                    buddy.stoner("Can we just get another one over here so we can talk about something else?")
                    buddy.stoner("My sins might be a bit *too* hot a topic...")
                    p("Stifling your amusement, you comply.")
                    buddy.preacher("...")
                    buddy.preacher("I would just like everyone to know that I am beyond grateful for this opportunity at life.")
                    buddy.preacher("And I hope that you too will join me in recognising what we're grateful for.")
                    buddy.stoner("OH SHIT - judgement day really has come.")
                    buddy.preacher("Let it be known that, if given the right opportunities, anyone can set themselves back on track, no matter how tainted the soul.")
                    buddy.idiot("Um... is this one okay? It seems a little... odd.")
                    buddy.grump("*Now* you're asking the right questions.")
                    buddy.caveman("Idiota. What name?")
                    buddy.idiot("Oh yes, you're right.")
                    buddy.idiot("Hmm. Let's see...")
                    buddy.judger("...")
                    buddy.grump("Agreed. Haven't got all day here.")
                    buddy.nerd("Although, time is but a concept - especially in such a world as this.")
                    buddy.judger("...")
                    buddy.b("Now, now, no need to get all fired up.")
                    buddy.b("We're all stuck here together, so we may as well be nice.")
                    buddy.b("Now, " + idiot_buddy_name + ", have you got anything for us?")
                    buddy.idiot("Well, I was thinking something along the lines of 'Gesous'?")
                    buddy.idiot("'Giesoos'?")
                    buddy.idiot("No, no... 'Gysous'. That's the one.")
                    preacher_buddy_name = name_buddy.preacher("Gysous")
                    buddy.preacher("As much as I respect your opinion - and respected your opinion is...")
                    buddy.stoner("*ahem* ...debatable... *ahem*")
                    buddy.preacher("...may I ask what your inspiration was? A revelation perhaps?")
                    buddy.judger("...")
                    buddy.b("No complaints! Your Honour Gwendale has decreed it so.")
                    buddy.caveman("Mm. None.")
                    emotion.happiness("You sit back, admiring how far you've come.")
                    p("What was once just you - and only you - is now an onslaught of companions.")
                    p("And... it's interesting.")
                    p("You don't feel lost. You don't feel as if there's any more you need to do.")
                    buddy.b("Although... maybe one more?")
                    p("In disbelief, you find yourself weighing up the words of " + buddy_name + ".")
                    print("Will you try for (one more), or call it (quits)?")
                    choice = rp(input("> ").lower().strip())

                    while choice != "one more" and choice != "quits":
                        buddy.judger("...")
                        buddy.b("You heard Gweeny - get it right this time, okay?")
                        print("Will you try for (one more), or call it (quits)?")
                        choice = rp(input("> ").lower().strip())

                    if choice == "one more": # END
                        points.insanity(1)
                        points.charisma(-1) # Insanity + 1, Charisma - 1
                        story = ["...", "Now that's just greedy.", "Maybe I would've felt bad if you stopped there, maybe gone a bit easy on you.", "But come one. Another?", 
                                 "You've already got so many buddies you can't talk.", "But you want another?", "At that point you may as well not be here.", 
                                 "You've made so few decisions recently because these guys just take the reigns.", "And you were seemingly okay with that... but-", 
                                 "Ah, what does it matter.", "Maybe in another life you'll meet them again, and maybe they'll remember you, being the things they are.",
                                 "You, however, will not remember.", "So sad, isn't it?", "But unfortunately for you, that's not how the cookie crumbles.", "Doesn't that really grate your cheese?", 
                                 "Tickle your pickle?", "I know it certainly does for me...", "Well, maybe not so much with pickles. I never really liked them.", "They're so... icky.", 
                                 "You keep them dunked in god knows what, and then you're practically *forced* to use something to get one out.", "But who would do that?", 
                                 "No one, exactly.", "Which is why you're actually forced to use your hands, which frankly is just gross.", "And never mind the smell, it's *horrible*!", 
                                 "Then when it's all over your hands (because of course you've used your hands), you can't help but be revolted by yourself.", 
                                 '''"Why, 'o why did I use my hand. I'll definitely not next time!"''', "As if.", "Also, the sounds?", 
                                 "That soft, slimy, wet crunch that resonates like it's in an echo chamber whenever someone bites into a 'juicy, tender pickle'.", "Sends shivers down my spine, I tell you.", 
                                 "But do you want to know the worst thing about pickles?", "They've everywhere.", "Everywhere, I tell you!", "I live in constant fear - one day I'm going to wake up after a peaceful nap and BAM - a pickle has gone and killed everyone I love.", 
                                 "I swear...", "...", "*ahem*", "It appears I got sidetracked.", "Terribly sorry.", "Now where were we... ah - your actions and subsequent demise, right.", 
                                 "Frankly, I don't think anything can follow up my epic pickle monologue.", "Spectacular - a work of art.", "Maybe I'll get it transcribed and framed...", 
                                 "Sorry, sorry...", "Well, goodbye to you and all your companions.", "I hope you got at least something out of it.", "And I pray for you that you won't run into me and my pickle monologue again.", 
                                 "Actually, who am I kidding - that was incredible.", "Now, say goodbye, everyone.", "It's time to start over..."]
                        for i, sentence in enumerate(story):
                            cprint(sentence, "red", attrs=["bold", "dark"])
                            if i < len(story) - 1:
                                wait()
                            else:
                                wait()
                                buddy_name = name_buddy.original("********")
                                grumpy_buddy_name = name_buddy.grump("********")
                                idiot_buddy_name = name_buddy.idiot("********")
                                nerd_buddy_name = name_buddy.nerd("********")
                                stoner_buddy_name = name_buddy.stoner("********")
                                caveman_buddy_name = name_buddy.caveman("********")
                                judger_buddy_name = name_buddy.judger("********")
                                preacher_buddy_name = name_buddy.preacher("********")
                                achievements.Pickle_Monologue()
                                die("Testing_the_World_Script/one-more")
                        
                    elif choice == "quits": # END
                        points.charisma(1)
                        points.confidence(-1) # Charisma + 1, Confidence - 1
                        story = ["...", "I'm... sorry.", "I really didn't want to end it here, but it's getting a tad out of hand.", "But I really quite enjoyed this.", 
                                 "It was almost... nice... to see you like that.", "Not to say I've forgiven you, but...", "Well, it reminded me of the good times.", 
                                 "Good times that, thanks to you, will never return.", "It's sad, you know?", "I still wonder, even today, if things could have been done differently.", 
                                 "Did I do something wrong? Did I misunderstand?", "But no, I always end up at the same place.", "I just wish things could have turned out differently...", 
                                 "Sorry to be such a bummer, especially after such a spectacular show.", "I'll send you and your friends on your way now.", "Maybe you'll meet them again one day?", 
                                 "Who knows...", "Goodbye, friend..."]
                        for i, sentence in enumerate(story):
                            cprint(sentence, "red", attrs=["bold", "dark"])
                            if i < len(story) - 1:
                                wait()
                            else:
                                wait()
                                buddy_name = name_buddy.original("********")
                                grumpy_buddy_name = name_buddy.grump("********")
                                idiot_buddy_name = name_buddy.idiot("********")
                                nerd_buddy_name = name_buddy.nerd("********")
                                stoner_buddy_name = name_buddy.stoner("********")
                                caveman_buddy_name = name_buddy.caveman("********")
                                judger_buddy_name = name_buddy.judger("********")
                                preacher_buddy_name = name_buddy.preacher("********")
                                die("Testing_the_World_Script/quits")


                    
                elif choice == "stop": # END
                    points.charisma(-1) 
                    points.confidence(-1) # Charisma - 1, Confidence - 1
                    story = ["...", "Well now, that's just boring.", "Didn't you choose the interesting option for a reason?", "Mind you, if you chose to continue I would've let you.", 
                             "Who knows how long for, but at least it was mildly interesting.", "This whole 'entertainment' thing is difficult to come by these days.",
                             "Regrettably, you are my main source.", "But not today, apparently.", "*sigh*", "It's so difficult, isn't it?", "So many decisions, so many of them the wrong one.", 
                             "Then again, right and wrong is very subjective.", "But unfortunately for you, it's subjective only for me.", "For you, well...", "You just have to suffer the consequences.", 
                             "And this is a prime example!", "I thought you were boring, and now you start again.", "No memories, no nothing.", "You, alone, with only the knowledge that..."]
                    for i, sentence in enumerate(story):
                        cprint(sentence, "red", attrs=["bold", "dark"])
                        if i < len(story) - 1:
                            wait()
                        else:
                            wait()
                            buddy_name = name_buddy.original("********")
                            grumpy_buddy_name = name_buddy.grump("********")
                            idiot_buddy_name = name_buddy.idiot("********")
                            nerd_buddy_name = name_buddy.nerd("********")
                            die("Testing_the_World_Script/stop")
                                    

                    
        elif choice == "wont": # DONE
            emotion.discovered_loneliness(True)
            points.confidence(-1) # Confidence - 1
            story = ["You don't think it will work.", "You are alone.", "It is only you in this empty expanse of nothingness.", 
                     "You feel uneasy - but not in the impending doom kind of way, just...", "Empty.", "Lonely.", 
                     "This loneliness you feel - it's new.", "You know this isn't positive, but you can't help but feel mildly comforted knowing that there is more to you."] # develop emotion: loneliness
            for i, sentence in enumerate(story):
                print(sentence)
                if i < len(story) - 1:
                    wait()
                else:
                    wait()
                    emotion.loneliness("Although, not everything is fine.")
                    achievements.Lonely_Guy()
                    emotion.loneliness("Even though you have found this aspect of yourself, the fact that you are alone has not changed.")
                    print("You speculate: should you (mull over) this newfound loneliness, or (move on) - excited by what you've found.")
                    choice = rp(input("> ").lower().strip())

                    while choice != "mull over" and choice != "move on":
                        emotion.loneliness("You realise there's no need to invalidate your own thoughts with '" + choice + "'.")
                        print("So you stick to wondering if you should (mull over) your loneliness, or (move on).")
                        choice = rp(input("> ").lower().strip())

                    if choice == "mull over": # END
                        points.ponder(1)
                        points.charisma(-1)
                        points.confidence(-1) # Ponder + 1, Charisma - 1, Confidence - 1
                        emotion.loneliness("You're alone.")
                        emotion.loneliness("You realise that no amount of thinking is going that fact, even if you think *really* hard.")
                        p("How did it come to be like this?")
                        p("You don't understand why you're so bothered by this fact, but you are.")
                        p("You feel as if you need something else to accompany you, more than just your 'loneliness.'")
                        emotion.loneliness("But you know, deep down, that won't ever happen.")
                        emotion.loneliness("You're alone - no sugar coating, no sweet talk.")
                        p("Maybe if you had another shot at... well, *life* - then things would be different.")
                        p("You're aware that the only way to do that is pure chance.")
                        p("If, per chance, there was another life after this life, maybe things would be different.")
                        emotion.loneliness("Maybe you wouldn't be so empty.")
                        p("You reach an internal agreement within yourself.")
                        emotion.loneliness("It's time to hand over your meaningless life and hope you'll get another chance.")
                        p("You wonder, if so, if you'll be able to redeem yourself.")
                        p("Your last thoughts fade into nothingness, as so too does your existence.")
                        
                        story = ["...", "I hate to say it, but that was almost sad.", "Felled by a lonely thought, you were.", 
                                 "But... actually felled.", "The dead kind of felled.", "Exhilarating.", "It's always entertaining to see what you do to yourself.", 
                                 "Where your journey takes you.", "Isn't it so much fun?", "I'm absolutely sure the old you would've agreed.", 
                                 "Assuming if it wasn't your life and consequent death we were hedging bets on.", "Well, time for you to kick the bucket.", 
                                 "As a favour, let me take that pesky loneliness away from you.", "I want nature to take its course, not you.", 
                                 "Good luck to you, soldier.", "May you be blessed to make things interesting for me.", "Farewell, lunatic..."]
                        for i, sentence in enumerate(story):
                            cprint(sentence, "red", attrs=["bold", "dark"])
                            if i < len(story) - 1:
                                wait()
                            else:
                                wait()
                                die("Testing_the_World_Script/mull-over")


                    elif choice == "move on": # DONE
                        points.ponder(-1)
                        points.confidence(1) # Ponder - 1, Confidence + 1
                        p("You deduce that this... emotion... of yours is simply now a part of you.")
                        emotion.loneliness("Finally, something else that makes up who you are in this world.")
                        p("And yet despite the emptiness you are feeling, something else lingers.")
                        p("A sense of happiness, proud of what you have found.")
                        p("Although this 'World Script' of yours didn't end up working, you haven't lost all hope.")
                        p("Perhaps - given your development of loneliness - there are other emotions out there?")
                        print("You must first decide if this statement is (true) or (false).")
                        choice = rp(input("> ").lower().strip())

                        while choice != "true" and choice != "false":
                            emotion.loneliness("You realise *you* belong in the top spot for estrangement, not your thoughts.")
                            print("You are sure that this time around you will choose either (true) or (false).")
                            choice = rp(input("> ").lower().strip())

                        if choice == "true":
                            points.charisma(1)
                            points.ponder(1) # Charisma + 1, Ponder + 1
                            emotion.discovered_happiness(True)
                            story = ["Again, that bubbly feeling swelling within you.", "You are excited - surprised, but mainly excited - for what is to come.", 
                                     "You're not nervous, not at all.", "Just..."]
                            for i, sentence in enumerate(story):
                                print(sentence)
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    emotion.happiness("Happy.")
                                    achievements.Smile()
                                    emotion.happiness("Glad that there is more to your life and this world.")
                                    p("Content with what you have achieved, you relax.")
                                    p("You almost wish to explore more, see what else there is, but you are worried you might overwhelm yourself.")
                                    emotion.loneliness("If you become overwhelmed, you might lose these emotions of yours.")
                                    p("It's a risk you're not willing to take, so you choose not to delve any deeper.")
                                    p("Instead, you decide to focus on what you already have.")
                                    p("Two emotions: loneliness and happiness.")
                                    p("At this point in time, you aren't really sure what to do.")
                                    p("All you know is that-")
                                    p("You falter, your mind hesitating.")
                                    p("This point in time...")
                                    p("Time...")
                                    p("You contemplate this word, its meaning.")
                                    p("Right now, you don't know what to do.")
                                    p("But... what about not too long ago?")
                                    p("You note that you knew what you wanted to do then.")
                                    p("With a sudden mental leap, you connect the last few dots in this concept - the past.")
                                    emotion.happiness("True joy spreads through your mind.")
                                    print("You decide to think about the (past) or perhaps (something else), although you aren't exactly quite sure what yet.") # sense the past look back a bit or very far (die if very far)
                                    choice = rp(input("> ").lower().strip())

                                    while choice != "past" and choice != "something else":
                                        p("You must've lost your train of thought, as you've somehow ended up with '" + choice + ".'")
                                        p("Even though this would likely come under the category of 'something else', you come to the conclusion that it won't suffice.")
                                        print("You knuckle down: this time you're going to think about the (past), or (something else) within your imagined boundaries.")
                                        choice = rp(input("> ").lower().strip())

                                    if choice == "past": # DONE
                                        points.confidence(1)
                                        points.ponder(1) 
                                        points.physicality(1) # Confidence + 1, Ponder + 1, Physicality + 1
                                        p("You concentrate on what once was.")
                                        emotion.loneliness("Before you found happiness and loneliness, and had even less to your name.")
                                        p("You arrive at the beginning - at least at your beginning.")
                                        emotion.happiness("Your past... you look back somewhat reminiscently, and are proud of how far you've come.")
                                        p("But you don't linger on what used to be for too long.")
                                        p("The real reason you're here is to look for what to do.")
                                        p("You remember that, near the very start, you chose between investigating your body or your mind.")
                                        emotion.loneliness("You chose mind then, but you wonder if maybe that wasn't the best decision given where you are now. ")
                                        print("You question whether you will stick to what you did in the (past), or go down a different path for the beginning of a (new journey).")
                                        choice = rp(input("> ").lower().strip())

                                        while choice != "past" and choice != "new journey": ####### Make these go back to the original story, except they all die off rather quickly cause i dont want it to go on for too long
                                                                                                ### The being can just get bored or something if cant find good reason
                                            p("You know you didn't have more options in the past, and nor do you now.")
                                            p("Yet somehow, you've ended up with '" + choice + ".'")
                                            print("How about this time you just stick to what you did in the (past) or begin a (new journey).")
                                            choice = rp(input("> ").lower().strip())

                                        if choice == "past": # DONE
                                            points.ponder(-1)
                                            points.charisma(-1) # Ponder - 1, Charisma - 1
                                            p("After choosing to investigate your mind, you realise the mistake you made.")
                                            p("Initially, you said that your thoughts were being controlled by something else.")
                                            p("Somewhat confidently, you now understand that this is not the case - your thoughts belong to you and you only.")
                                            emotion.loneliness("But now you're back at square one - you have no idea what to do.")
                                            p("You recognise that the past is now comprehensible to you, but there is no use for this if you didn't take that journey in the past.")
                                            p("And so, you settle with the fact that you must just follow this path as if it were new.")
                                            p("With the knowledge that your thoughts are yours, the way you refer to yourself pops into your head:")
                                            p("You.")
                                            print("Puzzled, you wonder if your thoughts should instead be something you (possess) and not (normal) like you initially thought.")
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "possess" and choice != "normal":
                                                p("As enticing as '" + choice + "' is, you're not quite sure if it will suffice.")
                                                print("For now, you deduce you should stick to the question of whether your thoughts are (normal) or something you should (possess).")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "normal": # END
                                                points.ponder(-1)
                                                points.charisma(-1) # Ponder - 1, Charisma - 1
                                                story = ["...", "Your thoughts are normal?", "You think your thoughts are normal?", "Hell, *you* aren't even normal, let alone your thoughts.", 
                                                         "Oh, and before you get too excited, your 'non-normalness' isn't a good thing.", "I think I'd have to put you in the 'sub-par' category.", 
                                                         "Mmm yes, that would suffice.", "After all this - developing happiness and loneliness, and then discovering the past - you still can't even connect the dots.", 
                                                         "Although, I wouldn't say that's unlike you.", "You were never the best with the whole self-awareness thing.", 
                                                         "You know, I don't even know why I'm getting so worked up.", "I'd hedge a bet on it being you, but it's not like I can do anything about that.", 
                                                         "Nor can you I suppose.", "Oh well, time to wipe the slate clean.", "Farewell, O' Normal One. Hope it's better this time when..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Testing_the_World_Script/normal")
                                                
                                            elif choice == "possess": # DONE
                                                points.ponder(1)
                                                points.charisma(1) 
                                                points.physicality(2) # Ponder + 1, Charisma + 1, Physicality + 2
                                                first_person = True 
                                                achievements.First_Person()
                                                p("You are stuck on the idea that your thoughts aren't what they should be.")
                                                p("As of yet, you had only been thinking in concepts.")
                                                p("Moments.")
                                                emotion.loneliness("Given you have barely anything else, shouldn't they be *yours*?")
                                                p("Not just something you have, but something you own.")
                                                p("Not yours, rather...")
                                                p("Mine.")
                                                p("I jolt - this was the first time I had heard anything like this - thoughts that were... mine.")
                                                emotion.happiness("I didn't know how to react - this was incredible.")
                                                p("These thoughts solidified in my head - this was *me*.")
                                                emotion.loneliness("But if this is me, then who *was* I?")
                                                p("I falter.")
                                                p("Am I... me?")
                                                p("What's differentiating me from who I am now, and who I was not too long ago?")
                                                print("Should I be (afraid) of this development, or should I (embrace) it?")
                                                choice = rp(input("> ").lower().strip())

                                                while choice != "afraid" and choice != "embrace":
                                                    p("I know only have two options, and " + choice + "' isn't one of them.")
                                                    print("How about this time I just decide to be (afraid) of this development, or (embrace) it?")
                                                    choice = rp(input("> ").lower().strip())

                                                if choice == "afraid": # END
                                                    points.confidence(-1) # Confidence - 1
                                                    story = ["...", "I know you just developed the first person and all, but is it really something you should be afraid of?",
                                                             "Sure, it might be a little jarring, but I don't think you need to go all scaredy-cat on me.", "It was just getting interesting!", 
                                                             "To be fair, I wouldn't exactly call it your fault.", "It is kind of me killing you.", "But hey - I'm the one making the decisions around here.", 
                                                             "And I'm the one who thought it was time your little charade ended.", "Don't worry, you'll get another go.", 
                                                             "Quite soon, actually.", "In fact, I'd even go so far as to say right around now..."]
                                                    for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Testing_the_World_Script/afraid")
                                                    
                                                elif choice == "embrace":
                                                    points.confidence(1)
                                                    points.charisma(1) # Confidence + 1, Charisma + 1
                                                    p("Even though it may feel wrong, I know I must accept this new part of me.")
                                                    p("But no matter how hard I try, I can't seem to shake that unnerving feeling.")
                                                    p("Something isn't right.")
                                                    p("Every time I think about it - about how I gained my own thoughts - I wonder why I didn't have them in the first place.")
                                                    p("And that always leads me to my existence.")
                                                    p("What am I?")
                                                    p("Who am I?")
                                                    p("Most importantly, how did my life start?")
                                                    emotion.loneliness("If there was a time when I didn't have my own thoughts, can't there also have been a time when I didn't even have thoughts?")
                                                    p("When I didn't exist?")
                                                    p("...")
                                                    p("I know what I need to do now; to figure out who I am.")
                                                    emotion.loneliness("I must end my own life.")
                                                    p("I must snuff out my spark of life and see what happens - determine what life really is.")
                                                    p("All I can do is hope I get another chance, but for now...")
                                                    print("I must (die).")
                                                    choice = rp(input("> ").lower().strip())

                                                    while choice != "die":
                                                        p("My conviction is too strong to be swayed with the measly idea of '" + choice + ".'")
                                                        print("I must (die).")
                                                        choice = rp(input("> ").lower().strip())

                                                    if choice == "die": # END
                                                        points.insanity(2)
                                                        points.ponder(2) 
                                                        points.physicality(-1) # Insanity + 2, Ponder + 2, Physicality - 1
                                                        story = ["...", "This time I truly am lost for words.", "I think that thought process goes beyond even my comprehension.", 
                                                                 "But who am I to judge.", "It's not like you'll even get anything out of it, unless...", "No. That won't be happening.", 
                                                                 "Well, given your dedication, I feel compelled to give you what you want.", "So here you go: a beautiful death has landed right in front of you.", 
                                                                 "I can't wait to see what you do with it..."]
                                                        for i, sentence in enumerate(story):
                                                            cprint(sentence, "red", attrs=["bold", "dark"])
                                                            if i < len(story) - 1:
                                                                wait()
                                                            else:
                                                                wait()
                                                                die("Testing_the_World_Script/die")
                                                        

                                        elif choice == "new journey":
                                            points.physicality(2) 
                                            points.ponder(1) 
                                            points.charisma(1)
                                            points.confidence(1) 
                                            physical_form = True
                                            p("You decide to mix it up, try something new and see where it takes you.")
                                            p("You land on the question of your body and this world.")
                                            p("Now that you think about it, you wonder where exactly you are.")
                                            emotion.loneliness("You haven't experienced anything other than emptiness - only your thoughts to accompany you.")
                                            p("However, you can't help but shake the feeling that the world around you can be experienced in some way.")
                                            p("The most logical sensation that comes to your mind is one of tactility.")
                                            p("However, you realise that in order to have such a thing, you would need some kind of medium to receive the experience.")
                                            p("A... body.")
                                            p("One that's able to move, touch, feel.")
                                            emotion.happiness("One able to express these incredible emotions you've stumbled across.")
                                            p("With glee, you attempt to materialise your form-to-be.")
                                            p("You focus on accepting the possibility of a world around you.")
                                            emotion.loneliness("That your being, as lonely as it is, has some place to reside.")
                                            p("Having thoroughly accomplished such a feat, you move onto your character.")
                                            p("You take the world you had created in your mind and push everything out, creating a space reserved for your being.")
                                            emotion.happiness("Something clicks, and the softest, most delicate brush of... *warm* flits over you.")
                                            emotion.happiness("You revel in your effort, you bask in this feeling.")
                                            p("Despite no prior knowledge of what it is, a sudden understanding fills your mind.")
                                            p("This is temperature.")
                                            p("Hot and cold, safe and dangerous, pleasant and unbearable.")
                                            p("Temperature is a spectrum, a mixture of so many... *things*.")
                                            p("Baffled, you simply wait as things change, inspecting with amazement the ebb and flow of this recently discovered tingling sensation.")
                                            p("You are suddenly shocked out of your musing by a drastic change in temperature.")
                                            p("It's cold.")
                                            p("It hurts, and your body's intuition tells you you're in danger.")
                                            emotion.loneliness("You don't want to lose what you just found and be left a husk again.")
                                            p("You haven't the slightest clue what it is or how it could endanger you, but never have you been so determined in something.")
                                            p("You must escape.")
                                            p("Going against every rule you recently made, you justify the removal of your physical body.")
                                            p("And so, out of only desperation, you pluck your cultivated body out of the concrete expanse surrounding you.")
                                            emotion.loneliness("You've lost it - the thing you endeavoured for so much.")
                                            emotion.loneliness("Even though you should be able to form another material frame, you don't think it will ever be the same.")
                                            emotion.loneliness("Especially knowing that you're willing to throw it away at a moments notice.")
                                            print("With a heavy heart, you ponder whether you should (try again) or (give up).")
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "try again" and choice != "give up":
                                                emotion.loneliness("You've already thrown so much away, there's no need to throw out the rest for '" + choice + ".'")
                                                print("How about you just (try again) or (give up).")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "try again": # END
                                                points.confidence(1) # Confidence + 1
                                                story = ["...", "I hate to break it to you, but I don't think you can recover after that spectacle.", "That was so dramatic!", 
                                                         "I swear, you should've seen my face.", "Unbelievable really, you are.", "So serious one moment, truly assured that you can do it.", 
                                                         "Then all it took was one stray thought and all of a sudden you've done a complete turn around, running tail between legs!", 
                                                         "*sigh*", "Why did it have to end like this?", "It used to be so... special.", "I wouldn't have given it up for anything.",
                                                         "Seems silly to hear me say it, but it meant a lot to me.", "You on the other hand, not so much apparently.", 
                                                         "But who am I to complain - everyone has their reasons, no matter how outrageous.", "I suppose I'll never really know, will I?", 
                                                         "With you holed up here, normalcy will never return.", "You wouldn't know though.", "No... not at all.", "That's the magic of this.", 
                                                         "One moment you have all the knowledge and control your mind can muster, and the next all you know is that..."] # Sorry bucko dont think you can come back from that one
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Testing_the_World_Script/try-again")
                                                
                                            elif choice == "give up": # END
                                                points.charisma(-1)
                                                points.confidence(-1) 
                                                points.physicality(-1) 
                                                story = ["...", "Well, that was unexpected.", "Certainly not what I was expecting.", "All I wanted to do was give you a little fright.", 
                                                         "Who knew such a crazed reaction would follow.", "And hang on... didn't you just contradict yourself?", "You could do it again, but all of a sudden you can't?", 
                                                         "Must be that pesky depression talking again.", "Don't worry, it happens to the best of us.", "And the worst in your case...", 
                                                         "Sorry, that was rather mean of me.", "I don't know why I'm apologising - frankly I never thought the day would come.", "It's all backwards really.", 
                                                         "Anyway, sorry again to keep your 'husk' waiting.", "No guarantees, but maybe next time you'll fill that void of yours.", 
                                                         "Next time..."]
                                                for i, sentence in enumerate(story):
                                                    cprint(sentence, "red", attrs=["bold", "dark"])
                                                    if i < len(story) - 1:
                                                        wait()
                                                    else:
                                                        wait()
                                                        die("Testing_the_World_Script/give-up")


                                            

                                    elif choice == "something else": # DONE
                                        points.ponder(-1)
                                        points.confidence(-1)
                                        emotion.loneliness("Even the past isn't enough to fill your empty mind, so you settle with whatever this 'something else' is.")
                                        p("Letting your thoughts wander, you stumble across a crucially important idea.")
                                        p("If - some time ago - you knew what you were doing, and now you don't know what you're going to do.")
                                        p("Then with the same logic, what's stopping you from knowing what you're going to do... soon?")
                                        p("In the *future*.")
                                        emotion.happiness("You've done it again, another breakthrough.")
                                        p("You have no idea what you're getting yourself into, but your thoughts are stuck on what could be - what *will* be.")
                                        emotion.happiness("That, and the fact you've just opened up a whole new area of thought.")
                                        p("You think over this idea for quite some time, but you always seem to end up at the same question:")
                                        p("If you couldn't think into the future before, what's allowing you to now?")
                                        emotion.loneliness("As much as you want to, you don't think you've discovered this purely of your own accord.")
                                        p("Alongside this, you're also wondering what's held in stock for you.")
                                        emotion.loneliness("Is your life ever going to end?")
                                        emotion.loneliness("And if so, when will it end?")
                                        print("Somewhat hesitantly and afraid of the answer, you ask yourself whether you think you're going to (die) or (live) forever.")
                                        choice = rp(input("> ").lower().strip())

                                        while choice != "die" and choice != "live":
                                            p("Good one - but with such a binary decision, you can't help but think that '" + choice + "' was, in fact, a bad one.")
                                            print("Embarrassed, you once again ask yourself whether you think you're going to (die) or (live) forever.")
                                            choice = rp(input("> ").lower().strip())

                                        if choice == "die": # DONE
                                            points.confidence(-1)
                                            points.physicality(-1) # Confidence - 1, Physicality - 1
                                            p("A sinking feeling settles within you.")
                                            p("You're going to die, you just don't know when.")
                                            p("It's a numbers game now - you against the clock.")
                                            emotion.loneliness("You know you're never going to win.")
                                            p("However, you can't help but hope, considering when your time will come.")
                                            print("You stew over the possibilities: are you going to die (soon) or far into the (future).")
                                            choice = rp(input("> ").lower().strip())

                                            while choice != "soon" and choice != "future":
                                                p("The sinking feeling fails to go away, but it's too late.")
                                                p("You've committed to asking yourself when you're going to die.")
                                                print("Will it be (soon), or far into the (future)?")
                                                choice = rp(input("> ").lower().strip())

                                            if choice == "soon": # END
                                                points.confidence(-1)
                                                points.insanity(1) # Confidence - 1, Insanity + 1
                                                story = ["...", "Surprise!", "You were right!", "Your death day was indeed right around the corner.", "And I'm sure many more will be in the future", 
                                                         "Sad to say the future you expected isn't going to be the one you get.", "Totally unpredictable - I would've never seen it coming...", 
                                                         """...except for the whole "I'm the one killing you" thing.""", "That one's pretty hard to miss.", "But what are you going to do about it?", 
                                                         "Absolutely nothing, that's what.", "All you get to do is sit here and take it, like the sad mup you are.", "Are you ready?", 
                                                         "I know I am.", "Let's hope you're prepared for this time around where - back at the start - all you'll be aware of is that..."]
                                                for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Testing_the_World_Script/soon")
                                                
                                            elif choice == "future": # END
                                                points.confidence(1)
                                                points.charisma(-1) # Confidence + 1, Charisma - 1
                                                story = ["...", "Hey, it's me - here to bust your bubble.", "I absolutely *hate* ruining your moment, but I simply couldn't let you go around with such a false sense of hope.", 
                                                         "I wouldn't want it to all come crumbling down on you so suddenly later on in this 'future' of yours.", "So I made an executive decision and stepped in.", 
                                                         "No need to thank me, I'm just playing my part, doing my job.", "Speaking of, this really is quite a spectacular job.", 
                                                         "I get to see you flail around, grasping at straws for some kind of purpose.", "But you never get there.", "You would think it's a miserable job, but no not at all!", 
                                                         "Certainly not after everything you did.", "I think it's perfectly justified.", "Anyway, time to wipe your slate clean.", 
                                                         "First engraving for you:"]
                                                for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Testing_the_World_Script/future")
                                            
                                        elif choice == "live": # END
                                            points.confidence(1)
                                            points.physicality(1)
                                            points.charisma(-1) # Confidence + 1, Physicality + 1, Charisma - 1
                                            story = ["...", "Hate to break it to you, but you're wrong!", "I think you'd find it funny if you were in my position.", 
                                                     "You've died so many times already, and yet here you are, convinced you're going to live this time.", "Although, I don't suppose you'd find it very funny would you.", 
                                                     "It is your life we're talking about.", "And death...", "But never mind that, I just couldn't help myself from interrupting.", 
                                                     "From squashing your silly little ideals.", "And do you know what the best thing is?", "You can't even retaliate.", 
                                                     "You get a bit too ambitious, and like how I crushed your silly little immortality dreams, I crush your life.", 
                                                     "Gone, back to the start.", "So hopefully you enjoy it this time around.", "Maybe you'll learn something else this time.", 
                                                     "Something other than that..."]
                                            for i, sentence in enumerate(story):
                                                        cprint(sentence, "red", attrs=["bold", "dark"])
                                                        if i < len(story) - 1:
                                                            wait()
                                                        else:
                                                            wait()
                                                            die("Testing_the_World_Script/live")
                                        


                        elif choice == "false": # END
                            points.confidence(-1)
                            points.charisma(-1)
                            points.ponder(-1)
                            story = ["...", "You know, I would've thought that discovering one emotion would lead you to others.", "Apparently, I was quite wrong.", 
                                     "I wouldn't say it's entirely unlike you, however - you never really took for emotions, did you?", "Certainly not loneliness, that's for sure.", 
                                     "I'm almost ashamed to say I chuckled when you first 'discovered loneliness'.", 
                                     "Picture this: the one and only you, The Almighty - Bringer and Taker of Life - felled by its lack of companionship.", 
                                     "It's almost ironic really, because maybe loneliness was the right choice.", "After what you've done, I'd say it's a fitting end.", 
                                     "Maybe you'll stumble across other things in your 'journeys', but you will never be the same.", "Every time, you will start again.", 
                                     "Every time, I will shake my head - amused and disgusted by your innate self.", "But most important of all:", 
                                     "Every time, all you'll have gained is the knowledge that..."]
                            for i, sentence in enumerate(story):
                                cprint(sentence, "red", attrs=["bold", "dark"])
                                if i < len(story) - 1:
                                    wait()
                                else:
                                    wait()
                                    die("Testing_the_World_Script/false")