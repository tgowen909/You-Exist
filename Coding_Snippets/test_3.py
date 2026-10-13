import tkinter as tk
from tkterminal import Terminal
import os
import sys

sys.path.append("/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages")
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/termcolor")
root = tk.Tk()
terminal = Terminal(root)
root.title("Balls")

photo = tk.PhotoImage(file = 'Images/Icon.png')
root.wm_iconphoto(False, photo)

terminal.shell = True
terminal.basename = ""
terminal.pack(expand=True, fill='both')
print(os.getcwd())
terminal.run_command("python3 /Users/tobyowen/Documents/Coding/You\ Exist/You_Exist.py")
root.mainloop()

