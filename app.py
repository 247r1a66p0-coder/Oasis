import tkinter as tk
from tkinter import messagebox

from bmi_logic import (
    calculate_bmi,
    bmi_category
)

from database import save_data
from graph import show_graph

def calculate():

    try:
        name = name_entry.get()

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:

            messagebox.showerror(
                "Error",
                "Enter valid positive values"
            )

            return

        bmi = calculate_bmi(
            weight,
            height
        )

        category = bmi_category(bmi)

        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}"
        )

        save_data(
            name,
            weight,
            height,
            bmi
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )

root = tk.Tk()

root.title("Advanced BMI Calculator")

root.geometry("400x450")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

tk.Label(
    root,
    text="Name"
).pack()

name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(
    root,
    text="Weight (kg)"
).pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(
    root,
    text="Height (m)"
).pack()

height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate
).pack(pady=10)

result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 12)
)

result_label.pack(pady=10)

tk.Button(
    root,
    text="Show BMI Graph",
    command=show_graph
).pack(pady=10)

root.mainloop()