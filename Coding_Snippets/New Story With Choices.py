from You_Exist_Imports import * 


cp_emotion = True

size = os.get_terminal_size()
os.environ['LINES'] = str(size.lines)
os.environ['COLUMNS'] = str(size.columns)


story = []

for i, sentence in enumerate(story):
    print(sentence)
    if i < len(story) - 1:
        wait()
    else:
        choice = rp(input("> ").lower().strip())

        while choice != "" and choice != "":
            p("")
            print("")
            choice = rp(input("> ").lower().strip())

        if choice == "":
            story = ["", ""]
            
        elif choice == "":
            story = ["", ""]





################################## For killing off a branch
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






################################## For changing text colour within a dialogue


p("")
cp_emotion("") # for determined emotion
cprint("") # for not-defined colours
wait()
p("")
p("")
cprint("")
choice = rp(input("> ").lower().strip())

while choice != "" and choice != "":
    p("")
    print("")
    choice = rp(input("> ").lower().strip())

if choice == "":
    story = ["", ""]
    
elif choice == "":
    story = ["", ""]