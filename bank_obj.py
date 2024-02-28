import sqlite3
from tkinter import *
from tkinter import simpledialog, messagebox
conn = sqlite3.connect('bank.db')
c = conn.cursor()

class Bank:
    def __init__(self,name,acc_num,bal):
        self.name = name
        self.acc_num = acc_num
        self.bal = bal

    def withdraw(self,amt):
        if amt > self.bal or amt <= 0:
            messagebox.showinfo("Error", "Invalid Value")
        else:
            self.bal -= amt
            c.execute(f"update bank_info set Balance = '{self.bal}' where Name = '{self.name}'")
            conn.commit()

    def deposit(self,amt):
        if amt <= 0:
            messagebox.showinfo("Error", "Invalid Value")
        else:
            self.bal += amt
            c.execute(f"update bank_info set Balance = '{self.bal}' where Name = '{self.name}'")
            conn.commit()

    