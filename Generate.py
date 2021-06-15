# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox

# Creating the window , adding a title and sizing it
window = Tk()
window.title("LOTTO NUMBERS")
window.geometry("650x400")
window.config(bg="yellow")
window.resizable(0, 0)

# A function to generate 6 random numbers


def ran_numbers():
    mylist = []
    while len(mylist) < 6:
        mynumber = random.randint(1, 49)
        if mynumber not in mylist:
            mylist.append(mynumber)
    lotto_num.config(text=mylist)


def claim():
    window.destroy()
    import Claim


def reset():
    first_ent.delete(0, END)
    second_ent.delete(0, END)
    third_ent.delete(0, END)
    fourth_ent.delete(0, END)
    fifth_ent.delete(0, END)
    sixth_ent.delete(0, END)
    lotto_num.config(text=" ")


def exit_program():
    messagebox.showinfo("GoodBye", "Thank You For Playing")
    window.destroy()


# A label telling the user to input 6 numbers

lbl_numbers = tk.Label(window, text="PLEASE INSERT 6 NUMBERS AND THEN CLICK PLAY: ", bg="yellow")
lbl_numbers.place(x=180, y=50)

first_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
first_ent.place(x=50, y=120)

second_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
second_ent.place(x=150, y=120)

third_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
third_ent.place(x=250, y=120)

fourth_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
fourth_ent.place(x=350, y=120)

fifth_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
fifth_ent.place(x=450, y=120)

sixth_ent = tk.Entry(window, fg="white", bg="maroon", width=4)
sixth_ent.place(x=550, y=120)

lotto_num = tk.Label(window, height=5, width=50, fg="white", bg="maroon")
lotto_num.place(x=130, y=180)

play_btn = tk.Button(window, text="PLAY", fg="white", bg="maroon", relief="raised", borderwidth=4, command=ran_numbers)
play_btn.place(x=200, y=320)

reset_btn = tk.Button(window, text="RESET", fg="white", bg="maroon",  relief="raised", borderwidth=4, command=reset)
reset_btn.place(x=50, y=320)

claim_btn = tk.Button(window, text="CLAIM", fg="white", bg="maroon",  relief="raised", borderwidth=4 , command=claim)
claim_btn.place(x=350, y=320)

exit_btn = tk.Button(window, text="EXIT", fg="white", bg="maroon",  relief="raised", borderwidth=4, command=exit_program)
exit_btn.place(x=500, y=320)


window.mainloop()
