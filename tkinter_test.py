import tkinter as tk


import os
os.system("clear")

def test():
    print("This is a test")

root = tk.Tk()

# Making the canvas(frame)
canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

# Making a fram
frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.4, relheight=0.8, relwidth=0.8)

# Making a button
button1 = tk.Button(frame, text="Hello", command=test)
button1.place(relx=0, rely=0, relheight=0.05, relwidth=0.1)

button2 = tk.Button(frame, text="Hello", command=test)
button2.place(relx=0, rely=0.1, relheight=0.05, relwidth=0.1)

button3 = tk.Button(frame, text="Hello", command=test)
button3.place(relx=0, rely=0.2, relheight=0.05, relwidth=0.1)

# Making a label
label = tk.Label(frame, text="test")
label.place(relx=0, rely=0.3, relheight=0.05, relwidth=0.1)

# Making a textbox
txtbox = tk.Entry(frame)
txtbox.place(relx=0.1, rely=0)


root.mainloop()