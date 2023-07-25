# gui_program.py
import tkinter as tk
from tkinter import messagebox
import cli_program

def run_cli_program():
    input_value = entry.get()
    result = cli_program.cli_program(input_value)
    messagebox.showinfo("Result", f"CLI program returned: {result}")

app = tk.Tk()
app.title("GUI Program")

label = tk.Label(app, text="Enter input:")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Run CLI Program", command=run_cli_program)
button.pack()

app.mainloop()
