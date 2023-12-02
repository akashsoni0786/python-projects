import tkinter as tk
from tkinter import ttk

class LoginPage(tk.Tk):
    def _init_(self):
        super()._init_()

        self.geometry('300x300')
        self.resizable(0,0)
        self.title("Login Page")

        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.page()

    def page(self):

        username_l = ttk.Label(self,text="Username")
        username_l.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_e = ttk.Entry(self)
        username_e.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        password_l = ttk.Label(self, text="Password")
        password_l.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        password_e = ttk.Entry(self,show="*")
        password_e.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        login_Btn = ttk.Button(self,text="Login")
        login_Btn.grid(column= 2,row=3,sticky=tk.E,padx=5,pady=5)

# if __name__=="_main_":
login = LoginPage()

login.mainloop()


