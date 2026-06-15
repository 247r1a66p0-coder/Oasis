import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length must be at least 4"
            )
            return

        characters = ""

        if var_upper.get():
            characters += string.ascii_uppercase

        if var_lower.get():
            characters += string.ascii_lowercase

        if var_digits.get():
            characters += string.digits

        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror(
                "Error",
                "Select at least one character type"
            )
            return

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except:
        messagebox.showerror(
            "Error",
            "Invalid input"
        )

def copy_password():

    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard"
        )

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=var_upper
).pack()

tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=var_lower
).pack()

tk.Checkbutton(
    root,
    text="Numbers",
    variable=var_digits
).pack()

tk.Checkbutton(
    root,
    text="Symbols",
    variable=var_symbols
).pack()

tk.Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=10)

password_entry = tk.Entry(root, width=35)
password_entry.pack()

tk.Button(
    root,
    text="Copy Password",
    command=copy_password
).pack(pady=10)

root.mainloop()