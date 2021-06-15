# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creating the window , adding a title and sizing it
window = Tk()
window.title("BANKING DETAILS")
window.geometry("500x300")
window.config(bg="grey")
window.resizable(0, 0)


def function():
    window.destroy()
    import Convert


lbl_account_holder = tk.Label(window, text="ACCOUNT HOLDER NAME: ", fg="white", bg="grey")
lbl_account_holder.grid(row=0, column=1, padx=20, pady=20)

account_holder_ent = tk.Entry(window, bg="white")
account_holder_ent.grid(row=0, column=2, padx=10, pady=10)

lbl_account_number = tk.Label(window, text="ACCOUNT NUMBER: ", fg="white", bg="grey")
lbl_account_number.grid(row=1, column=1, padx=20, pady=20)

account_number_ent = tk.Entry(window, bg="white")
account_number_ent.grid(row=1, column=2, padx=10, pady=10)

lbl_bank_name = tk.Label(window, text="NAME OF BANK: ", fg="white", bg="grey")
lbl_bank_name.grid(row=2, column=1, padx=20, pady=20)

bank_name_ent = ttk.Combobox(window)
bank_name_ent["values"] = "Select-- ABSA CAPITEC FNB STANDARD NEDBANK"
bank_name_ent.current(0)
bank_name_ent.grid(row=2, column=2)

convert_btn = tk.Button(window, text="CONVERT", width=10,  relief="raised", borderwidth=4, height=1, command=function)
convert_btn.grid(row=3, column=1, padx=20, pady=20)

submit_btn = tk.Button(window, text="SUBMIT", width=10,  relief="raised", borderwidth=4, height=1)
submit_btn.grid(row=3, column=2, padx=20, pady=20)

window.mainloop()

