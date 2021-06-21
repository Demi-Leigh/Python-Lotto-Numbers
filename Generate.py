# Demi-Leigh Jefferies class 1
from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from playsound import playsound


# Creating the window , adding a title and sizing it
window = Tk()
window.title("LOTTO NUMBERS")
window.geometry("650x400")
window.config(bg="yellow")
window.resizable(0, 0)

# A function to generate 6 random numbers


def ran_numbers():
    playsound("click.mp3")
    try:
        mylist = []
        while len(mylist) < 6:
            mynumber = random.randint(1, 49)
            if mynumber not in mylist:
                mylist.append(mynumber)
                lotto_num.config(text=mylist)
        mylist = set(mylist)
        entry_numbers = {int(first_ent.get()), int(second_ent.get()), int(third_ent.get()), int(fourth_ent.get()),
                         int(fifth_ent.get()), int(sixth_ent.get())}
        matching_nums = mylist.intersection(entry_numbers)
        count = len(matching_nums)
        file = open("players.txt", "a+")
# Checking if numbers match and how much user gets based on numbers matched

        if count == 2:
            playsound("cheer.mp3")
            messagebox.showinfo("You Win!", "You have won R20")

            file.write("Cash: " + "R20")

        elif count == 3:
            playsound("cheer.mp3")
            messagebox.showinfo("You Win!!", "You have won R100.50 ")
            file.write("\n")

            file.write("Cash: " + "R100.50")

        elif count == 4:
            playsound("cheer.mp3")
            messagebox.showinfo("You Win", "You Have won R2384")
            file.write("\n")

            file.write("Cash: " + "R2384")

        elif count == 5:
            playsound("cheer.mp3")
            messagebox.showinfo("You Win", "You have won R8584")
            file.write("\n")

            file.write("Cash: " + "R8584")

        elif count == 6:
            playsound("jackpot.mp3")
            messagebox.showinfo("JACKPOT", "You Win R10 000 000")
            file.write("\n")

            file.write("Cash: " + "R10 000 000")

        else:
            playsound("laugh.mp3")
            msg = messagebox.showinfo("Unlucky!!", "You Lose")
            if msg == "ok":
                first_ent.delete(0, END)
                second_ent.delete(0, END)
                third_ent.delete(0, END)
                fourth_ent.delete(0, END)
                fifth_ent.delete(0, END)
                sixth_ent.delete(0, END)
                lotto_num.config(text=" ")
    except ValueError:
        messagebox.showerror("Error", "Please Insert 6 Numbers!")

# Function that takes user to the next window to fill in bank details


def claim():
    playsound("click.mp3")
    window.destroy()
    import Claim

# Resets the entries that user entered


def reset():
    playsound("click.mp3")
    first_ent.delete(0, END)
    second_ent.delete(0, END)
    third_ent.delete(0, END)
    fourth_ent.delete(0, END)
    fifth_ent.delete(0, END)
    sixth_ent.delete(0, END)

# Exits the program


def exit_program():
    playsound("click.mp3")
    messagebox.showinfo("GoodBye", "Thank You For Playing")
    window.destroy()


# A label telling the user to input 6 numbers
# Entries to input the 6 numbers

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

claim_btn = tk.Button(window, text="CLAIM", fg="white", bg="maroon",  relief="raised", borderwidth=4, command=claim)
claim_btn.place(x=350, y=320)

exit_btn = tk.Button(window, text="EXIT", fg="white", bg="maroon",  relief="raised", borderwidth=4, command=exit_program)
exit_btn.place(x=500, y=320)


window.mainloop()
