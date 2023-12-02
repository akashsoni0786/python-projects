import random
import os
from tkinter import messagebox
from tkinter import *

class Crypto:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x850")
        self.root.title("Prediction Software")
        bg_color = "lightblue"
        title = Label(self.root, text="CRYPTOCURRENCY PRICE PREDICTION", font=("times new roman", 30, "bold"), fg="white", pady=2,
                      bd=12, bg="Blue", relief=GROOVE)
        title.pack(fill=X)

        F2 = LabelFrame(self.root, text="BIT COIN", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F2.place(x=3, y=75, width = F2.winfo_screenwidth(), height=240)

        bitcoinlbl1 = Label(F2, text="Real Value ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10, pady=0)
        bitcoinlbl1.grid(row=0, column=0, sticky="W")
        w=F2.winfo_screenwidth()
        bitcoinbtn1 = Button(F2, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=0, column=1, padx=10,pady=5)

        bitcoinlbl2 = Label(F2, text="Prediction ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                           padx=10, pady=0)
        bitcoinlbl2.grid(row=1, column=0, sticky="W")
        bitcoinbtn2 = Button(F2, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=1, column=1, padx=10,
                                                                                               pady=5)

        bitcoinlbl3 = Label(F2, text="Compare", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                           padx=10, pady=0)
        bitcoinlbl3.grid(row=2, column=0, sticky="W")

        bitcoinbtn3 = Button(F2, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=2, column=1, padx=10,
                                                                                               pady=5)


        F3 = LabelFrame(self.root, text="Wazir X", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F3.place(x=3, y=315, width=F2.winfo_screenwidth(), height=240)

        bitcoinlbl11 = Label(F3, text="Real Value ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                            padx=10, pady=0)
        bitcoinlbl11.grid(row=0, column=0, sticky="W")
        w = F3.winfo_screenwidth()
        bitcoinbtn11 = Button(F3, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=0, column=1, padx=10,
                                                                                             pady=5)

        bitcoinlbl21 = Label(F3, text="Prediction ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                            padx=10, pady=0)
        bitcoinlbl21.grid(row=1, column=0, sticky="W")
        w = F2.winfo_screenwidth()
        bitcoinbtn21 = Button(F3, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=1, column=1, padx=10,
                                                                                             pady=5)

        bitcoinlbl31 = Label(F3, text="Compare", font=("times new roman", 17, "bold"), bg=bg_color,
                            fg="blue",
                            padx=10, pady=0)
        bitcoinlbl31.grid(row=2, column=0, sticky="W")
        w = F2.winfo_screenwidth()
        bitcoinbtn31 = Button(F3, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=2, column=1,
                                                                                                padx=10,
                                                                                                pady=5)

        F4 = LabelFrame(self.root, text="Big Bull", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F4.place(x=3, y=555, width=F2.winfo_screenwidth(), height=230)

        bitcoinlbl22 = Label(F4, text="Real Value ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                             padx=10, pady=0)
        bitcoinlbl22.grid(row=0, column=0, sticky="W")
        w = F3.winfo_screenwidth()
        bitcoinbtn22 = Button(F4, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=0, column=1, padx=10,
                                                                                              pady=5)

        bitcoinlbl221 = Label(F4, text="Prediction ", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                              padx=10, pady=0)
        bitcoinlbl221.grid(row=1, column=0, sticky="W")
        w = F2.winfo_screenwidth()
        bitcoinbtn221 = Button(F4, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=1, column=1, padx=10,
                                                                                               pady=5)

        bitcoinlbl321 = Label(F4, text="Compare", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="blue",
                              padx=10, pady=0)
        bitcoinlbl321.grid(row=2, column=0, sticky="W")
        w = F2.winfo_screenwidth()
        bitcoinbtn321 = Button(F4, text="Click", width=110, bd=7, font=("arial 15 bold")).grid(row=2, column=1,
                                                                                               padx=10,
                                                                                               pady=5)







root = Tk()
obj = Crypto(root)
root.mainloop()