import tkinter as tk
from tkinter import ttk

def on_submit():
    name = name_entry.get()
    age = age_entry.get()
    address = address_text.get("1.0", "end-1c")  # Retrieve text from the Text widget

    result_label.config(text=f"Name: {name}, Age: {age}, Address: {address}")

root = tk.Tk()
root.title("Personal Information Form")
root.configure(background='#FA86C4')

style = ttk.Style()
style.configure('TLabel', font=('Verdana', 12), padding=5, foreground='black', background='#9E4244')
style.configure('TEntry', font=('Verdana', 12), padding=5, foreground='black', background='##9E4244')
style.configure('TButton', font=('Verdana', 12), padding=5, foreground='black', background='#9E4244')

name_label = ttk.Label(root, text="Name:",)
name_label.grid(row=0, column=0, padx=10, pady=15, sticky='w')

name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

age_label = ttk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

age_entry = ttk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

address_label = ttk.Label(root, text="Address:")
address_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

address_text = tk.Text(root, height=4, width=30)
address_text.grid(row=2, column=1, padx=10, pady=5, sticky='w')

submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
