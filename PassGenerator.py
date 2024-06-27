import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, strength):
    if strength == "Weak":
        characters = string.ascii_lowercase
    elif strength == "Medium":
        characters = string.ascii_letters + string.digits
    else:  # Strong
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        strength = strength_var.get()
        password = generate_password(length, strength)
        result_label.config(text=f"Generated Password: {password}")
        result_label.password = password 
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    try:
        root.clipboard_clear()
        root.clipboard_append(result_label.password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    except AttributeError:
        messagebox.showerror("Error", "No password to copy!")

root = tk.Tk()
root.title("Colorful Password Generator")
root.geometry("500x450")
root.config(bg="#5F9EA0")

font_style = ("Helvetica", 12, "bold")

length_label = tk.Label(root, text="Enter the desired length for the password:", font=font_style, bg="#5F9EA0")
length_label.pack(pady=10)

entry = tk.Entry(root, font=font_style, justify='center')
entry.pack(pady=5)

strength_label = tk.Label(root, text="Select password strength:", font=font_style, bg="#5F9EA0")
strength_label.pack(pady=10)

strength_var = tk.StringVar(root)
strength_var.set("Medium")

radio_weak = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak", font=font_style, bg="#5F9EA0")
radio_medium = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium", font=font_style, bg="#5F9EA0")
radio_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong", font=font_style, bg="#5F9EA0")

radio_weak.pack(pady=5)
radio_medium.pack(pady=5)
radio_strong.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click, font=font_style, bg="#FFD700", activebackground="#FFA500")
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=font_style, bg="#5F9EA0", fg="#FF4500")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, font=font_style, bg="#90EE90", activebackground="#32CD32")
copy_button.pack(pady=10)

root.mainloop()
