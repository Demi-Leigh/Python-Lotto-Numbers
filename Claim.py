# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk
from tkinter import ttk
import smtplib
from tkinter import messagebox
from playsound import playsound


# Creating the window , adding a title and sizing it
window = Tk()
window.title("BANKING DETAILS")
window.geometry("500x300")
window.config(bg="grey")
window.resizable(0, 0)
window.wm_iconify()


# Sends an email to user telling them they've won and confirming bank details
def submit():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email_id = 'demijay2323@gmail.com'
    receiver_email_id = email_add.get()
    password = "1a2a3a4a5a6a7a8a"
    s.starttls()
    s.login(sender_email_id, password)
    message = "CONGRATULATIONS\n"
    message = message + "You Have Won" + "\n" + "These are your bank details " + "\n" + account_holder_ent.get() + "\n" + account_number_ent.get() + "\n" + bank_name_ent.get()
    s.sendmail(sender_email_id, receiver_email_id, message)
    s.quit()
    messagebox.showinfo("LOTTO", "Thanks for playing, please check your emails")
    window.destroy()

# Tells user to use uppercase when converting currency


def function():
    playsound("click.mp3")
    messagebox.showinfo("NOTE", "Please Use UpperCase When Selecting Currencies!!")
    window.iconify()
    import Convert


# Labels and Entries for bank details to be entered
# Buttons to take user to conversion window and submit button to receive email
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

lbl_email = tk.Label(window, text="EMAIL: ", fg="white", bg="grey")
lbl_email.grid(row=3, column=1)

email_add = tk.Entry(window, bg="white")
email_add.grid(row=3, column=2)

convert_btn = tk.Button(window, text="CONVERT", width=10,  relief="raised", borderwidth=4, height=1, command=function)
convert_btn.grid(row=4, column=1, padx=20, pady=20)

submit_btn = tk.Button(window, text="SUBMIT", width=10,  relief="raised", borderwidth=4, height=1, command=submit)
submit_btn.grid(row=4, column=2, padx=20, pady=20)


window.mainloop()
