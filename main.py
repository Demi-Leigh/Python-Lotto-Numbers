# Demi-Leigh Jefferies class 1
import random
from tkinter import *
import tkinter as tk
from datetime import date
import rsaidnumber
from dateutil.relativedelta import relativedelta
from tkinter import messagebox
from playsound import playsound
from validate_email import validate_email

# Creating the window , adding a title and sizing it
window = Tk()
window.title("LOTTO NUMBERS")
window.geometry("600x400")
window.config(bg="navy")
window.resizable(0, 0)


def player_id():
    player_name = random.sample((1,20),1)
    player_name = str(player_name)

    file = open("players.txt", "a+")

    file.write("\n")

    file.write("Name: " + name_ent.get())

    file.write("\n")

    file.write("player_name" + player_name[1])

    file.write("\n")

    file.write("Email: " + email_ent.get())

    file.write("\n")

    file.write("ID: " + str(id_ent.get()))

    file.write("\n")

    file.write("Address: " + address_ent.get())

    file.write("\n")


# Function to retrieve id number
# Function to check users age


def validation():
    my_id = rsaidnumber.parse(id_ent.get())
    dob = my_id.date_of_birth
    age = relativedelta(date.today(), dob.date())
    print(age.years)
    is_valid = validate_email(email_ent.get())
    if age.years >= 18 and is_valid == True:
        playsound("access.mp3")
        player_id()
        window.destroy()
        import Generate

    elif age.years < 18:
        playsound("access_denied.mp3")
        messagebox.showinfo("Tough Luck", "You're Too Young")
    else:
        playsound("access_denied.mp3")
        messagebox.showerror("Error", "Make Sure Email Address and ID Valid")


# Creating labels and entries for the user to input their name, email address,
# id number and address
lbl_name = tk.Label(window, text="ENTER NAME: ", fg="white", bg="navy")
lbl_name.grid(row=0, column=1, padx=20, pady=20)

name_ent = tk.Entry(window, fg="black", bg="yellow")
name_ent.grid(row=0, column=2, padx=20, pady=20)

lbl_email = tk.Label(window, text="EMAIL ADDRESS: ", fg="white", bg="navy")
lbl_email.grid(row=1, column=1, padx=20, pady=20)

email_ent = tk.Entry(window, fg="black", bg="yellow")
email_ent.grid(row=1, column=2, padx=20, pady=20)

lbl_id = tk.Label(window, text="ID NUMBER: ", fg="white", bg="navy")
lbl_id.grid(row=2, column=1, padx=20, pady=20)

id_ent = tk.Entry(window, fg="black", bg="yellow")
id_ent.grid(row=2, column=2, padx=20, pady=20)

lbl_address = tk.Label(window, text="ADDRESS: ", fg="white", bg="navy")
lbl_address.grid(row=3, column=1, padx=20, pady=20)

address_ent = tk.Entry(window, fg="black", bg="yellow")
address_ent.grid(row=3, column=2, padx=20, pady=20)

# Adding a button for the user to submit their information
submit_btn = tk.Button(window, text="SUBMIT", relief="raised", borderwidth=4, bg="yellow", width=25, height=1, command=validation)
submit_btn.place(x=160, y=300)

window.mainloop()
