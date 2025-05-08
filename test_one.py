import tkinter as tk
from tkinter import messagebox
import os
import json

window = tk.Tk()

bg_color = "#fff9ed"
main_color = "#f5fcd1"
font_color = "#f5fcd1"

window.geometry("900x600")
window.configure(bg=bg_color)

header_frame = tk.Frame(window, height=50, bd=1, bg='#fff9ed')
header_frame.pack(fill='x')

header_label = tk.Label(header_frame, text='Quiz', font='Arial, 60', bg='#fff9ed')
header_label.pack(anchor="w")
desktop_path = os.path.join(os.path.expanduser("~"), "Documents", "user_quiz_GUI.json")

try:
    with open(desktop_path, 'r', encoding='utf=8') as file:
        quiz_data = json.load(file)

except FileNotFoundError:
    print("The file is not found. Please make sure to save the quiz")
    exit()


questions = quiz_data["questions"] #from kson
question_number = 0
current_number = 0
score = 0

question_var = tk.StringVar()
selected = tk.IntVar()
answer_vars = [tk.StringVar() for _ in range(4)]

def load_question():
    q = questions[question_number]
    question_var.set(f"Q{question_number+1}: {q['question']}")
    for i in range(4):
        answer_vars[i].set(q["answers"][i])
    selected.set(0)


def next_question():
    global current_number, score
    if selected.get() == questions[current_number]["correct"]:
        score += 1
    current_number += 1
    if current_number < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Complete", f"{quiz_data['name']}'s Quiz\nScore: {score}/{len(questions)}")
        window.destroy()

tk.Button(window, text="Next", command=next_question).pack(pady=20)





tk.Label(window, bg='#fff9ed' , textvariable=question_var, font=("Arial", 16), wraplength=550).pack(pady=20)

for i in range(4):
    tk.Radiobutton(window,bg='#fff9ed', textvariable=answer_vars[i], variable=selected, value=i+1, font=("Arial", 12)).pack(anchor="w", padx=50)

load_question()
window.mainloop()
