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
window = tk.Tk()

window.geometry("800x600")
window.title("Quiz maker")

label = tk.Label(window, text="Quiz maker", font="Arial, 16")
label.pack()

textbox = tk.Text(window, height=2, font="Arial, 16")
textbox.pack()

myentry = tk.Entry(window)
myentry.pack()

window.mainloop()




















