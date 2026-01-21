import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase
        if lower_var.get():
            chars += string.ascii_lowercase
        if number_var.get():
            chars += string.digits
        if symbol_var.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Password Generator")
root.geometry("320x350")
root.resizable(False, False)

title = tk.Label(root, text="PASSWORD GENERATOR", font=("Arial", 14, "bold"))
title.pack(pady=10)

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root, width=10, justify="center")
length_entry.pack(pady=5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Numbers", variable=number_var).pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack(anchor="w", padx=60)

tk.Button(root, text="Generate Password", bg="green", fg="white",
          command=generate_password).pack(pady=10)

result_entry = tk.Entry(root, width=30, justify="center")
result_entry.pack(pady=5)

tk.Button(root, text="Copy Password", bg="blue", fg="white",
          command=copy_password).pack(pady=10)

root.mainloop()