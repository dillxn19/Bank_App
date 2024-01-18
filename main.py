import sqlite3
from tkinter import *
from bank_obj import *
conn = sqlite3.connect('bank.db')
c = conn.cursor()
root = Tk()
root.title("Bank App")

def login():
    home_frame.grid_forget()
    login_frame.grid(row = 0, column = 0)

    
# frames
home_frame = Frame(root)
home_frame.grid(row = 0, column = 0)
login_frame = Frame(root)

# home frame
new_user_button = Button(home_frame, text = "New User")
old_user_button = Button(home_frame, text = "Old User", command = login)
new_user_button.grid(row = 0, column = 0)
old_user_button.grid(row = 1, column = 0)

#login frame
nam_label = Label(login_frame, text = "Name: ")
nam_entry = Entry(login_frame)
acc_label = Label(login_frame, text = "Account Number: ")
acc_entry = Entry(login_frame)
log_button = Button(login_frame, text = "Login")
nam_label.grid(row = 0, column = 0)
nam_entry.grid(row = 0, column = 1)
acc_label.grid(row = 1, column = 0)
acc_entry.grid(row = 1, column = 1)
log_button.grid(row = 2, column = 0, columnspan = 2)
root.mainloop()