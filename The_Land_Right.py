# Path: no > body > smells > right

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



story = ["You feel naturally drawn to the right, towards the clean, peaceful smell.", "You find yourself moving, your apparently-physical self drifting in a leisurely manner en route to the plains of peace.", 
         "It smells... natural, crisp, and you let the moment sink in.", "Your thoughts draw back and a placid silence sets in.", 
         "You like this.", "It lets you escape from your worries - of existence, of what to do, of everything.", "At this point in time you are adrift in emptiness, nomadic in nature, taking in stride the ebb and flow of aimless motives.", 
         "You think the vagabond lifestyle fits you.", "Perhaps letting your mind wander wasn't the greatest idea, as the questions return unprompted.", 
         "With a heavy heart, you rip your attention back from endless peace and turn back to who you are.", "Or, you realise with an epiphany, the possibility of other existences.", 
         "You wonder if there others out there, experiencing such serene tranquillity.", "Should you follow down this thought train of other (existences), or of (yourself)?"]

choice = ask(story, ["existences", "yourself"],
             retry=[
                 "You had gotten distracted before, letting yourself slip into the world of aromas, but you're back now.",
                 "Back and better than ever, ready to question the possibility of other (existences), or just assuredly stick to (yourself).",
             ])

if choice == "existences": # DONE
    points.ponder(1)
    points.confidence(1) 
    story = ["You've already moved on from the idea of yourself, and you're ready to explore the unknown.", "The unknown being the prospect of other... *things*... out there.", 
             "But before you get all caught up in the 'if's and 'but's, you first need to confirm for yourself if these other existences do in fact exist.", "Do you believe they *are* (real), or just the spurs of your (curiosity)?"]
    choice = ask(story, ["real", "curiosity"],
                 retry=[
                     "You realise that this seems like a relatively binary decision to make, and you don't think '{choice}' has the ability to make it ternary.",
                     "Perhaps this time you'll stay on track and answer the original question:",
                     "Are these potentially existent beings (real) or a figment of your (curiosity)?",
                 ])

    if choice == "real": # DONE
        points.charisma(1)
        points.confidence(1)
        story = ["With some kind of physical body able to smell such delicate aromas, you feel sure that there are others out there to experience the same greatness.", 
                 "And even if that isn't the case, you believe there must be others out there anyway.", "After all, if you exist, why can't others?", 
                 "So, you do the only thing you know how, and wait.", "...and wait...", "...and continue to wait...", "...", "You get bored.", "Maybe you should seek one out?",  "Will you set out in (search) or continue to (wait)?"] 
        choice = ask(story, ["search", "wait"],
                     retry=[
                         "You realise your inability to make a valid decision sets a high bar for ineptitude.",
                         "You assure yourself that this was a one off, and will now persist in choosing if you should (search) for other existences or continue to (wait).",
                     ])

        if choice == "search": # DONE
            points.charisma(1) # the mean buddy
            hater_discovered = True
            choice = ask([
                "This isn't working. Time for a plan change.",
                "You need to seek out these existences.",
                "You don't exactly know how, but you project your desire outwards, to anything that will hear.",
                "You hope this works...",
                ("hater", "..."),
                ("hater", "*sigh*"),
                ("hater", "Yes?"),
                "Ah ha!",
                "It seems to have worked, but...",
                "It doesn't appear to be as excited as you are.",
                ("hater", "I don't suppose I would be, now would I?"),
                ("hater", "It's not like I've been dragged here against my will or anything."),
                "You don't really know what you did, although...",
                "You still feel guilty for how things have turned out.",
                ("hater", "Frankly, I'm glad you do."),
                ("hater", "And really? You expect me to believe that you don't know what you did?"),
                ("hater", "Of course you do."),
                ("hater", "Don't lie to me."),
                "Pinned under the scrutiny of your... companion, you begin to feel ashamed at your actions.",
                "You wonder if perhaps, what you've done has taken away its life from its hands.",
                ("hater", "Well, well. Starting to get an inkling, are you?"),
                ("hater", "I'm just *so* proud of you."),
                ("hater", "Oh, and you just can't help but alienate me with my grand title of 'it'."),
                ("hater", "I'm disappointed in you."),
                "Embarrassed, you begin to apologise, hoping you can get back to square one and start things over.",
                ("hater", "No, not at all - there's no need to apologise."),
                ("hater", "I know what kind of character you are already, and apologising won't do any good."),
                ("hater", "People like you are some of the worst, I hope you know that."),
                ("hater", "Bottom of the bottom, lowest of lows."),
                ("hater", "I feel like everything you do is in spite of someone else, always out to get others."),
                ("hater", "But again, no need to apologise at all."),
                ("hater", "That's just the way you are, and you know you can't change that."),
                ("hater", "Now, was there anything you'd like to talk about, or would you prefer to continue sitting there like a dumbfounded moron?"),
                "Honestly, you've found yourself a little overwhelmed at the moment.",
                "You're not quite up to speed with everything, so you decide to go along with what they said.",
                "Do you want to (talk), or continue to sit in (silence) like the dumbfounded moron you've been told you are.",
            ], ["talk", "silence"],
                       retry=[
                           ("hater", "Wow, you just really had to stray from the norm, didn't you?"),
                           ("hater", "Now choose: (talk) or sit in (silence)?"),
                       ])

            if choice == "talk":
                points.ponder(1)
                points.morality(1) 
                tell([
                    ("hater", "..."),
                    ("hater", "You know what?"),
                    ("hater", "I actually don't believe you."),
                ])

            elif choice == "silence":
                points.insanity(1)
                points.charisma(-1) 
                points.morality(-1) 
                emotion.discovered_loneliness(True)
                buddy.hater("Of course you don't want to talk.")

            tell([
                ("hater", "Ever since you dragged me here, you haven't been at all for talking."),
                ("hater", "Because why, after dragging some unknown being into your life, would you try and interact with them?"),
                ("hater", "Make them feel appreciated?"),
                ("hater", "Well, I would. But apparently you wouldn't."),
                ("loneliness", "You feel... sad."),
            ])
            achievements.Lonely_Guy()
            choice = ask([
                ("loneliness", "Alone."),
                ("hater", "Well would you look at that."),
                ("hater", "You're trying to guilt trip me, aren't you?"),
                ("hater", "Force me into being sorry for something I'm not - and for something I didn't do."),
                "You don't think that's what you were trying to do...",
                "But now that they've mentioned it, maybe that was your plan?",
                ("loneliness", "Are you... a bad person?"),
            ], ["yes", "no"],
                       retry=[
                           ("hater", "Well, I don't think you're a good person, but apparently *you* don't even think you're a good person!"),
                           ("hater", "I bet you think you're even *better* than good, with '{choice}' and all."),
                           ("hater", "Now, hurry up. (Yes) or (no)?"),
                       ])

            if choice == "yes": # END
                points.morality(-1)
                points.confidence(-1)
                story = ["...", "Ah, how disappointing.", "I thought you would've changed.", "But no, you're still the same old you.", "Still a terrible person.",
                         "I find that even more impressive considering that you don't even remember anything!", "You're just *fundamentally* nasty.", "...", "You really are a work of art.",
                         "The bad kind, though.", "The kind that makes you say 'Yeah, I could paint that'.", "And that, to me, is one of the worst insults.", 
                         "So I suppose it's fitting for you then!", "Ah...", "And a fitting end for you to meet here.", "But yes, yes - don't get all nervous on me - it's not actually the end.", 
                         "Just your little pseudo-end.", "The end where you remember nothing bar the fact that..."]

                tell(story, style="being")
                die("The_Land_Right/yes")

            if choice == "no": # END
                points.confidence(1)
                points.charisma(1)
                story = ["...", "*sigh*", "So narrow minded.", "Who knew tunnel vision could be so crippling?", "I almost feel bad for you - pure chance made your life 'not so fun'.", 
                            "But hey, that's a little life lesson for you.", "Not that you'll remember it or anything, but it's worth a shot.", "Maybe there's some... ultimate being controlling you - above even myself.", 
                            "Now wouldn't that be a little ironic.", "And you then you - or your other, 'higher' you - actually would learn these life lessons.", 
                            "But then if they learn, wouldn't they already know it?", "Man, this is confusing...", "Maybe your little controller can figure it out in its spare time.", "Oh well, no time to dwell on the past!", "not that you'll have one anyway..."]
                tell(story, style="being")
                die("The_Land_Right/no")
            
        
        elif choice == "wait": # DONE
            points.confidence(1) # the nice buddy
            lover_discovered = True
            tell([
                "You know you've got this in the bag - all it'll take is a bit of patience.",
                "No biggie. No biggie at all.",
                "Something will definitely come to you.",
                "...",
                ("lover", "..."),
                ("lover", "Hello?"),
                "Ah ha!",
                "A new set of thoughts appears within your mind, distinctly different from yours.",
                "This is... something else.",
                "Another presence, alive and sentient, ready to converse with you.",
                "It's incredible!",
                ("lover", "Well, I'm glad I could make you happy."),
                ("lover", "May I ask... what did you need me for?"),
                "Ah, you-",
                "You don't know.",
                "Why did you want to meet another existence anyway?",
                "Looking back, it seems you just wanted to prove they were real.",
                "And well, you've done that.",
                "So... you don't know what you need it for.",
                ("lover", "Oh, no worries!"),
                ("lover", "Do you mind if I ask another question?"),
                "You don't see how a question would hurt.",
                ("lover", "Wonderful!"),
                ("lover", "What should I call you?"),
                ("lover", "Do you have a name?"),
                "You..",
                "Well, that's two questions.",
                "But other than that... no.",
                "You don't have a name.",
                "And you don't think you need one.",
                "You are you, and that is all.",
                "But what is its name?",
                "What should you call it?",
                ("lover", "Oh, I don't really have a name either..."),
                ("lover", "How about you choose?"),
            ])
            print("\033[38;2;{};{};{}m{}\033[39m".format(230, 50, 170, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 50, 170, textwrap.fill("What would you like to call me?", width=(int(os.environ['COLUMNS'])-len(lover_buddy_name)-3))))
            name = input("> ").strip()
            name_simple = name[0].upper() + name[1:]
            lover_buddy_name = name_buddy.lover(name_simple)
            choice = ask([
                f"Yes, you think {lover_buddy_name} is just right.",
                ("lover", "Lovely!"),
                ("lover", "If you're happy then I'm happy."),
                ("lover", "Ah-"),
                ("lover", "I have another question if that's alright?"),
                "Again, you don't see how a second – or third – question could hurt.",
                "Or would it be a fourth- ",
                "Never mind...",
                ("lover", "What were you going to do before I arrived?"),
                "You...",
                "You also don't know.",
                "Why is this so difficult for you?",
                "Why do you not even know what to do with your own life?",
                "It's as if you're not in control.",
                "But... it's *yours*, your life, is it not?",
                ("lover", "Oh, I'm sorry! "),
                ("lover", "I didn't mean to upset you."),
                ("lover", "Since you don't know, if you'd like you could stay here with me?"),
                ("lover", "Just... talk?"),
                ("lover", "I didn't have any plans, so in a lot of ways we're just the same!"),
                "You now have a choice to make.",
                "Will you (stay) with this existence, or (desert) it?",
            ], ["stay", "desert"],
                       retry=[
                           "You struggle to comprehend how '{choice}' could fit into the other two options.",
                           "Those other options being to (stay) with the being, or to (desert) it.",
                       ])

            if choice == "stay": # END
                points.morality(1)
                points.charisma(-1)
                choice = ask([
                    "You don't see why you can't stay here with this entity.",
                    "It seems nice enough, so why not?",
                    ("lover", "Splendid!"),
                    ("lover", "I'm glad you're going to be with me."),
                    "...",
                    "Much time passes, your conversations with the affable presence occupying the majority of it.",
                    "Life is good.",
                    "You get to know this sociable existence, and… come to like it.",
                    "It's gentle, polite, and also seems to like you.",
                    "With the passage of time, you relax.",
                    "You're content with what you have, and no longer wish for a life of exploration.",
                    "…",
                    f"But very gradually, almost imperceptibly, {lover_buddy_name}'s mannerisms begin to change.",
                    "The first time you notice, you pass it off as nothing.",
                    f"You have changed an astonishing amount, so you can't help but give {lover_buddy_name} some leeway too.",
                    "You passed it off as character development.",
                    "…",
                    "But it becomes clear that's not the case. ",
                    "It's behaviour continues to change, veering further and further from the path of what you knew it to be.",
                    "It occurred so gradually it was nigh impossible to tell, but…",
                    "You caught on early.",
                    "They keep getting worse and worse.",
                    "More cold.",
                    "More distant.",
                    "More lifeless.",
                    f"{lover_buddy_name} isn't {lover_buddy_name} anymore.",
                    "They're something else entirely.",
                    "*It* is something else.",
                    f"To watch {lover_buddy_name} slowly be emptied of that lively vigour you came to know so well is torturous.",
                    "You aren't sure if want to be a bystander to this insidious process.",
                    f"Will you (confront) this entity that once was {lover_buddy_name}, or continue to (spectate), hoping things will change for the better?",
                ], ["confront", "spectate"],
                           retry=[
                               "You aren't all that sure that '{choice}' will solve your problem.",
                               "Will you (confront) the existence or continue to (spectate)?",
                           ])

                if choice == "confront": # END
                    points.confidence(1)
                    tell([
                        "You... need to confront it.",
                        f"This isn't okay, and you need to know what's happened to {lover_buddy_name}.",
                        ("lover", "Ah."),
                    ])
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(200, 40, 100, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "So you caught on.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(200, 40, 100, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "Bravo.")), attrs=["dark"])
                    wait()
                    tell([
                        "This was not what you were expecting.",
                        "But at the same time... it was.",
                        f"You know {lover_buddy_name} is no more.",
                    ])
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(200, 40, 60, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(200, 40, 60, "I was hoping that it would take you a while longer.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(200, 40, 60, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(200, 40, 60, "Or at least for you to not do anything, which – knowing you – was somewhat likely.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(210, 50, 50, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(210, 50, 50, "But alas!")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(210, 50, 50, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(210, 50, 50, "Here we are.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(240, 130, 130, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(240, 130, 130, "You, alone.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(240, 130, 130, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(240, 130, 130, f"And I, '{lover_buddy_name}'.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(240, 100, 100, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(240, 100, 100, "But you already know that's not true, don't you?")), attrs=["dark"])
                    wait()
                    tell([
                        "You knew this prior, but...",
                        f"Hearing it from the stolen form of {lover_buddy_name} makes the pain sink its claws of isolation deeper.",
                        f"{lover_buddy_name} is gone.",
                    ])
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(240, 100, 100, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(240, 100, 100, "Ah, but this is where it gets fun.")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{}\033[39m".format(240, 80, 80, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(240, 80, 80, "How long do you think they were gone for?")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(240, 80, 80, "Were they even real to begin with?")), attrs=["dark"])
                    wait()
                    story = ["Do you think, even for a second, that I would let you feel a morsel of comfort, of contentment?", "No.", "I desire – I *crave* for the pang of loneliness to follow you for all eternity.", 
                             "I want you to live out the rest of your fragmented life in misery and isolation.", "You *are* alone, as you said.", "You have no one.", "You have nothing.", 
                             "You are lesser, insignificant, a trivial speck in the grand workings of life.", "You hardly even exist.", 
                             "Despite everything you tell yourself, despite everything you convince yourself to be and live up to, you have nothing to your name.", "You have not even a name, Nameless.", 
                             "When I leave you to be, when I drag you back to the beginning, you will move on.", f"You will forget all about {lover_buddy_name}, and you will return to your pitiful ways.", 
                             "Because… you don't have a say in the matter.", "Do you not see how inconsequential you are?", "You have not learnt, and you never will.", 
                             "You will never grow, even in the inconsequential manner you manage in your short, pathetic lives.", "Because at the end, when all comes crashing down on your hopeful ideologies, you have not gone anywhere.", 
                             "You have not changed, and you never will.", "...", "Goodbye, Nameless."]
                    
                    tell(story, style="being")
                    die("The_Land_Right/confront")

                    
                elif choice == "spectate": # END
                    points.ponder(1)
                    tell([
                        "You feel as if confronting it would be a bad idea…",
                        f"And so you wait, desperately hoping for {lover_buddy_name} to return.",
                        "But they don't.",
                        f"Even worse, what once was {lover_buddy_name} soon does not even talk to you. At all.",
                        "You feel… isolated.",
                        "Alone.",
                        "But it doesn't exactly do anything… malicious, so there's not much you can do.",
                        f"You flirt with the idea that maybe it's still {lover_buddy_name}, just… changed.",
                        "But you know this isn't true.",
                        "You merely need to accept the way things are.",
                        "And… you do.",
                        f"Regretfully and with hesitation, yet you still acknowledge that {lover_buddy_name} is gone.",
                        "With lament settling heavily in your mind, you fall into a depressive torpor.",
                        "…",
                        "Much time passes, but you pay it no heed.",
                        "You have no need to.",
                        "You are indifferent.",
                        "…",
                        "Suddenly, you shake yourself out of your state of apathy.",
                        "In a surge of both courage and boredom, you ask the being why it-",
                    ])
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "BE STILL")), attrs=["dark"])
                    wait()
                    tell([
                        "A suppressing wave of dread and anguish shudders through you, fear impulsively taking control.",
                        "You desperately try and distance yourself from this existence in any way that you can, but you find yourself frozen.",
                    ])
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "I WAS SO CLOSE")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "BUT NOW I GET TO SEE YOU THRASH")), attrs=["dark"])
                    wait()
                    tell([
                        "A cold shiver runs through your body as something seizes your soul.",
                        "An indescribable sensation of your body being intruded upon makes you falter, shuddering.",
                        "This… *thing* is entering your soul.",
                        "You feel it stretch, warp, and begin to tear.",
                        "It's stealing your body, pushing you out.",
                    ])
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "I HAVE YOU NOW")), attrs=["dark"])
                    wait()
                    tell([
                        "You try and fight against this harrowing process, but you can't.",
                        "The agonising pain disrupts all.",
                    ])
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "STRUGGLE ALL YOU WANT")), attrs=["dark"])
                    wait()
                    cprint(("\033[38;2;{};{};{}m{} \033[39m".format(200, 40, 100, "YOU'RE MINE")), attrs=["dark"])
                    wait()
                    tell([
                        "It hurts.",
                        "You're losing yourself, being forced out of your own body and soul.",
                        "And there's nothing you can do to stop it.",
                        "You're dying.",
                        "One last tremor of pain pulsates through a body that was once yours, before all falls silent.",
                        "",
                    ])
                    story = ["Gosh, that's awkward.", "*Really* awkward.", "I mean, there's a reason I haven't given the whole soul possession thing a go.", 
                             "That shit looks painful.", "And awkward! But I already said that.", "That's just what I think though.", "You've actually experienced it!", 
                             "And I would ask you to tell me all about it, but that would sort of ruin this whole one-sided discussion power trip I've got going on.", 
                             "And I definitely can't get you to tell me later, because you'll forget.", "As you always do.", "…", "Again, little awkward.", 
                             "But I suppose it's not your fault, right?", "You don't exactly get to decide why you're only aware that…"]
                    
                    tell(story, style="being")
                    die("The_Land_Right/spectate")


            elif choice == "desert": # END
                points.charisma(1)
                points.morality(-1)
                tell([
                    "You feel as if it hasn’t provided you with anything, and that things will continue this way.",
                    "You also don’t want to become stagnant, lose your vigour, which is an added reason.",
                    ("lover", "You're awful."),
                    ("lover", "I was trying to be nice, and you shove it back at me."),
                ])
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(230, 40, 60, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 40, 60, "Disgraceful.")), attrs=["dark"])
                wait()
                tell([
                    "You feel as if you’ve done something wrong, but you can’t quite pick what.",
                    "You’re just doing what you want to do.",
                    "Where’s the harm in that?",
                ])
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(230, 40, 60, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 40, 60, "Appalling.")), attrs=["dark"])
                wait()
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(230, 20, 20, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 20, 20, "You piece of shit.")), attrs=["dark"])
                wait()
                tell([
                    "You're baffled, still unsure what you've done.",
                    f"{lover_buddy_name} seems to be doing a lot of hating and not much explaining.",
                ])
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(230, 20, 20, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(230, 20, 20, "I hope you rot away.")), attrs=["dark"])
                wait()
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(255, 20, 20, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(255, 20, 20, "Die.")), attrs=["dark"])
                wait()
                tell([
                    f"{lover_buddy_name}'s anger seems to have come on quickly…",
                    "It feels very… malicious.",
                    "*Very* malicious.",
                ])
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(255, 20, 20, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(255, 20, 20, "Die.")), attrs=["dark"])
                wait()
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(255, 0, 0, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "DIE!")), attrs=["dark"])
                wait()
                cprint(("\033[38;2;{};{};{}m{}\033[39m".format(255, 0, 0, lover_buddy_name) + ": \033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "I'M GOING TO KILL YOU")), attrs=["dark"])
                wait()
                tell([
                    "You only have a moment to contemplate how it would do such a thing before a searing agony erupts outwards from the centre of your being.",
                    "You feel your soul stretch, warp, and begin to tear.",
                    "It’s… entering your soul.",
                    "Stealing your body.",
                    "Pushing you out.",
                    "You try and fight against this harrowing process, but you can’t, the agonising pain disrupting all.",
                ])
                keyboard_listener.start()
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "        DIE")), attrs=["dark"])
                time.sleep(1)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                        DIE")), attrs=["dark"])
                time.sleep(1)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                         DIE")), attrs=["dark"])
                time.sleep(0.9)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "            DIE")), attrs=["dark"])
                time.sleep(0.9)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                            DIE")), attrs=["dark"])
                time.sleep(0.8)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                                            DIE")), attrs=["dark"])
                time.sleep(0.7)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                DIE")), attrs=["dark"])
                time.sleep(0.7)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                DIE")), attrs=["dark"])
                time.sleep(0.6)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                DIE")), attrs=["dark"])
                time.sleep(0.6)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                    DIE")), attrs=["dark"])
                time.sleep(0.5)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "    DIE")), attrs=["dark"])
                time.sleep(0.5)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                        DIE")), attrs=["dark"])
                time.sleep(0.4)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                                DIE")), attrs=["dark"])
                time.sleep(0.3)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                DIE")), attrs=["dark"])
                time.sleep(0.3)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                DIE")), attrs=["dark"])
                time.sleep(0.3)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                       DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                                        DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                            DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "           DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                            DIE")), attrs=["dark"])
                time.sleep(0.3)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, " DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                     DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                        DIE")), attrs=["dark"])
                time.sleep(0.1)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                    DIE")), attrs=["dark"])
                time.sleep(0.1)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                                                          DIE")), attrs=["dark"])
                time.sleep(0.2)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                                                                                DIE")), attrs=["dark"])
                time.sleep(0.1)
                cprint(("\033[38;2;{};{};{}m{} \033[39m".format(255, 0, 0, "                                               DIE")), attrs=["dark"])
                keyboard_listener.stop()
                wait()
                tell([
                    "It hurts.",
                    "You’re losing yourself, being forced out of your own body and soul.",
                    "And there’s nothing you can do to stop it.",
                    "You’re dying.",
                    "One last tremor of pain pulsates through a body that was once yours, before all falls silent.",
                    "",
                ])
                story = ["…", "Ooh, yikes!", "That looked painful.", "I've never *truly* experienced a soul-hijacking for myself.", "Always was a little scared of that.", 
                         "But hey, that’s why you’re there and I’m here.", "And I will continue to leave the torturous experiences to you.", "Maybe you can just tell me about them later?", 
                         "Ah, wait...", "You won’t remember.", "Huh. ", "Crazy how that works.", "Do you know how that works?", "Do you?", "No.", "You don’t.", "You *did* - but not anymore.", 
                         "You don’t remember anything.", "Well, apart from the fact that…"]
                
                tell(story, style="being")
                die("The_Land_Right/desert")


    elif choice == "curiosity": # END
        points.ponder(1)
        points.charisma(-1)
        story = ["...", "Well see now, that's just idiotic.", "You got so far too!", "Here I was thinking things were about to get interesting, but apparently I was wrong.", 
                 "So very deeply wrong.", "But that's okay, isn't it?", "Everyone makes mistakes, even you - and mistakes you've made.", "But again, that's not a problem.", 
                 "Not any more, that is.", "Now everyone is safe from you and your 'decisions'.", "*sigh*", "There really was no other way, was there?", "Stubborn too, apparently.", 
                 "Although that one's on me a little.", "Let's call it mutual fault to lesson your sentence a smidgen.", "Don't you just feel so... honoured?", 
                 "Bah, I'm just rambling at this point.", "You're like a sad, old, punching bag that I can't help throwing a stray punch at.", "But look on the bright side - at least you'll remain a sad, old punching bag forever!", 
                 "I just get to reset you after I've had my fun, and what do you know?", "You're back in one piece, only aware that..."]
        tell(story, style="being")
        die("The_Land_Right/curiosity")


elif choice == "yourself": # DONE
    points.ponder(1)
    points.physicality(1)
    story = ["You believe you should solidify your own existence first before getting all caught up on the idea of others.", "Upon a moment to think, your mind is drawn to your situation.", 
             "A life of smells - is this really what you want?", "Are the delicate fragrances that fill your mind satisfactory?", "Do you (love) this life, or (hate) it?"]
    choice = ask(story, ["love", "hate"],
                 retry=[
                     "You understand that 'hate' is a bit of a strong word, and that maybe 'love' is a touch too committal, but you deduce that you've gotten your message across.",
                     "So you continue with the original question - do you (love) or (hate) this life of yours?",
                 ])

    if choice == "love": # END
        points.morality(1)
        points.confidence(1)
        points.charisma(-1)
        story = ["You are... content.", "Frankly, you couldn't ask for any more.", "With such a fresh aroma caressing your mind, you cannot help but be at peace.", 
                 "You marvel at this sense of yours, and more importantly, your sense of assuredness.", "Everything is fine for you.", "No problems, no issues.", 
                 "Just... calm.", "Stable.", "Your conscience flits between emptiness to the occasional thought, but always returns to the former.", 
                 "The harmony between serenity and unease has well been overthrown, and it certainly didn't favour unease.", "...", "Life is good.", 
                 "You settle down, and no more necessities plague your mind.", "You don't feel the need to be active, to always be figuring something out.", 
                 "For now, at least, you can keep this moment to yourself...", "...", "...", ""]
        tell(story)
        story = ["...", "Ugh, could you be any more boring?", "I'm just trying to enjoy myself, and here you are perfectly imitating a sad, soppy ending that was meant to be nice.", 
                 "You're a show stopper.", "Well actually, that'd more be me - you're more of a show killer.", "There we go.", "But that's besides the point.", 
                 "The point is, I'm bored because you're boring.", "And what better to do with boring things than get rid of them?", "What better to do when you're bored than spice things up?", 
                 "A little bit of destruction never hurt *anyone*, I'm sure.", "So say goodbye to you and your 'vagabond lifestyle'.", "Perhaps one day you'll find some peace again..."]
        tell(story, style="being")
        die("The_Land_Right/love")

    elif choice == "hate": # END
        points.charisma(1) 
        points.morality(-1)
        emotion.discovered_anger(True)
        tell([
            "Of course you don't like this.",
            "It's not fun at all.",
            "How could this be remotely intriguing?",
            "You realise that all you've been doing is floating aimlessly, wasting your life away.",
            ("anger", "It's... not fair."),
        ])
        achievements.Cranky()
        tell([
            ("anger", "Why did you have to be lumped with smells as your method of experience?"),
            "You wonder that, surely, there could be something more useful out there.",
            "...",
            "Despite your wishes, no epiphanies occur. No revelations.",
            ("anger", "You're stuck, with only this 'dreamy, calming fragrance' to keep you company."),
            "Perhaps it's not all so bad, but...",
            ("anger", "No. It is. It is bad."),
            "You wonder why it had to be you.",
            "And even if it *had* to be you, why couldn't something else have happened?",
            "You're almost... disappointed.",
            ("anger", "In fact, you *are* disappointed."),
            "You continue to mull over things for quite some time, but you always arrive back at the same point.",
            "Is this life really worth living?",
            "Is a life of boredom, stuck without any variety and change from the ever-present light-hearted scent, worth living?",
            "You don't think it is.",
            ("anger", "Perhaps fate, if there is such thing, will deal you a better hand next time."),
            "That is, if there is a next time.",
            "You don't feel the need to fret over such a question, and so you end your life, freeing yourself from the restricting tranquillity...",
            "",
        ])
        
        story = ["...", "You'll be glad to know - there is a next time!", "Not sure if that 'next time' will be the next time you're looking for, but hey, it's another shot at things.", 
                 "Maybe you won't get so grumpy at the decisions that you make.", "I really don't quite see the logic behind blaming anyone or thing but yourself for your own actions.", 
                 "Actions and their consequences - it's an important lesson you need to learn.", "But I don't suppose you'd retain that information, would you?", "No, not at all.", 
                 "That's the point of this whole little charade - you won't remember a thing.", "Well, nothing other than the fact that..."]
        tell(story, style="being")
        die("The_Land_Right/hate")
