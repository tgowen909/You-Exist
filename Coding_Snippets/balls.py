import tkinter as tk

# Creates window
window = tk.Tk()
window.geometry('700x350')

# Creates text widget
text = tk.Text(window)
 
# Put it on the screen
text.pack()
 
# Inserts text into the text widget
text.insert()

window.mainloop()
