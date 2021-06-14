# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk

# Creating the window , adding a title and sizing it
window = Tk()
window.title("LOTTO NUMBERS")
window.geometry("600x400")
window.config(bg="navy")
window.resizable(0, 0)


# Creating labels and entries for the user to input their name, email address,
# id number and address
lbl_name = tk.Label(window, text="ENTER NAME: ", fg="white",  bg="navy")
lbl_name.grid(row=0, column=1, padx=20, pady=20)

name_ent = tk.Entry(window, fg="black", bg="yellow")
name_ent.grid(row=0, column=2, padx=20, pady=20)

lbl_email = tk.Label(window, text="EMAIL ADDRESS: ", fg="white", bg="navy")
lbl_email.grid(row=1, column=1, padx=20, pady=20)

email_ent = tk.Entry(window, fg="black", bg="yellow")
email_ent.grid(row=1, column=2, padx=20, pady=20)

lbl_dob = tk.Label(window, text="D.O.B: ", fg="white", bg="navy")
lbl_dob.grid(row=2, column=1, padx=20, pady=20)

year_ent = tk.Entry(window, fg="black", bg="yellow", width=4)
year_ent.place(x=178, y=150)

month_ent = tk.Entry(window, fg="black", bg="yellow", width=4)
month_ent.place(x=240, y=150)

day_ent = tk.Entry(window, fg="black", bg="yellow", width=4)
day_ent.place(x=300, y=150)

lbl_address = tk.Label(window, text="ADDRESS: ", fg="white", bg="navy")
lbl_address.grid(row=3, column=1, padx=20, pady=20)

address_ent = tk.Entry(window, fg="black", bg="yellow")
address_ent.grid(row=3, column=2, padx=20, pady=20)

# Adding a button for the user to submit their information
confirm_btn = tk.Button(window, text="SUBMIT", relief="raised", borderwidth=4, bg="yellow", width=25, height=1)
confirm_btn.place(x=160, y=300)

# Function to check users age



window.mainloop()
