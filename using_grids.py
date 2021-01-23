import tkinter as tk


import os
from tkinter.constants import END
os.system("clear")

def clear():
    txtbox.delete(0, END)

root = tk.Tk()

# Making a label
label = tk.Label(root, text="Test")
label.grid(row=0, column=0)

# Making a textbox
txtbox = tk.Entry(root)
txtbox.grid(row=0, column=1)

# Making a button
button1 = tk.Button(root, text="Hello", command=clear)
button1.grid(row=1, column=0, columnspan=2, ipadx=100, padx=10)

root.mainloop()