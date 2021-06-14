# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk

# Creating the window , adding a title and sizing it
window = Tk()
window.title("LOTTO NUMBERS")
window.geometry("650x400")
window.config(bg="yellow")
window.resizable(0, 0)


# A label telling the user to input 6 numbers

lbl_numbers = tk.Label(window, text="PLEASE INSERT 6 NUMBERS : ", bg="yellow")
lbl_numbers.place(x=250, y=50)

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

lotto_num = tk.LabelFrame(window, height=100, width=320, fg="white", bg="maroon")
lotto_num.place(x=160, y=180)

reset_btn = tk.Button(window, text="RESET", fg="white", bg="maroon")
reset_btn.place(x=50, y=320)

claim_btn = tk.Button(window, text="CLAIM PRIZE", fg="white", bg="maroon")
claim_btn.place(x=255, y=320)

exit_btn = tk.Button(window, text="EXIT", fg="white", bg="maroon")
exit_btn.place(x=500, y=320)


window.mainloop()
