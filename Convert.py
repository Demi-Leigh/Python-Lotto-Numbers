# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests
from playsound import playsound

# Creating the window , adding a title and sizing it and adding a color
window = Tk()
window.title("CURRENCY CONVERTER")
window.geometry("600x300")
window.config(bg="teal")
window.resizable(0, 0)
window.wm_iconify()

# A function which will convert the users winnings to any currency
def convert():
    playsound("click.mp3")
    try:
        url = "https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/" + from_ent.get()
        rates = requests.get(url).json()
        conversion = float(amount_ent.get()) * rates["conversion_rates"][to_ent.get()]
        currency_amount.config(text=conversion)
        amount = conversion

        with open("players.txt", "a+") as file:
            file.write("Converted Amount: " + str(amount))

    except:
        messagebox.showerror("Error", "Entries Cannot Be Empty")


def return_btn():
    window.iconify()
    import Claim


lbl_from = tk.Label(window, text="FROM: ", bg="teal")
lbl_from.place(x=30, y=50)

from_ent = tk.Entry(window)
from_ent.place(x=100, y=50)

lbl_to = tk.Label(window, text="TO:", bg="teal")
lbl_to.place(x=320, y=50)

to_ent = tk.Entry(window)
to_ent.place(x=370, y=50)

lbl_amount = tk.Label(window, text="AMOUNT:", bg="teal")
lbl_amount.place(x=280, y=100)

amount_ent = tk.Entry(window)
amount_ent.place(x=235, y=130)

currency_amount = tk.Label(window, height=1, width=21, bg="teal")
currency_amount.place(x=233, y=170)

return_btn = tk.Button(window, text="RETURN", relief="raised", borderwidth=4, width=10, height=1, command=return_btn)
return_btn.place(x=120, y=210)


convert_btn = tk.Button(window, text="CONVERT", relief="raised", borderwidth=4, width=10, height=1, command=convert)
convert_btn.place(x=360, y=210)

window.mainloop()
