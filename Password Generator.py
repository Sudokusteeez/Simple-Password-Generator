import random
import tkinter as tk
from tkinter import messagebox

def generate_passwords():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,0123456789'
    number = int(number_entry.get())
    length = int(length_entry.get())
    
    if number <= 0 or length <= 0:
        messagebox.showerror("Error", "Please enter valid numbers for the number of passwords and length.")
        return
    
    passwords = []
    for _ in range(number):
        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)

    result_text.delete('1.0', tk.END)
    for password in passwords:
        result_text.insert(tk.END, f"{password}\n")

app = tk.Tk()
app.title("Password Generator")

number_label = tk.Label(app, text="How many passwords would you like to create?")
number_label.pack()
number_entry = tk.Entry(app)
number_entry.pack()

length_label = tk.Label(app, text="Password length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Passwords", command=generate_passwords)
generate_button.pack()

result_label = tk.Label(app, text="Generated Passwords:")
result_label.pack()
result_text = tk.Text(app, width=40, height=10)
result_text.pack()

app.mainloop()

