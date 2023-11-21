import tkinter as tk
from tkinter import messagebox

def calculate_max_apples_and_remaining_money(money, apple_price):
    max_apples = int(money // apple_price)
    remaining_money = money % apple_price
    
    messagebox.showinfo("Result", f"With {money} pesos, you can buy {max_apples} apples.\nYou will have {remaining_money:.2f} pesos remaining.")

def on_submit():
    try:
        money = float(money_entry.get())
        apple_price = float(apple_price_entry.get())
        
        calculate_max_apples_and_remaining_money(money, apple_price)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Apple Purchase Calculator")
root.configure(background='#FD5DA8')

window_width = 400
window_height = 200
root.geometry(f"{window_width}x{window_height}")

tk.Label(root, text="Enter the amount of money you have:", font= ('Monospace')).pack()
money_entry = tk.Entry(root)
money_entry.pack(padx=20, pady=20)

tk.Label(root, text="Enter the price of an apple:", font= ('Monospace')).pack()
apple_price_entry = tk.Entry(root)
apple_price_entry.pack(padx=20, pady=20)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(padx=20)

root.mainloop()