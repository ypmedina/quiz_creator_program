"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d)
and the correct answer.Write the collected data to a text file.
Ask another question until the user chose to exit.
"""
import tkinter as tk
from tkinter import Radiobutton, IntVar

window =tk.Tk()

bg_color = "#fff9ed"
main_color = "#f5fcd1"
font_color = "#f5fcd1"

window.geometry("900x600")
window.configure(bg=bg_color)

header_frame = tk.Frame(window, height=50, bd=1, bg='#fff9ed')
header_frame.pack(fill='x')

header_label = tk.Label(header_frame, text='Quiz maker', font='Arial, 60', bg='#fff9ed')
header_label.pack(anchor="w")


def user_inp(var, entry_text, border, outline):
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=10)

    entry = tk.Entry(frame, width=15, font='Arial, 12', bd=border, relief=outline)
    entry.pack(side='left')
    entry.insert(var, entry_text)

    text = tk.Text(frame, height=1, width=50, font='Arial, 12', bd=border, relief=outline)
    text.pack(side='left')

    return text

name_entry = user_inp(0, 'Input name here:', 1, "solid")
question_entry = user_inp(0, 'input question here:', 1, "solid" )


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


quiz_items = []
def next_button():
    question = question_entry.get('1.0', 'end')
    answers = [ input_field1.get('1.0', 'end'),
                input_field2.get('1.0', 'end'),
                input_field3.get('1.0', 'end'),
                input_field4.get('1.0', 'end')
                ]
    correct_answer = r.get()
    if question and all(answers) and correct_answer:
        quiz_items.append({
            'question': question,
            'answers':answers,
            'correct':correct_answer
        })

    question_entry.delete('1.0', 'end')
    input_field1.delete('1.0', 'end')
    input_field2.delete('1.0', 'end')
    input_field3.delete('1.0', 'end')
    input_field4.delete('1.0', 'end')
    r.set(0)


def save_button():
    with open("user_quiz_GUI.txt", "w", encoding='utf-8') as file:
        name = name_entry.get('1.0', 'end')
        file.write(f"Name:{name}")
        for i in range(len(quiz_items)):
            q = quiz_items[i]
            file.write(f"Q{i+1}: {q['question']}\n")
            for j in range(len(q['answers'])):
                alphabet = chr(65 + j) #turn the IntVar values from r into letters(A,B,C,D)
                if (j + 1)  == q['correct']:
                    file.write(f"{alphabet}. {q['answers'][j]}(correct)\n")
                else:
                    file.write(f"{alphabet}. {q['answers'][j]}\n")


def exit_button():
    window.destroy()


button_frame = tk.Frame(window, bg='#fff9ed')
button_frame.pack(padx=40, pady=30)

save_btn = tk.Button(button_frame, text="Save", command=save_button)
save_btn.grid(row=0, column=0, pady=10, padx=20)

stop_btn = tk.Button(button_frame, text="Stop", command=exit_button)
stop_btn.grid(row=0, column=1, pady=10, padx=20)

next_btn = tk.Button(window, text="next", command=next_button, width= 20)
next_btn.pack(anchor='center')


window.mainloop()

















