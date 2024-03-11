import tkinter as tk
import random


def usd_to_uah(amount, rate):
    return amount * rate


def uah_to_usd(amount, rate):
    return amount / rate


def update_rate():
    global usd_to_uah_rate
    usd_to_uah_rate = random.uniform(26, 28)  

def convert():
    amount = entry_amount.get()
    try:
        amount = float(amount)
        choice = option_menu_var.get()
        if choice == 'З Долара в Гривні':
            converted_amount = usd_to_uah(amount, usd_to_uah_rate)
            label_result.config(text=f"{amount} USD = {converted_amount:.2f} UAH")
        elif choice == 'З Гривні в Долар':
            converted_amount = uah_to_usd(amount, usd_to_uah_rate)
            label_result.config(text=f"{amount} UAH = {converted_amount:.2f} USD")
    except ValueError:
        label_result.config(text="Будь ласка, введіть число")


def check_input(char):
    return char.isdigit() or char == '.'


root = tk.Tk()
root.title("Конвертер валют")

usd_to_uah_rate = random.uniform(26, 28) 

label_amount = tk.Label(root, text="Введи число:")
label_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)
entry_amount.config(validate="key", validatecommand=(root.register(check_input), "%S"))

option_menu_var = tk.StringVar(root)
option_menu_var.set('З Долара в Гривні')
option_menu = tk.OptionMenu(root, option_menu_var, 'З Долара в Гривні', 'З Гривні в Долар')
option_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Порахувати", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

update_button = tk.Button(root, text="Оновити курс", command=update_rate)
update_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
