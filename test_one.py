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

header_label = tk.Label(header_frame, text='Quiz', font='Arial, 60', bg='#fff9ed')
header_label.pack(anchor="w")


def question(var, entry_text, border, outline):
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=10)

    entry = tk.Entry(frame, width=15, font='Arial, 12', bd=border, relief=outline)
    entry.pack(side='left')
    entry.insert(var, entry_text)

    text = tk.Text(frame, height=1, width=50, font='Arial, 12', bd=border, relief=outline)
    text.pack(side='left')

    return text

question_num = 1
qstn_display = question(0, f'Question {question_num}:', 1, 'solid')
question_num += 1



window.mainloop()
