import tkinter
import os
from subprocess import call
import threading

window = tkinter.Tk()
window.title("GUI")

def clicked():
    #os.system('python inference.py')
    #os.system('python extract_frames.py')

    # I used the threading approach 

    threading.Thread(target=call, args=("You_Exist.py" ,), ).start()

bt = tkinter.Button(window,text="Click Here to start detecting",command=clicked).pack()

window.geometry('400x400')
window.mainloop()