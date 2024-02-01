import sqlite3
from tkinter import *
from tkinter import simpledialog
from bank_obj import *
conn = sqlite3.connect('bank.db')
c = conn.cursor()
root = Tk()
root.title("Bank App")
user_obj = Bank(name = "", acc_num = "", bal = "")


def login():
    home_frame.grid_forget()
    login_frame.grid(row = 0, column = 0)


def log_check():
    user_name = nam_entry.get()
    user_acc = acc_entry.get()
    c.execute(f"select * from bank_info where Name = '{user_name}' and Acc_Num = '{user_acc}';")
    user = c.fetchone()
    if user:
        user_obj.name, user_obj.acc_num, user_obj.bal = user
        nam_info.config(text = user_obj.name)
        acc_info.config(text = user_obj.acc_num)
        bal_info.config(text = user_obj.bal)
        login_frame.grid_forget()
        nam_entry.delete(0,END)
        acc_entry.delete(0,END)
        info_frame.grid(row = 0, column = 0)

def withdraw():
    result = simpledialog.askstring("Input", "Enter your amount")
    if result:
        user_obj.withdraw(int(result))
        bal_info.config(text = user_obj.bal)
    else:
        print("nothing")

def deposit():
    result = simpledialog.askstring("Input", "Enter your amount")
    if result:
        user_obj.deposit(int(result))
        bal_info.config(text = user_obj.bal)
    else:
        print("nothing")

def logout():
    user_obj = Bank(name = "", acc_num = "", bal = "")
    info_frame.grid_forget()
    login_frame.grid()

    
# frames
home_frame = Frame(root)
home_frame.grid(row = 0, column = 0)
login_frame = Frame(root)
info_frame = Frame(root)

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
log_button = Button(login_frame, text = "Login", command = log_check)
nam_label.grid(row = 0, column = 0)
nam_entry.grid(row = 0, column = 1)
acc_label.grid(row = 1, column = 0)
acc_entry.grid(row = 1, column = 1)
log_button.grid(row = 2, column = 0, columnspan = 2)

#info frame
nam_info_label = Label(info_frame, text = "Name: ")
nam_info = Label(info_frame, text = user_obj.name)
acc_info_label = Label(info_frame, text = "Account Number: ")
acc_info = Label(info_frame, text = user_obj.acc_num)
bal_info_label = Label(info_frame, text = "Balance: ")
bal_info = Label(info_frame, text = user_obj.bal)
wit_button = Button(info_frame, text = "Withdraw", command = withdraw)
dep_button = Button(info_frame, text = "Deposit", command = deposit)
logout_button = Button(info_frame, text = "Logout", command = logout)
nam_info_label.grid(row = 0, column = 0)
nam_info.grid(row = 0, column = 1)
acc_info_label.grid(row = 1, column = 0)
acc_info.grid(row = 1, column = 1)
bal_info_label.grid(row = 2, column = 0)
bal_info.grid(row = 2, column = 1)
wit_button.grid(row = 3, column = 0)
dep_button.grid(row = 3, column = 1)
logout_button.grid(row = 4, column = 0, columnspan = 2)
root.mainloop()