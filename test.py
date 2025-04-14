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

r = IntVar()
def test(window, number, letter):
    frame = tk.Frame(window)
    frame.pack(padx=30, pady=10)

    entre = tk.Entry(frame,width=50)
    entre.pack(side="left")
    entre.insert(0, "enter answer here: ")

    radio_but = Radiobutton(frame, variable=r, value=number)
    radio_but.pack(side="left")

    letter = tk.Label(frame, text=letter, font="Arial, 12")
    letter.pack(side="left")

    return frame

test_text1 = test(window, 1, "A")
test_text2 = test(window, 2, "B")
test_text3 = test(window, 3, "C")
test_text4 = test(window, 4, "D")

button1 = tk.Button(window, text="Save")
button1.pack()

button2 = tk.Button(window, text="Next")
button2.pack()

button3 = tk.Button(window, text="Stop")
button3.pack()






window.mainloop()

















