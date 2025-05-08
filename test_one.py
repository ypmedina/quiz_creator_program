import tkinter as tk
from tkinter import Radiobutton, IntVar
import os
import json

desktop_path = os.path.join(os.path.expanduser("~"), "Documents", "user_quiz_GUI.json")

try:
    with open(desktop_path, 'r', encoding='utf=8') as file:
        quiz_data = json.load(file)

except FileNotFoundError:
    print("The file is not found. Please make sure to save the quiz")
    exit()

window = tk.Tk()

bg_color = "#fff9ed"
main_color = "#f5fcd1"
font_color = "#f5fcd1"

window.geometry("900x600")
window.configure(bg=bg_color)

header_frame = tk.Frame(window, height=50, bd=1, bg='#fff9ed')
header_frame.pack(fill='x')

header_label = tk.Label(header_frame, text='Quiz maker', font='Arial, 60', bg='#fff9ed')
header_label.pack(anchor="w")


window.mainloop()
