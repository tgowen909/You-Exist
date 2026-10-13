import os

loneliness_discovered = False
happiness_discovered = False

### Functions ### 

def rp(inp):
    punctuation = "\'().,"
    for symbol in punctuation:
        inp = inp.replace(symbol, '')
    return inp

def wait():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\"'")

def p(text):
    print(text)
    wait()


### Emotions ###

def cp_loneliness(text):
    if loneliness_discovered == True:
        os.system('''printf "\x1b[38;2;128;128;128m''' + text + '''\x1b[0m\n"''')
        wait()
    else:
        print(text)
        wait()

def cp_happiness(text):
    if happiness_discovered == True:
        os.system('''printf "\x1b[38;2;255;255;0m''' + text + '''\x1b[0m\n"''')
        wait()
    else:
        print(text)
        wait()

