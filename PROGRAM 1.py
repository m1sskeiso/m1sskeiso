import tkinter as tk
from tkinter import messagebox
from turtle import window_height, window_width
from webbrowser import BackgroundBrowser

def calculate_total_amount(apples, oranges):
    apple_price = 20
    orange_price = 25

    total_amount = (apples * apple_price) + (oranges * orange_price)
    
    # Display the output in a pop-up window
    messagebox.showinfo("Total Amount", f"You need to pay {total_amount} pesos.")

def on_submit():
    try:
        apples = int(apple_entry.get())
        oranges = int(orange_entry.get())
        
        calculate_total_amount(apples, oranges)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Marck's Fruit Shop")
root.configure(background='#FD5DA8')

window_width = 400
window_height = 200
root.geometry(f"{window_width}x{window_height}")

apple_entry = tk.Label(root, text="How many apples do you want to buy?", font= ('Verdana')).pack()
apple_entry = tk.Entry(root)
apple_entry.pack(padx=20, pady=20)

tk.Label(root, text="How many oranges do you want to buy?", font= ('Verdana')).pack()
orange_entry = tk.Entry(root)
orange_entry.pack(padx=20, pady=20)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(padx=20)

root.mainloop()
