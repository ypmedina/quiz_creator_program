"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d)
and the correct answer.Write the collected data to a text file.
Ask another question until the user chose to exit.
"""

#use the function open() to create the text file

#ask the user for their name, after asking the user for their name, display text that will prompt them to
#write a quiz question and let the user input 4 different answers to the question with 1 being the correct
#answer.

#make a "Next question" functionality using the while loop, make it go on until the user tells the program
#to stop.


import tkinter as tk
from tkinter import Radiobutton, IntVar

window =tk.Tk()
#Make a save, exit, and next button
#Do checkboxes for the correct answer picking
#Window design: Header-#f5fcd1, background-#fff9ed, font color-#c
bg_color = "#fff9ed"
main_color = "#f5fcd1"
font_color = "#f5fcd1"

window.geometry("900x600")
window.configure(bg=bg_color)

#buttons first
#question, answer1, answer2, answer3, answer4, checkboxes, next, save and stop
#5 input fields, 3 buttons, 4 radio buttons(Replacement for checkbox)

entry1 = tk.Entry(window, width=50)
entry1.pack()
entry1.insert(0,"Enter your name: ")

entry2 = tk.Entry(window, width=50)
entry2.pack()
entry2.insert(0,"Enter a quiz question: ")

entry3 = tk.Entry(window, width=50)
entry3.pack()
entry3.insert(0,"Enter answer A: ")

entry4 = tk.Entry(window, width=50)
entry4.pack()
entry4.insert(0,"Enter answer B: ")

entry5 = tk.Entry(window, width=50)
entry5.pack()
entry5.insert(0,"Enter answer C: ")

entry6 = tk.Entry(window, width=50)
entry6.pack()
entry6.insert(0,"Enter answer D: ")


button1 = tk.Button(window, text="Save")
button1.pack()

button2 = tk.Button(window, text="Next")
button2.pack()

button3 = tk.Button(window, text="Stop")
button3.pack()

r = IntVar()

Radiobutton(window, text="A", variable=r, value=1).pack()
Radiobutton(window, text="B", variable=r, value=2).pack()
Radiobutton(window, text="C", variable=r, value=3).pack()
Radiobutton(window, text="D", variable=r, value=4).pack()









window.mainloop()

















