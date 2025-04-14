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

name_entry = tk.Entry(window, width=50)
name_entry.pack()
name_entry.insert(0,"Enter your name: ")

question_entry = tk.Entry(window, width=50)
question_entry.pack()
question_entry.insert(0,"Enter a quiz question: ")

r = IntVar()
def answer_inputs(window, number, letter):
    frame = tk.Frame(window)
    frame.pack(padx=30, pady=10)

    text = tk.Text(frame, height=1, width=50, font="Arial, 12")
    text.pack(side='left')

    radio_but = Radiobutton(frame, variable=r, value=number)
    radio_but.pack(side="left")

    letter = tk.Label(frame, text=letter, font="Arial, 12")
    letter.pack(side="left")

    return text

input_field1 = answer_inputs(window, 1, "A")
input_field2 = answer_inputs(window, 2, "B")
input_field3 = answer_inputs(window, 3, "C")
input_field4 = answer_inputs(window, 4, "D")

#Just append the inputs into a list then make the program write that list in the text file
#Append to the text file will only happen when the user presses "save"
#Develop the "next" button, only append when the question, all answers and the correct answer is recorded
#The correct answer is the radio button
#use the get() function of tkinter
#Use the 'command=' function of the buttons


quiz_items = []
def next_button():

    answers = [ input_field1.get('1.0', 'end'),
                input_field1.get('1.0', 'end'),
                input_field1.get('1.0', 'end'),
                input_field1.get('1.0', 'end')
                ]
    correct_answer = r.get()
    if question_entry and all(answers) and correct_answer:
        quiz_items.append({
            'question: ': question_entry,
            'answers: ':answers,
            'correct answer: ':correct_answer
        })

    print(quiz_items)

next_btn = tk.Button(window,text="next", command=next_button)
next_btn.pack()






button1 = tk.Button(window, text="Save")
button1.pack()



button3 = tk.Button(window, text="Stop")
button3.pack()






window.mainloop()

















