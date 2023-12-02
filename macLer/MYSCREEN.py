import random
import os
from tkinter import messagebox
from tkinter import *


class BILL_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x850")
        self.root.title("Billing Software")
        bg_color = "lightblue"
        title = Label(self.root, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"), fg="white", pady=2,
                      bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)
        # ========================================================Variables========================================================================
        # ++++++++Drinks++++++++++++++++++++++++
        self.maza = IntVar()
        self.coak = IntVar()
        self.frooti = IntVar()
        self.thump = IntVar()
        self.appy = IntVar()
        self.sprite = IntVar()
        # ++++++++Total product price & tax+++++++++++++++++++++++++++
        self.t_amt = IntVar()
        self.t_tax = IntVar()
        # +++++++++++++++CAKES+++++++++++++++++++++++++++++++++++++++++++++++
        # ================Special Cakes=========================================
        self.sp1 = IntVar()
        self.sp2 = IntVar()
        self.sp3 = IntVar()
        self.sp4 = IntVar()
        self.sp5 = IntVar()
        self.sp6 = IntVar()
        # ==================Black Forest========================================================
        self.bf1 = IntVar()
        self.bf2 = IntVar()
        self.bf3 = IntVar()
        self.bf4 = IntVar()
        self.bf5 = IntVar()
        self.bf6 = IntVar()
        # ===================Strwaberry Cakes=======================================================================
        self.st1 = IntVar()
        self.st2 = IntVar()
        self.st3 = IntVar()
        self.st4 = IntVar()
        self.st5 = IntVar()
        self.st6 = IntVar()
        # ===================Welwet Cakes=============================================================================
        self.wt1 = IntVar()
        self.wt2 = IntVar()
        self.wt3 = IntVar()
        self.wt4 = IntVar()
        self.wt5 = IntVar()
        self.wt6 = IntVar()
        # ===================Creamy Cakes====================================================================
        self.cr1 = IntVar()
        self.cr2 = IntVar()
        self.cr3 = IntVar()
        self.cr4 = IntVar()
        self.cr5 = IntVar()
        self.cr6 = IntVar()
        # =====================Fruit Cakes==============================================================================
        self.fr1 = IntVar()
        self.fr2 = IntVar()
        self.fr3 = IntVar()
        self.fr4 = IntVar()
        self.fr5 = IntVar()
        self.fr6 = IntVar()
        # ====================Shape Cakes================================================================================
        self.sh1 = IntVar()
        self.sh2 = IntVar()
        self.sh3 = IntVar()
        self.sh4 = IntVar()
        self.sh5 = IntVar()
        self.sh6 = IntVar()
        # =====================Cookies================================================================================
        self.co1 = IntVar()
        self.co2 = IntVar()
        self.co3 = IntVar()
        self.co4 = IntVar()
        self.co5 = IntVar()
        self.co6 = IntVar()
        # ====================Floor Cakes=================================================================================
        self.fl1 = IntVar()
        self.fl2 = IntVar()
        self.fl3 = IntVar()
        self.fl4 = IntVar()
        self.fl5 = IntVar()
        self.fl6 = IntVar()
        # +++++++++++++++++++++++++++++Breads and Buns++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ===========================Slice Bread =======================================================================
        self.sb1 = IntVar()
        self.sb2 = IntVar()
        self.sb3 = IntVar()
        self.sb4 = IntVar()
        self.sb5 = IntVar()
        self.sb6 = IntVar()
        # ===========================Wheat Bread================================================================================
        self.wh1 = IntVar()
        self.wh2 = IntVar()
        self.wh3 = IntVar()
        self.wh4 = IntVar()
        self.wh5 = IntVar()
        self.wh6 = IntVar()
        # ===========================Pizza======================================================================================
        self.pz1 = IntVar()
        self.pz2 = IntVar()
        self.pz3 = IntVar()
        self.pz4 = IntVar()
        self.pz5 = IntVar()
        self.pz6 = IntVar()
        # ========================Burgers========================================================================
        self.bg1 = IntVar()
        self.bg2 = IntVar()
        self.bg3 = IntVar()
        self.bg4 = IntVar()
        self.bg5 = IntVar()
        self.bg6 = IntVar()
        # =======================Hot Dogs======================================================================================
        self.hd1 = IntVar()
        self.hd2 = IntVar()
        self.hd3 = IntVar()
        self.hd4 = IntVar()
        self.hd5 = IntVar()
        self.hd6 = IntVar()
        # =======================Toastss========================================================================================
        self.to1 = IntVar()
        self.to2 = IntVar()
        self.to3 = IntVar()
        self.to4 = IntVar()
        self.to5 = IntVar()
        self.to6 = IntVar()
        # =====================Lollipops=================================================================================
        self.lp1 = IntVar()
        self.lp2 = IntVar()
        self.lp3 = IntVar()
        self.lp4 = IntVar()
        self.lp5 = IntVar()
        self.lp6 = IntVar()
        # ====================Gummy===================================================================================
        self.gm1 = IntVar()
        self.gm2 = IntVar()
        self.gm3 = IntVar()
        self.gm4 = IntVar()
        self.gm5 = IntVar()
        self.gm6 = IntVar()
        # ==================Brioches====================================================================================
        self.bo1 = IntVar()
        self.bo2 = IntVar()
        self.bo3 = IntVar()
        self.bo4 = IntVar()
        self.bo5 = IntVar()
        self.bo6 = IntVar()
        # ++++++++++Customer's Details Variable++++++++++++++++++++++++++++++++++++++++++
        self.c_name = StringVar()
        self.c_phn = StringVar()

        self.bill_no = StringVar()
        x = random.randint(11111111, 99999999)
        self.bill_no.set(str(x))
        self.Choose = StringVar()

        # +++++++++++++++++++++++++++++Customer Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        F1 = LabelFrame(self.root, text="Customer Details", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F1.place(x=0, y=80, relwidth=1)
        cname_label = Label(F1, text="Customer Name", font=("times new roman", 15, "bold"), bg=bg_color, fg="white",
                            padx=20, pady=5, )
        cname_label.grid(row=0, column=0)
        cname_entry = Entry(F1, width=20, bd=7, textvariable=self.c_name, relief=SUNKEN, font=("arial", 15)).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=10,
                                                                                                                  pady=5)

        cphn_label = Label(F1, text="Customer Phone No.", font=("times new roman", 15, "bold"), bg=bg_color, fg="white",
                           padx=20, pady=5, )
        cphn_label.grid(row=0, column=2)
        cphn_entry = Entry(F1, width=20, bd=7, relief=SUNKEN, textvariable=self.c_phn, font=("arial", 15)).grid(row=0,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=5)

        cbill_label = Label(F1, text="Bill Number", font=("times new roman", 15, "bold"), bg=bg_color, fg="white",
                            padx=10, pady=5, )
        cbill_label.grid(row=0, column=4)
        cbill_entry = Entry(F1, width=20, bd=7, textvariable=self.bill_no, relief=SUNKEN, font=("arial", 15)).grid(
            row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Choose", command=self.find_bill, width=10, bd=7, font=("arial 15 bold")).grid(row=0,
                                                                                                                  column=6,
                                                                                                                  padx=70,
                                                                                                                  pady=15)
        # +++++++++++++++++++++++++++++++++++++++++++++Cosmetic Frame+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        F2 = LabelFrame(self.root, text="CAKES & PASTERY", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F2.place(x=3, y=200, width=350, height=600)

        cake1 = Label(F2, text="Special", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10, pady=0)
        cake1.grid(row=0, column=0, sticky="W")
        cake1e = Button(F2, text="Choose", command=self.special, width=10, bd=7, font=("arial 15 bold")).grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5)

        cake2 = Label(F2, text="Black Forest", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10,
                      pady=0)
        cake2.grid(row=1, column=0, sticky="W")
        cake2e = Button(F2, text="Choose", command=self.Bklforest, width=10, bd=7, font=("arial 15 bold")).grid(row=1,
                                                                                                                column=1,
                                                                                                                padx=10,
                                                                                                                pady=5)

        cake3 = Label(F2, text="Strawberry", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10,
                      pady=0)
        cake3.grid(row=2, column=0, sticky="W")
        cake3e = Button(F2, text="Choose", command=self.Strawberry, width=10, bd=7, font=("arial 15 bold")).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        cake4 = Label(F2, text="Welwet", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10, pady=0)
        cake4.grid(row=3, column=0, sticky="W")
        cake4e = Button(F2, text="Choose", command=self.Welwet, width=10, bd=7, font=("arial 15 bold")).grid(row=3,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=5)

        cake5 = Label(F2, text="CREAMY", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10, pady=0)
        cake5.grid(row=4, column=0, sticky="W")
        cake5e = Button(F2, text="Choose", command=self.Creamy, width=10, bd=7, font=("arial 15 bold")).grid(row=4,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=5)

        cake6 = Label(F2, text="Fruit", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10, pady=0)
        cake6.grid(row=5, column=0, sticky="W")
        cake6e = Button(F2, text="Choose", command=self.Fruit, width=10, bd=7, font=("arial 15 bold")).grid(row=5,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        cake7 = Label(F2, text="Shape", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10,
                      pady=0)
        cake7.grid(row=6, column=0, sticky="W")
        cake7e = Button(F2, text="Choose", command=self.Shape, width=10, bd=7, font=("arial 15 bold")).grid(row=6,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        cake8 = Label(F2, text="Cookies", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10,
                      pady=0)
        cake8.grid(row=7, column=0, sticky="W")
        cake8e = Button(F2, text="Choose", command=self.Shapflav, width=10, bd=7, font=("arial 15 bold")).grid(row=7,
                                                                                                               column=1,
                                                                                                               padx=10,
                                                                                                               pady=5)
        cake9 = Label(F2, text="Floor", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=10,
                      pady=0)
        cake9.grid(row=8, column=0, sticky="W")
        cake9e = Button(F2, text="Choose", width=10, command=self.Floor, bd=7, font=("arial 15 bold")).grid(row=8,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        # +++++++++++++++++++++++++++++++++++++++++++++Bread Frame+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        F3 = LabelFrame(self.root, text="Breads Buns & Candy", font=("times new roman", 18, "bold"), bg=bg_color,
                        relief=GROOVE, bd=10, fg="Green")
        F3.place(x=360, y=200, width=350, height=600)

        bun1 = Label(F3, text="Slice \nBread", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                     pady=5)
        bun1.grid(row=0, column=0)
        bun1e = Button(F3, text="Choose", command=self.SliceB, width=10, bd=7, font=("arial 15 bold")).grid(row=0,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        bun2 = Label(F3, text="Wheat \nBread", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                     pady=5)
        bun2.grid(row=1, column=0)
        bun2e = Button(F3, text="Choose", command=self.Wheatb, width=10, bd=7, font=("arial 15 bold")).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        bun3 = Label(F3, text="Pizza", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        bun3.grid(row=2, column=0)
        bun3e = Button(F3, text="Choose", command=self.Pizza, width=10, bd=7, font=("arial 15 bold")).grid(row=2,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=5)

        bun4 = Label(F3, text="Burger", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        bun4.grid(row=3, column=0)
        bun4e = Button(F3, text="Choose", command=self.Burger, width=10, bd=7, font=("arial 15 bold")).grid(row=3,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        bun5 = Label(F3, text="Hogdog", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        bun5.grid(row=4, column=0)
        bun5e = Button(F3, text="Choose", command=self.Hogdog, width=10, bd=7, font=("arial 15 bold")).grid(row=4,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=5)

        bun7 = Label(F3, text="Toast", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        bun7.grid(row=5, column=0)
        bun7e = Button(F3, text="Choose", command=self.Toast, width=10, bd=7, font=("arial 15 bold")).grid(row=5,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=5)

        bun8 = Label(F3, text="Lolipops\nSours", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                     pady=5)
        bun8.grid(row=7, column=0)
        bun8e = Button(F3, text="Choose", command=self.Lolipops, width=10, bd=7, font=("arial 15 bold")).grid(row=7,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5)

        bun9 = Label(F3, text="Gummies &\nChocolates", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue",
                     padx=20,
                     pady=5)
        bun9.grid(row=8, column=0)
        bun9e = Button(F3, text="Choose", command=self.Gummy, width=10, bd=7, font=("arial 15 bold")).grid(row=8,
                                                                                                           column=1,
                                                                                                           padx=10,
                                                                                                           pady=5)

        bun10 = Label(F3, text="Brioche", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                      pady=5)
        bun10.grid(row=9, column=0)
        bun10e = Button(F3, text="Choose", command=self.Brioche, width=10, bd=7, font=("arial 15 bold")).grid(row=9,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5)
        # +++++++++++++++++++++++++++++++++++++++++++++Drink Frame+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        F4 = LabelFrame(self.root, text="Drink Items", font=("times new roman", 16, "bold"), bg=bg_color, relief=GROOVE,
                        bd=10, fg="Green")
        F4.place(x=715, y=200, width=350, height=340)

        d1_label = Label(F4, text="Maza", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        d1_label.grid(row=0, column=0)
        d1_entry = Entry(F4, width=10, bd=7, textvariable=self.maza, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=0, column=1, padx=10, pady=5)

        d2_label = Label(F4, text="Cock", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20, pady=5)
        d2_label.grid(row=1, column=0)
        d2_entry = Entry(F4, width=10, textvariable=self.coak, bd=7, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=1, column=1, padx=10, pady=5)

        d3_label = Label(F4, text="Frooti", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                         pady=5)
        d3_label.grid(row=2, column=0)
        d3_entry = Entry(F4, width=10, bd=7, textvariable=self.frooti, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=2, column=1, padx=10, pady=5)

        d4_label = Label(F4, text="Thumps Up", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                         pady=5)
        d4_label.grid(row=3, column=0)
        d5_entry = Entry(F4, width=10, bd=7, textvariable=self.thump, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=3, column=1, padx=10, pady=5)

        d5_label = Label(F4, text="Appy Fizz", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                         pady=5)
        d5_label.grid(row=4, column=0)
        d5_entry = Entry(F4, width=10, bd=7, textvariable=self.appy, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=4, column=1, padx=10, pady=5)

        d6_label = Label(F4, text="Sprite", font=("times new roman", 17, "bold"), bg=bg_color, fg="blue", padx=20,
                         pady=5)
        d6_label.grid(row=5, column=0)
        d6_entry = Entry(F4, width=10, bd=7, textvariable=self.sprite, relief=SUNKEN, font=("arial", 15, "bold")).grid(
            row=5, column=1, padx=10, pady=5)
        # =================================================Bill Area============================================================================================
        F5 = Frame(self.root, relief=GROOVE, bd=10)
        F5.place(x=1070, y=200, width=465, height=420)
        bill_title = Label(F5, text="Phoenix United Mall", font=("arial 15 bold "), bd=10, relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =================================================bUTTON FRAME============================================================
        F6 = LabelFrame(self.root, text="Bill Menu", font=("times new roman", 18, "bold"), bg=bg_color, relief=GROOVE,
                        bd=10, fg="green")
        F6.place(x=715, y=540, width=350, height=260)
        bill1 = Label(F6, text="Total Amount(in Rupees)  :", bg=bg_color, fg='Blue',
                      font=("timea new roman", 18, "bold"))
        bill1.grid(row=0, column=0)
        bill1_ent = Entry(F6, font=("timea new roman", 18, "bold"), textvariable=self.t_amt, width=20, bd=10,
                          relief=SUNKEN)
        bill1_ent.grid(row=1, column=0, pady=16, padx=15)
        bill2 = Label(F6, text="Total Tax (in Rupees)  :", bg=bg_color, fg='Blue', font=("timea new roman", 18, "bold"))
        bill2.grid(row=2, column=0)
        bill2_ent = Entry(F6, font=("timea new roman", 18, "bold"), textvariable=self.t_tax, width=20, bd=10,
                          relief=SUNKEN)
        bill2_ent.grid(row=3, column=0, pady=10, padx=15)

        F7 = Frame(root, bd=7, relief=GROOVE)
        F7.place(x=1070, y=630, width=460, height=167)
        total_btn = Button(F7, width=17, height=0, bd=5, command=self.total, font=("arial 15 bold"), text="Total",
                           bg="cadetblue", fg="white", pady=15).grid(row=0, column=0)
        Gbill_btn = Button(F7, width=17, height=0, command=self.bill_area, bd=5, font=("arial 15 bold"),
                           text="Generate Bill", bg="cadetblue", fg="white", pady=15).grid(row=1, column=0)
        clear_btn = Button(F7, width=17, height=0, command=self.clear, bd=5, font=("arial 15 bold"), text="Clear",
                           bg="cadetblue", fg="white", pady=15).grid(row=0, column=1)
        exit_btn = Button(F7, width=17, height=0, command=self.exit, bd=5, font=("arial 15 bold"), text="Exit",
                          bg="cadetblue", fg="white", pady=15).grid(row=1, column=1)
        self.welcome()

    # ===============================Special Cakes=============================================================================================

    def special(self):
        sp = Tk()
        self.sp = sp
        self.sp.geometry("680x450")
        self.sp.title("Billing Software")
        self.sp.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.sp, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"), fg="white", pady=2, bd=12,
                      bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F1s = LabelFrame(self.sp, text="Special Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="Blue")
        F1s.place(x=0, y=75, width=680, height=375)

        spcake1_label = Label(F1s, text="* Caramel Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        spcake1_label.place(x=30, y=10)
        spcake1_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        spcake2_label = Label(F1s, text="* Fudgy Chocolate Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        spcake2_label.place(x=30, y=50)
        spcake2_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        spcake3_label = Label(F1s, text="*  Carrot Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        spcake3_label.place(x=30, y=90, )
        spcake3_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        spcake4_label = Label(F1s, text="*  Buttercake with Lemon Icing", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        spcake4_label.place(x=30, y=130)
        spcake4_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        spcake5_label = Label(F1s, text="*  Easy lightblue Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        spcake5_label.place(x=30, y=170, )
        spcake5_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        spcake6_label = Label(F1s, text="*  Apple Tea Cup", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        spcake6_label.place(x=30, y=210, )
        spcake6_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sp6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F1s, bd=7, width=10, font=("arial 15 bold"), command=self.total,
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        sp.mainloop()

    # ===============================Black Forest Cakes=============================================================================================
    def Bklforest(self):
        bf = Tk()
        self.bf = bf
        self.bf.geometry("680x450")
        self.bf.title("Billing Software")
        self.bf.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.bf, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.bf, text="Black Forest Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        bfcake1_label = Label(F2s, text="* My go-to Chocolate layer Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bfcake1_label.place(x=30, y=10)
        bfcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        bfcake2_label = Label(F2s, text="* Dark Sweet Cherries Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bfcake2_label.place(x=30, y=50)
        bfcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        bfcake3_label = Label(F2s, text="*  Fluffy Vanilla Whipped Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bfcake3_label.place(x=30, y=90, )
        bfcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        bfcake4_label = Label(F2s, text="*  Fully Brownie Layer Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bfcake4_label.place(x=30, y=130)
        bfcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        bfcake5_label = Label(F2s, text="*  Dark Chocolate Ganache Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bfcake5_label.place(x=30, y=170, )
        bfcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        bfcake6_label = Label(F2s, text="*  Dark Forest Dump Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        bfcake6_label.place(x=30, y=210, )
        bfcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bf6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        bf.mainloop()

    # ===============================Strawberry Cakes=============================================================================================
    def Strawberry(self):
        st = Tk()

        self.st = st
        self.st.geometry("680x450")
        self.st.title("Billing Software")
        self.st.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.st, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.st, text="Strawberry Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        stcake1_label = Label(F2s, text="* Strawberry Caramel Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        stcake1_label.place(x=30, y=10)
        stcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        stcake2_label = Label(F2s, text="* Strawberry Chocolate Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        stcake2_label.place(x=30, y=50)
        stcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        stcake3_label = Label(F2s, text="*  Strawberry Vanilla Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        stcake3_label.place(x=30, y=90, )
        stcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        stcake4_label = Label(F2s, text="*  Buttercake with Strawberry Icing", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        stcake4_label.place(x=30, y=130)
        stcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        stcake5_label = Label(F2s, text="*  Fully Strawberry Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        stcake5_label.place(x=30, y=170, )
        stcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        stcake6_label = Label(F2s, text="*  Strawberry Tea Cup", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        stcake6_label.place(x=30, y=210, )
        stcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.st6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)
        st.mainloop()

    # ===============================Welwet Cakes=============================================================================================
    def Welwet(self):
        wt = Tk()
        self.wt = wt
        self.wt.geometry("680x450")
        self.wt.title("Billing Software")
        self.wt.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.wt, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.wt, text="Welwet Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        wtcake1_label = Label(F2s, text="* Yellow Welwet Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wtcake1_label.place(x=30, y=10)
        wtcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        wtcake2_label = Label(F2s, text="* Green Welwet Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wtcake2_label.place(x=30, y=50)
        wtcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        wtcake3_label = Label(F2s, text="*  Blue Welwet Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wtcake3_label.place(x=30, y=90, )
        wtcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        wtcake4_label = Label(F2s, text="*  Purple Welwet Cakes", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wtcake4_label.place(x=30, y=130)
        wtcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        wtcake5_label = Label(F2s, text="*  Pink Welwet Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wtcake5_label.place(x=30, y=170, )
        wtcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        wtcake6_label = Label(F2s, text="*  Black Welwet Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wtcake6_label.place(x=30, y=210, )
        wtcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wt6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        wt.mainloop()

    # ===============================Creamy Cakes=============================================================================================
    def Creamy(self):
        cm = Tk()

        self.cm = cm
        self.cm.geometry("680x450")
        self.cm.title("Billing Software")
        self.cm.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.cm, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.cm, text="Creamy Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        cmcake1_label = Label(F2s, text="* Caramel Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        cmcake1_label.place(x=30, y=10)
        cmcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        cmcake2_label = Label(F2s, text="* Fudgy Chocolate Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        cmcake2_label.place(x=30, y=50)
        cmcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        cmcake3_label = Label(F2s, text="*  Only Cream Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        cmcake3_label.place(x=30, y=90, )
        cmcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        cmcake4_label = Label(F2s, text="*  Buttercake with Lemon Icing", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        cmcake4_label.place(x=30, y=130)
        cmcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        cmcake5_label = Label(F2s, text="*  Easy lightblue Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        cmcake5_label.place(x=30, y=170, )
        cmcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        cmcake6_label = Label(F2s, text="*  Apple Tea Cup", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        cmcake6_label.place(x=30, y=210, )
        cmcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.cr6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        cm.mainloop()

    # ===============================Fruit Cakes=============================================================================================
    def Fruit(self):
        fr = Tk()
        self.fr = fr
        self.fr.geometry("680x450")
        self.fr.title("Billing Software")
        self.fr.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.fr, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.fr, text="Fruit Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        frcake1_label = Label(F2s, text="* Christmas Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        frcake1_label.place(x=30, y=10)
        frcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        frcake2_label = Label(F2s, text="* Candy Orange Slice Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        frcake2_label.place(x=30, y=50)
        frcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        frcake3_label = Label(F2s, text="*  Carrot Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        frcake3_label.place(x=30, y=90, )
        frcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        frcake4_label = Label(F2s, text="*  Buttercake with Lemon Icing", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        frcake4_label.place(x=30, y=130)
        frcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        frcake5_label = Label(F2s, text="*  Easy Banana Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        frcake5_label.place(x=30, y=170, )
        frcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        frcake6_label = Label(F2s, text="*  Apple Tea Cup", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        frcake6_label.place(x=30, y=210, )
        frcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fr6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        fr.mainloop()

    # ===============================Shape Cakes=============================================================================================
    def Shape(self):
        sh = Tk()
        self.sh = sh
        self.sh.geometry("680x450")
        self.sh.title("Billing Software")
        self.sh.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.sh, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.sh, text="Shape Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        shcake1_label = Label(F2s, text="* Character Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        shcake1_label.place(x=30, y=10)
        shcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        shcake2_label = Label(F2s, text="* Pops Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        shcake2_label.place(x=30, y=50)
        shcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        shcake3_label = Label(F2s, text="*  Ball Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        shcake3_label.place(x=30, y=90, )
        shcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        shcake4_label = Label(F2s, text="*  Conical Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        shcake4_label.place(x=30, y=130)
        shcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        shcake5_label = Label(F2s, text="*  Flat + Layered Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        shcake5_label.place(x=30, y=170, )
        shcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        shcake6_label = Label(F2s, text="*  Spring Form Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        shcake6_label.place(x=30, y=210, )
        shcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.sh6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        sh.mainloop()

    # ===============================Shape + Flavour Cakes=============================================================================================
    def Shapflav(self):
        sf = Tk()
        self.sf = sf
        self.sf.geometry("680x450")
        self.sf.title("Billing Software")
        self.sf.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.sf, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.sf, text="Cookies Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        sfcake1_label = Label(F2s, text="* Funfetti Suger Cookie Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake1_label.place(x=30, y=10)
        sfcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        sfcake2_label = Label(F2s, text="* Peanut Butter Chocolate Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake2_label.place(x=30, y=50)
        sfcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        sfcake3_label = Label(F2s, text="*  Banana Foster Cookie Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake3_label.place(x=30, y=90, )
        sfcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        sfcake4_label = Label(F2s, text="*  Chocolate Chip Cookie Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake4_label.place(x=30, y=130)
        sfcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        sfcake5_label = Label(F2s, text="*  Halloween Cookie Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake5_label.place(x=30, y=170, )
        sfcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        sfcake6_label = Label(F2s, text="*  Gluten-Free Vegan Chocolate", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sfcake6_label.place(x=30, y=210, )
        sfcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.co6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        sf.mainloop()

    # ===============================Floor Cakes=============================================================================================
    def Floor(self):
        fl = Tk()
        self.fl = fl
        self.fl.geometry("680x450")
        self.fl.title("Billing Software")
        self.fl.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.fl, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.fl, text="Floor Cake Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        flcake1_label = Label(F2s, text="* Single Layer Cake", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        flcake1_label.place(x=30, y=10)
        flcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl1,
                              font=("arial", 15, "bold")).place(x=480, y=10)

        flcake2_label = Label(F2s, text="* Double Layer With Double Flavour Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        flcake2_label.place(x=30, y=50)
        flcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl2,
                              font=("arial", 15, "bold")).place(x=480, y=50)

        flcake3_label = Label(F2s, text="*  Triple Layer With Triple Flavour Cake",
                              font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        flcake3_label.place(x=30, y=90, )
        flcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl3,
                              font=("arial", 15, "bold")).place(x=480, y=90)

        flcake4_label = Label(F2s, text="*  Normal Double Layer Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        flcake4_label.place(x=30, y=130)
        flcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl4,
                              font=("arial", 15, "bold")).place(x=480, y=130)

        flcake5_label = Label(F2s, text="*  Normal Tripe Layer Cake", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        flcake5_label.place(x=30, y=170, )
        flcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl5,
                              font=("arial", 15, "bold")).place(x=480, y=170)

        flcake6_label = Label(F2s, text="*  Triple Layer with Double Flavour Cake",
                              font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        flcake6_label.place(x=30, y=210, )
        flcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.fl6,
                              font=("arial", 15, "bold")).place(x=480, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        fl.mainloop()

    # =++++++++++++++++++++++++++++++++++++++++++++++++++++Buns & Breads+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # \
    #  \
    #   \

    # ===============================Slice Breads =============================================================================================

    def SliceB(self):
        sb = Tk()
        self.sb = sb
        self.sb.geometry("680x450")
        self.sb.title("Billing Software")
        self.sb.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.sb, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"), fg="white", pady=2,
                      bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F1s = LabelFrame(self.sb, text="Slice Breads Items", font=("times new roman", 15, "bold"), bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F1s.place(x=0, y=75, width=680, height=375)

        sbcake1_label = Label(F1s, text="* White Normal Bread", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        sbcake1_label.place(x=30, y=10)
        sbcake1_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        sbcake2_label = Label(F1s, text="* Brown Normal Bread", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sbcake2_label.place(x=30, y=50)
        sbcake2_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        sbcake3_label = Label(F1s, text="*  Cherry Mix White Bread ", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        sbcake3_label.place(x=30, y=90, )
        sbcake3_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        sbcake4_label = Label(F1s, text="*  Pizza Bread", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sbcake4_label.place(x=30, y=130)
        sbcake4_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        sbcake5_label = Label(F1s, text="*  Pav Bhaji Bread", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        sbcake5_label.place(x=30, y=170, )
        sbcake5_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        sbcake6_label = Label(F1s, text="*  Big Burger Bread", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        sbcake6_label.place(x=30, y=210, )
        sbcake6_entry = Entry(F1s, width=8, bd=7, relief=SUNKEN, textvariable=self.sb6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F1s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        sb.mainloop()

    # ===============================Wheat Breads =============================================================================================
    def Wheatb(self):
        wb = Tk()
        self.wb = wb
        self.wb.geometry("680x450")
        self.wb.title("Billing Software")
        self.wb.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.wb, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.wb, text="Wheat Bread Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        wbcake1_label = Label(F2s, text="* Slice Wheat Bread", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wbcake1_label.place(x=30, y=10)
        wbcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        wbcake2_label = Label(F2s, text="* Chocolaty Bread", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wbcake2_label.place(x=30, y=50)
        wbcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        wbcake3_label = Label(F2s, text="*  Delightful Bread", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wbcake3_label.place(x=30, y=90, )
        wbcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        wbcake4_label = Label(F2s, text="*  Honey Wheat Bread", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wbcake4_label.place(x=30, y=130)
        wbcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        wbcake5_label = Label(F2s, text="*  Honey Wheat Bread Sara Lee", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        wbcake5_label.place(x=30, y=170, )
        wbcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        wbcake6_label = Label(F2s, text="*  Whole Grain Wheat Bread", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        wbcake6_label.place(x=30, y=210, )
        wbcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.wh6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        wb.mainloop()

    # ===============================Pizza =============================================================================================
    def Pizza(self):
        pz = Tk()
        self.pz = pz
        self.pz.geometry("680x450")
        self.pz.title("Billing Software")
        self.pz.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.pz, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.pz, text="Pizza Items", font=("times new roman", 25, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        pzcake1_label = Label(F2s, text="* Margherita Pizza", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        pzcake1_label.place(x=30, y=10)
        pzcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        pzcake2_label = Label(F2s, text="* Double Cheese Margherita Pizza", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        pzcake2_label.place(x=30, y=50)
        pzcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        pzcake3_label = Label(F2s, text="*  Peppy Paneer Pizza", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        pzcake3_label.place(x=30, y=90, )
        pzcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        pzcake4_label = Label(F2s, text="*  Maxican Green Wave", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        pzcake4_label.place(x=30, y=130)
        pzcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        pzcake5_label = Label(F2s, text="*  Deluxe Veggie", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        pzcake5_label.place(x=30, y=170, )
        pzcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        pzcake6_label = Label(F2s, text="*  Cheese N Corn", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        pzcake6_label.place(x=30, y=210, )
        pzcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.pz6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        pz.mainloop()

    # ===============================Burger =============================================================================================
    def Burger(self):
        brg = Tk()
        self.brg = brg
        self.brg.geometry("680x450")
        self.brg.title("Billing Software")
        self.brg.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.brg, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.brg, text="Burger Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        brgcake1_label = Label(F2s, text="* Perfect Lamb Satay Burger", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake1_label.place(x=30, y=10)
        brgcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg1,
                               font=("arial", 15, "bold")).place(x=450, y=10)

        brgcake2_label = Label(F2s, text="* Lamb And Tomato Stuffed Burger", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake2_label.place(x=30, y=50)
        brgcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg2,
                               font=("arial", 15, "bold")).place(x=450, y=50)

        brgcake3_label = Label(F2s, text="*  Chicken Feta Cheese Burger", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake3_label.place(x=30, y=90, )
        brgcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg3,
                               font=("arial", 15, "bold")).place(x=450, y=90)

        brgcake4_label = Label(F2s, text="*  Lentil And Mushroom Burger", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake4_label.place(x=30, y=130)
        brgcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg4,
                               font=("arial", 15, "bold")).place(x=450, y=130)

        brgcake5_label = Label(F2s, text="*  Stuffed Bean Burger", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake5_label.place(x=30, y=170, )
        brgcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg5,
                               font=("arial", 15, "bold")).place(x=450, y=170)

        brgcake6_label = Label(F2s, text="*  Lamb Burger With Radish Slaw", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        brgcake6_label.place(x=30, y=210, )
        brgcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bg6,
                               font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        brg.mainloop()

    # ===============================Hogdog=============================================================================================
    def Hogdog(self):
        hg = Tk()
        self.hg = hg
        self.hg.geometry("680x450")
        self.hg.title("Billing Software")
        self.hg.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.hg, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.hg, text="Hogdog Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        hgcake1_label = Label(F2s, text="* Chicago Style HotDog", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        hgcake1_label.place(x=30, y=10)
        hgcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        hgcake2_label = Label(F2s, text="* Dodger Hot Dog", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        hgcake2_label.place(x=30, y=50)
        hgcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        hgcake3_label = Label(F2s, text="*  Seattle Style Hot Dog", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        hgcake3_label.place(x=30, y=90, )
        hgcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        hgcake4_label = Label(F2s, text="*  Half Smoke HotDog", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        hgcake4_label.place(x=30, y=130)
        hgcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        hgcake5_label = Label(F2s, text="*  Riper Hot Dog ", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        hgcake5_label.place(x=30, y=170, )
        hgcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        hgcake6_label = Label(F2s, text="*  Italian Hot Dog", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        hgcake6_label.place(x=30, y=210, )
        hgcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.hd6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        hg.mainloop()

    # ===============================Toast =============================================================================================
    def Toast(self):
        ts = Tk()
        self.ts = ts
        self.ts.geometry("680x450")
        self.ts.title("Billing Software")
        self.ts.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.ts, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.ts, text="Toast Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        tscake1_label = Label(F2s, text="* Egg In A Blanket", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        tscake1_label.place(x=30, y=10)
        tscake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        tscake2_label = Label(F2s, text="* Mozzarella Toast", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        tscake2_label.place(x=30, y=50)
        tscake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        tscake3_label = Label(F2s, text="*  Masala Chiken On Toast", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        tscake3_label.place(x=30, y=90, )
        tscake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        tscake4_label = Label(F2s, text="*  Masala Chiken French Toast", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        tscake4_label.place(x=30, y=130)
        tscake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        tscake5_label = Label(F2s, text="*  MAshroom Paneer Toast", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        tscake5_label.place(x=30, y=170, )
        tscake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        tscake6_label = Label(F2s, text="*  Prawn and Sesame Toast", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        tscake6_label.place(x=30, y=210, )
        tscake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.to6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        ts.mainloop()

    # ===============================Brioche=============================================================================================
    def Brioche(self):
        bi = Tk()
        self.bi = bi
        self.bi.geometry("680x450")
        self.bi.title("Billing Software")
        self.bi.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.bi, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.bi, text="Brioche Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        bicake1_label = Label(F2s, text="* Brioche Bun", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        bicake1_label.place(x=30, y=10)
        bicake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        bicake2_label = Label(F2s, text="* Puff Donut", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bicake2_label.place(x=30, y=50)
        bicake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        bicake3_label = Label(F2s, text="*  Puff Pastry Brioche Mold", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bicake3_label.place(x=30, y=90, )
        bicake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        bicake4_label = Label(F2s, text="*  Suger Brioche Tart", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bicake4_label.place(x=30, y=130)
        bicake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        bicake5_label = Label(F2s, text="* Orange Brioche Bun ", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        bicake5_label.place(x=30, y=170, )
        bicake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        bicake6_label = Label(F2s, text="*  French Brioche", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        bicake6_label.place(x=30, y=210, )
        bicake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.bo6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        bi.mainloop()

    # ===============================Gummies & Chocolates=============================================================================================
    def Gummy(self):
        gum = Tk()
        self.gum = gum
        self.gum.geometry("680x450")
        self.gum.title("Billing Software")
        self.gum.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.gum, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.gum, text="Gummies & Candy Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        gumcake1_label = Label(F2s, text="* Haribo Chamallows Share Size Bag Pouch",
                               font=("times new roman", 17, "bold"), bg=bg_color,
                               fg="black")
        gumcake1_label.place(x=30, y=10)
        gumcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm1,
                               font=("arial", 15, "bold")).place(x=520, y=10)

        gumcake2_label = Label(F2s, text="* Haribo Goldbears Share Size Bag Pouch",
                               font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        gumcake2_label.place(x=30, y=50)
        gumcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm2,
                               font=("arial", 15, "bold")).place(x=520, y=50)

        gumcake3_label = Label(F2s, text="*  Haribo Happy Cola", font=("times new roman", 17, "bold"), bg=bg_color,
                               fg="black")
        gumcake3_label.place(x=30, y=90, )
        gumcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm3,
                               font=("arial", 15, "bold")).place(x=520, y=90)

        gumcake4_label = Label(F2s, text="*  Wrigley Snappy Straberry Gum Tape", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        gumcake4_label.place(x=30, y=130)
        gumcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm4,
                               font=("arial", 15, "bold")).place(x=520, y=130)

        gumcake5_label = Label(F2s, text="*  Wonka Rainbow Nerds Candy", font=("times new roman", 17, "bold"),
                               bg=bg_color,
                               fg="black")
        gumcake5_label.place(x=30, y=170, )
        gumcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm5,
                               font=("arial", 15, "bold")).place(x=520, y=170)

        gumcake6_label = Label(F2s,
                               text="*  Wonka For The Love of Nerds Gotta Have\n Grapes & seriously Strawnerry Candy",
                               font=("times new roman", 17, "bold"), bg=bg_color,
                               fg="black")
        gumcake6_label.place(x=30, y=210, )
        gumcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.gm6,
                               font=("arial", 15, "bold")).place(x=520, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        gum.mainloop()

    # ===============================lolipops=============================================================================================
    def Lolipops(self):
        lp = Tk()
        self.lp = lp
        self.lp.geometry("680x450")
        self.lp.title("Billing Software")
        self.lp.resizable(width=False, height=False)
        bg_color = "lightblue"
        title = Label(self.lp, text="BRIJWASI BAKERY", font=("times new roman", 30, "bold"),
                      fg="white", pady=2, bd=12, bg="Green", relief=GROOVE)
        title.pack(fill=X)

        F2s = LabelFrame(self.lp, text="Lollipop Items", font=("times new roman", 15, "bold"),
                         bg=bg_color,
                         relief=GROOVE, bd=10, fg="blue")
        F2s.place(x=0, y=75, width=680, height=375)

        lpcake1_label = Label(F2s, text="* Caramel Apple Pops", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        lpcake1_label.place(x=30, y=10)
        lpcake1_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp1,
                              font=("arial", 15, "bold")).place(x=450, y=10)

        lpcake2_label = Label(F2s, text="* Mini Tootise Pops", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        lpcake2_label.place(x=30, y=50)
        lpcake2_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp2,
                              font=("arial", 15, "bold")).place(x=450, y=50)

        lpcake3_label = Label(F2s, text="* Jolly Rancher Lollipops", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        lpcake3_label.place(x=30, y=90, )
        lpcake3_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp3,
                              font=("arial", 15, "bold")).place(x=450, y=90)

        lpcake4_label = Label(F2s, text="* Rainbow Whirly Pops", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        lpcake4_label.place(x=30, y=130)
        lpcake4_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp4,
                              font=("arial", 15, "bold")).place(x=450, y=130)

        lpcake5_label = Label(F2s, text="* Charms Sweet & Sour Pops", font=("times new roman", 17, "bold"),
                              bg=bg_color,
                              fg="black")
        lpcake5_label.place(x=30, y=170, )
        lpcake5_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp5,
                              font=("arial", 15, "bold")).place(x=450, y=170)

        lpcake6_label = Label(F2s, text="*  Blow Pops Bulk", font=("times new roman", 17, "bold"), bg=bg_color,
                              fg="black")
        lpcake6_label.place(x=30, y=210, )
        lpcake6_entry = Entry(F2s, width=8, bd=7, relief=SUNKEN, textvariable=self.lp6,
                              font=("arial", 15, "bold")).place(x=450, y=210)
        Submit = Button(F2s, bd=7, width=10, font=("arial 15 bold"),
                        text="Submit", bg="cadetblue", fg="white", padx=10, pady=5).place(x=200, y=260)

        lp.mainloop()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Save karna hai ya nahi???")
        if op > 0:
            self.bill_data = self.txtarea.get("1.0", END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
        else:
            messagebox.showinfo("theeek hai ", "tum nhi khush hm bhi khush!!!")

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.Choose.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Matab kuchh bhi daal de re, hadd hai yrr")

    def clear(self):
        op = messagebox.askyesno("Clear", "Sab saaf ho jaiega to fir mat kehna???")
        if op > 0:
            # ++++++++Drinks++++++++++++++++++++++++
            self.maza.set(0)
            self.coak.set(0)
            self.frooti.set(0)
            self.thump.set(0)
            self.appy.set(0)
            self.sprite.set(0)
            # ++++++++Total product price & tax+++++++++++++++++++++++++++
            self.t_amt.set(0)

            self.t_tax.set(0)

            # ++++++++++Customer's Details Variable++++++++++++++++++++++++++++++++++++++++++
            self.c_name.set("")
            self.c_phn.set("")
            self.bill_no.set("")
            x = random.randint(11111111, 99999999)
            self.bill_no.set(str(x))
            self.Choose.set("")
            self.welcome()

    def exit(self):
        op = messagebox.askyesno("Exit", "Bhara jana hai kya???")
        if op > 0:
            self.root.destroy()

    def total(self):
        self.t_pri = float(
            (self.sp1.get() * 40) +
            (self.sp2.get() * 140) +
            (self.sp3.get() * 100) +
            (self.sp4.get() * 90) +
            (self.sp5.get() * 200) +
            (self.sp6.get() * 50) +
            (self.bf1.get() * 200) +
            (self.bf2.get() * 200) +
            (self.bf3.get() * 200) +
            (self.bf4.get() * 200) +
            (self.bf5.get() * 200) +
            (self.bf6.get() * 200) +
            (self.st1.get() * 200) +
            (self.st2.get() * 200) +
            (self.st3.get() * 200) +
            (self.st4.get() * 200) +
            (self.st5.get() * 200) +
            (self.st6.get() * 200) +
            (self.wt1.get() * 200) +
            (self.wt2.get() * 200) +
            (self.wt3.get() * 200) +
            (self.wt4.get() * 200) +
            (self.wt5.get() * 200) +
            (self.wt6.get() * 200) +
            (self.cr1.get() * 200) +
            (self.cr2.get() * 200) +
            (self.cr3.get() * 200) +
            (self.cr4.get() * 200) +
            (self.cr5.get() * 200) +
            (self.cr6.get() * 200) +
            (self.fr1.get() * 200) +
            (self.fr2.get() * 200) +
            (self.fr3.get() * 200) +
            (self.fr4.get() * 200) +
            (self.fr5.get() * 200) +
            (self.fr6.get() * 200) +
            (self.sh1.get() * 200) +
            (self.sh2.get() * 200) +
            (self.sh3.get() * 200) +
            (self.sh4.get() * 200) +
            (self.sh5.get() * 200) +
            (self.sh6.get() * 200) +
            (self.co1.get() * 200) +
            (self.co2.get() * 200) +
            (self.co3.get() * 200) +
            (self.co4.get() * 200) +
            (self.co5.get() * 200) +
            (self.co6.get() * 200) +
            (self.fl1.get() * 200) +
            (self.fl2.get() * 200) +
            (self.fl3.get() * 200) +
            (self.fl4.get() * 200) +
            (self.fl5.get() * 200) +
            (self.fl6.get() * 200) +
            (self.sb1.get() * 200) +
            (self.sb2.get() * 200) +
            (self.sb3.get() * 200) +
            (self.sb4.get() * 200) +
            (self.sb5.get() * 200) +
            (self.sb6.get() * 200) +
            (self.wh1.get() * 200) +
            (self.wh2.get() * 200) +
            (self.wh3.get() * 200) +
            (self.wh4.get() * 200) +
            (self.wh5.get() * 200) +
            (self.wh6.get() * 200) +
            (self.pz1.get() * 200) +
            (self.pz2.get() * 200) +
            (self.pz3.get() * 200) +
            (self.pz4.get() * 200) +
            (self.pz5.get() * 200) +
            (self.pz6.get() * 200) +
            (self.bg1.get() * 200) +
            (self.bg2.get() * 200) +
            (self.bg3.get() * 200) +
            (self.bg4.get() * 200) +
            (self.bg5.get() * 200) +
            (self.bg6.get() * 200) +
            (self.hd1.get() * 200) +
            (self.hd2.get() * 200) +
            (self.hd3.get() * 200) +
            (self.hd4.get() * 200) +
            (self.hd5.get() * 200) +
            (self.hd6.get() * 200) +
            (self.to1.get() * 200) +
            (self.to2.get() * 200) +
            (self.to3.get() * 200) +
            (self.to4.get() * 200) +
            (self.to5.get() * 200) +
            (self.to6.get() * 200) +
            (self.lp1.get() * 200) +
            (self.lp2.get() * 200) +
            (self.lp3.get() * 200) +
            (self.lp4.get() * 200) +
            (self.lp5.get() * 200) +
            (self.lp6.get() * 200) +
            (self.gm1.get() * 200) +
            (self.gm2.get() * 200) +
            (self.gm3.get() * 200) +
            (self.gm4.get() * 200) +
            (self.gm5.get() * 200) +
            (self.gm6.get() * 200) +
            (self.bo1.get() * 200) +
            (self.bo2.get() * 200) +
            (self.bo3.get() * 200) +
            (self.bo4.get() * 200) +
            (self.bo5.get() * 200) +
            (self.bo6.get() * 200) +
            (self.maza.get() * 95) +
            (self.coak.get() * 90) +
            (self.frooti.get() * 110) +
            (self.thump.get() * 90) +
            (self.appy.get() * 200) +
            (self.sprite.get() * 80)
        )
        self.t_priTax = float(
            (self.maza.get() * 95) +
            (self.coak.get() * 90) +
            (self.frooti.get() * 110) +
            (self.thump.get() * 90) +
            (self.appy.get() * 200) +
            (self.sprite.get() * 80) +
            (self.sp1.get() * 40) +
            (self.sp2.get() * 140) +
            (self.sp3.get() * 100) +
            (self.sp4.get() * 90) +
            (self.sp5.get() * 200) +
            (self.sp6.get() * 50) +
            (self.bf1.get() * 200) +
            (self.bf2.get() * 200) +
            (self.bf3.get() * 200) +
            (self.bf4.get() * 200) +
            (self.bf5.get() * 200) +
            (self.bf6.get() * 200) +
            (self.st1.get() * 200) +
            (self.st2.get() * 200) +
            (self.st3.get() * 200) +
            (self.st4.get() * 200) +
            (self.st5.get() * 200) +
            (self.st6.get() * 200) +
            (self.wt1.get() * 200) +
            (self.wt2.get() * 200) +
            (self.wt3.get() * 200) +
            (self.wt4.get() * 200) +
            (self.wt5.get() * 200) +
            (self.wt6.get() * 200) +
            (self.cr1.get() * 200) +
            (self.cr2.get() * 200) +
            (self.cr3.get() * 200) +
            (self.cr4.get() * 200) +
            (self.cr5.get() * 200) +
            (self.cr6.get() * 200) +
            (self.fr1.get() * 200) +
            (self.fr2.get() * 200) +
            (self.fr3.get() * 200) +
            (self.fr4.get() * 200) +
            (self.fr5.get() * 200) +
            (self.fr6.get() * 200) +
            (self.sh1.get() * 200) +
            (self.sh2.get() * 200) +
            (self.sh3.get() * 200) +
            (self.sh4.get() * 200) +
            (self.sh5.get() * 200) +
            (self.sh6.get() * 200) +
            (self.co1.get() * 200) +
            (self.co2.get() * 200) +
            (self.co3.get() * 200) +
            (self.co4.get() * 200) +
            (self.co5.get() * 200) +
            (self.co6.get() * 200) +
            (self.fl1.get() * 200) +
            (self.fl2.get() * 200) +
            (self.fl3.get() * 200) +
            (self.fl4.get() * 200) +
            (self.fl5.get() * 200) +
            (self.fl6.get() * 200) +
            (self.sb1.get() * 200) +
            (self.sb2.get() * 200) +
            (self.sb3.get() * 200) +
            (self.sb4.get() * 200) +
            (self.sb5.get() * 200) +
            (self.sb6.get() * 200) +
            (self.wh1.get() * 200) +
            (self.wh2.get() * 200) +
            (self.wh3.get() * 200) +
            (self.wh4.get() * 200) +
            (self.wh5.get() * 200) +
            (self.wh6.get() * 200) +
            (self.pz1.get() * 200) +
            (self.pz2.get() * 200) +
            (self.pz3.get() * 200) +
            (self.pz4.get() * 200) +
            (self.pz5.get() * 200) +
            (self.pz6.get() * 200) +
            (self.bg1.get() * 200) +
            (self.bg2.get() * 200) +
            (self.bg3.get() * 200) +
            (self.bg4.get() * 200) +
            (self.bg5.get() * 200) +
            (self.bg6.get() * 200) +
            (self.hd1.get() * 200) +
            (self.hd2.get() * 200) +
            (self.hd3.get() * 200) +
            (self.hd4.get() * 200) +
            (self.hd5.get() * 200) +
            (self.hd6.get() * 200) +
            (self.to1.get() * 200) +
            (self.to2.get() * 200) +
            (self.to3.get() * 200) +
            (self.to4.get() * 200) +
            (self.to5.get() * 200) +
            (self.to6.get() * 200) +
            (self.lp1.get() * 200) +
            (self.lp2.get() * 200) +
            (self.lp3.get() * 200) +
            (self.lp4.get() * 200) +
            (self.lp5.get() * 200) +
            (self.lp6.get() * 200) +
            (self.gm1.get() * 200) +
            (self.gm2.get() * 200) +
            (self.gm3.get() * 200) +
            (self.gm4.get() * 200) +
            (self.gm5.get() * 200) +
            (self.gm6.get() * 200) +
            (self.bo1.get() * 200) +
            (self.bo2.get() * 200) +
            (self.bo3.get() * 200) +
            (self.bo4.get() * 200) +
            (self.bo5.get() * 200) +
            (self.bo6.get() * 200)
        )

        self.ttl = self.t_pri + self.t_priTax
        self.sum = 0
        self.sum = self.sum + self.ttl
        self.t_amt.set(str(self.sum))
        self.sumt = 0
        self.sumt = self.sumt + self.t_priTax
        self.t_tax.set(str(self.sumt))

    # def Submit(self):
    #
    #     self.t_pri=float(
    #
    #
    #                                 (self.sp1.get()*40)+
    #                                 (self.sp2.get()*140)+
    #                                 (self.sp3.get()*100)+
    #                                 (self.sp4.get()*90)+
    #                                 (self.sp5.get()*200)+
    #                                 (self.sp6.get()*50)+
    #                                 (self.bf1.get() * 200) +
    #                                 (self.bf2.get() * 200) +
    #                                 (self.bf3.get() * 200) +
    #                                 (self.bf4.get() * 200)+
    #                                 (self.bf5.get() * 200) +
    #                                 (self.bf6.get() * 200) +
    #                                 (self.st1.get() * 200)+
    #                                 (self.st2.get() * 200) +
    #                                 (self.st3.get() * 200) +
    #                                 (self.st4.get() * 200) +
    #                                 (self.st5.get() * 200) +
    #                                 (self.st6.get() * 200) +
    #                                 (self.wt1.get() * 200) +
    #                                 (self.wt2.get() * 200) +
    #                                 (self.wt3.get() * 200) +
    #                                 (self.wt4.get() * 200) +
    #                                 (self.wt5.get() * 200) +
    #                                 (self.wt6.get() * 200) +
    #                                 (self.cr1.get() * 200) +
    #                                 (self.cr2.get() * 200) +
    #                                 (self.cr3.get() * 200) +
    #                                 (self.cr4.get() * 200) +
    #                                 (self.cr5.get() * 200) +
    #                                 (self.cr6.get() * 200)+
    #                                 (self.fr1.get() * 200) +
    #                                 (self.fr2.get() * 200) +
    #                                 (self.fr3.get() * 200) +
    #                                 (self.fr4.get() * 200) +
    #                                 (self.fr5.get() * 200) +
    #                                 (self.fr6.get() * 200) +
    #                                 (self.sh1.get() * 200) +
    #                                 (self.sh2.get() * 200) +
    #                                 (self.sh3.get() * 200) +
    #                                 (self.sh4.get() * 200) +
    #                                 (self.sh5.get() * 200) +
    #                                 (self.sh6.get() * 200)+
    #                                 (self.co1.get() * 200) +
    #                                 (self.co2.get() * 200) +
    #                                 (self.co3.get() * 200) +
    #                                 (self.co4.get() * 200) +
    #                                 (self.co5.get() * 200) +
    #                                 (self.co6.get() * 200)+
    #                                 (self.fl1.get() * 200) +
    #                                 (self.fl2.get() * 200) +
    #                                 (self.fl3.get() * 200) +
    #                                 (self.fl4.get() * 200) +
    #                                 (self.fl5.get() * 200) +
    #                                 (self.fl6.get() * 200) +
    #                                 (self.sb1.get() * 200) +
    #                                 (self.sb2.get() * 200) +
    #                                 (self.sb3.get() * 200) +
    #                                 (self.sb4.get() * 200) +
    #                                 (self.sb5.get() * 200) +
    #                                 (self.sb6.get() * 200) +
    #                                 (self.wh1.get() * 200) +
    #                                 (self.wh2.get() * 200) +
    #                                 (self.wh3.get() * 200) +
    #                                 (self.wh4.get() * 200) +
    #                                 (self.wh5.get() * 200) +
    #                                 (self.wh6.get() * 200) +
    #                                 (self.pz1.get() * 200) +
    #                                 (self.pz2.get() * 200) +
    #                                 (self.pz3.get() * 200) +
    #                                 (self.pz4.get() * 200) +
    #                                 (self.pz5.get() * 200) +
    #                                 (self.pz6.get() * 200) +
    #                                 (self.bg1.get() * 200) +
    #                                 (self.bg2.get() * 200) +
    #                                 (self.bg3.get() * 200) +
    #                                 (self.bg4.get() * 200) +
    #                                 (self.bg5.get() * 200) +
    #                                 (self.bg6.get() * 200) +
    #                                 (self.hd1.get() * 200) +
    #                                 (self.hd2.get() * 200) +
    #                                 (self.hd3.get() * 200) +
    #                                 (self.hd4.get() * 200) +
    #                                 (self.hd5.get() * 200) +
    #                                 (self.hd6.get() * 200) +
    #                                 (self.to1.get() * 200) +
    #                                 (self.to2.get() * 200) +
    #                                 (self.to3.get() * 200) +
    #                                 (self.to4.get() * 200) +
    #                                 (self.to5.get() * 200) +
    #                                 (self.to6.get() * 200) +
    #                                 (self.lp1.get() * 200) +
    #                                 (self.lp2.get() * 200) +
    #                                 (self.lp3.get() * 200) +
    #                                 (self.lp4.get() * 200) +
    #                                 (self.lp5.get() * 200) +
    #                                 (self.lp6.get() * 200) +
    #                                 (self.gm1.get() * 200) +
    #                                 (self.gm2.get() * 200) +
    #                                 (self.gm3.get() * 200) +
    #                                 (self.gm4.get() * 200) +
    #                                 (self.gm5.get() * 200) +
    #                                 (self.gm6.get() * 200) +
    #                                 (self.bo1.get() * 200) +
    #                                 (self.bo2.get() * 200) +
    #                                 (self.bo3.get() * 200) +
    #                                 (self.bo4.get() * 200) +
    #                                 (self.bo5.get() * 200) +
    #                                 (self.bo6.get() * 200)+
    #                                 (self.maza.get() * 95) +
    #                                 (self.coak.get() * 90) +
    #                                 (self.frooti.get() * 110) +
    #                                 (self.thump.get() * 90) +
    #                                 (self.appy.get() * 200) +
    #                                 (self.sprite.get() * 80)
    #
    #     )
    #     self.t_priTax = float(
    #         (self.maza.get() * 95) +
    #         (self.coak.get() * 90) +
    #         (self.frooti.get() * 110) +
    #         (self.thump.get() * 90) +
    #         (self.appy.get() * 200) +
    #         (self.sprite.get() * 80) +
    #         (self.sp1.get() * 40) +
    #         (self.sp2.get() * 140) +
    #         (self.sp3.get() * 100) +
    #         (self.sp4.get() * 90) +
    #         (self.sp5.get() * 200) +
    #         (self.sp6.get() * 50) +
    #         (self.bf1.get() * 200) +
    #         (self.bf2.get() * 200) +
    #         (self.bf3.get() * 200) +
    #         (self.bf4.get() * 200) +
    #         (self.bf5.get() * 200) +
    #         (self.bf6.get() * 200) +
    #         (self.st1.get() * 200) +
    #         (self.st2.get() * 200) +
    #         (self.st3.get() * 200) +
    #         (self.st4.get() * 200) +
    #         (self.st5.get() * 200) +
    #         (self.st6.get() * 200) +
    #         (self.wt1.get() * 200) +
    #         (self.wt2.get() * 200) +
    #         (self.wt3.get() * 200) +
    #         (self.wt4.get() * 200) +
    #         (self.wt5.get() * 200) +
    #         (self.wt6.get() * 200) +
    #         (self.cr1.get() * 200) +
    #         (self.cr2.get() * 200) +
    #         (self.cr3.get() * 200) +
    #         (self.cr4.get() * 200) +
    #         (self.cr5.get() * 200) +
    #         (self.cr6.get() * 200) +
    #         (self.fr1.get() * 200) +
    #         (self.fr2.get() * 200) +
    #         (self.fr3.get() * 200) +
    #         (self.fr4.get() * 200) +
    #         (self.fr5.get() * 200) +
    #         (self.fr6.get() * 200) +
    #         (self.sh1.get() * 200) +
    #         (self.sh2.get() * 200) +
    #         (self.sh3.get() * 200) +
    #         (self.sh4.get() * 200) +
    #         (self.sh5.get() * 200) +
    #         (self.sh6.get() * 200) +
    #         (self.co1.get() * 200) +
    #         (self.co2.get() * 200) +
    #         (self.co3.get() * 200) +
    #         (self.co4.get() * 200) +
    #         (self.co5.get() * 200) +
    #         (self.co6.get() * 200) +
    #         (self.fl1.get() * 200) +
    #         (self.fl2.get() * 200) +
    #         (self.fl3.get() * 200) +
    #         (self.fl4.get() * 200) +
    #         (self.fl5.get() * 200) +
    #         (self.fl6.get() * 200) +
    #         (self.sb1.get() * 200) +
    #         (self.sb2.get() * 200) +
    #         (self.sb3.get() * 200) +
    #         (self.sb4.get() * 200) +
    #         (self.sb5.get() * 200) +
    #         (self.sb6.get() * 200) +
    #         (self.wh1.get() * 200) +
    #         (self.wh2.get() * 200) +
    #         (self.wh3.get() * 200) +
    #         (self.wh4.get() * 200) +
    #         (self.wh5.get() * 200) +
    #         (self.wh6.get() * 200) +
    #         (self.pz1.get() * 200) +
    #         (self.pz2.get() * 200) +
    #         (self.pz3.get() * 200) +
    #         (self.pz4.get() * 200) +
    #         (self.pz5.get() * 200) +
    #         (self.pz6.get() * 200) +
    #         (self.bg1.get() * 200) +
    #         (self.bg2.get() * 200) +
    #         (self.bg3.get() * 200) +
    #         (self.bg4.get() * 200) +
    #         (self.bg5.get() * 200) +
    #         (self.bg6.get() * 200) +
    #         (self.hd1.get() * 200) +
    #         (self.hd2.get() * 200) +
    #         (self.hd3.get() * 200) +
    #         (self.hd4.get() * 200) +
    #         (self.hd5.get() * 200) +
    #         (self.hd6.get() * 200) +
    #         (self.to1.get() * 200) +
    #         (self.to2.get() * 200) +
    #         (self.to3.get() * 200) +
    #         (self.to4.get() * 200) +
    #         (self.to5.get() * 200) +
    #         (self.to6.get() * 200) +
    #         (self.lp1.get() * 200) +
    #         (self.lp2.get() * 200) +
    #         (self.lp3.get() * 200) +
    #         (self.lp4.get() * 200) +
    #         (self.lp5.get() * 200) +
    #         (self.lp6.get() * 200) +
    #         (self.gm1.get() * 200) +
    #         (self.gm2.get() * 200) +
    #         (self.gm3.get() * 200) +
    #         (self.gm4.get() * 200) +
    #         (self.gm5.get() * 200) +
    #         (self.gm6.get() * 200) +
    #         (self.bo1.get() * 200) +
    #         (self.bo2.get() * 200) +
    #         (self.bo3.get() * 200) +
    #         (self.bo4.get() * 200) +
    #         (self.bo5.get() * 200) +
    #         (self.bo6.get() * 200)
    #     )
    #
    #     self.ttl = self.amt+ self.t_priTax
    #     self.sum = 0
    #     self.sum = self.sum + self.ttl
    #     self.t_amt.set(str(self.sum))
    #     self.sumt = 0
    #     self.sumt = self.sumt + self.t_priTax
    #     self.t_tax.set(str(self.sumt))
    # self.t_amt.set(str(self.ttl))
    # self.t_tax.set(str(self.t_priTax))

    def welcome(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,
                            "\t     Welcome To Brijwasi Bakery \n\t    ===============================\n \t        Alambagh,Nahar,Lucknow.\n\t    ===============================")
        self.txtarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number : {self.c_phn.get()}")
        self.txtarea.insert(END, "\n===================================================== ")
        self.txtarea.insert(END, "\nProduct\t\t\tQty\t\tPrice ")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phn.get() == "":
            messagebox.showerror("hdd paar kiye ho yaar", "Name or Phone number pura bharo!!")
        elif self.t_amt.get() == '0.0' and self.t_tax.get() == '0.0':
            messagebox.showerror("hdd paar kiye ho yrr",
                                 "Product liye nahi ho or bill generate kar rahe ho mtlb hdd hai yrr!!")
        else:
            self.welcome()
            # if self.maza.get() ==0:

            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t\t{self.maza.get()}\t\t{self.maza.get() * 95} ")
            if self.coak.get() != 0:
                self.txtarea.insert(END, f"\n Cock\t\t\t{self.coak.get()}\t\t{self.coak.get() * 90} ")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t\t{self.frooti.get()}\t\t{self.frooti.get() * 110} ")
            if self.thump.get() != 0:
                self.txtarea.insert(END, f"\n Thumps Up\t\t\t{self.thump.get()}\t\t{self.thump.get() * 90} ")
            if self.appy.get() != 0:
                self.txtarea.insert(END, f"\n Appy Fizz\t\t\t{self.appy.get()}\t\t{self.appy.get() * 200} ")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t\t{self.sprite.get()}\t\t{self.sprite.get() * 80} ")
            self.txtarea.insert(END, "\n-----------------------------------------------------")
            if self.t_tax.get() != '0.0':
                self.txtarea.insert(END, f"\nTotal Tax\t\t\t\t\t {self.t_tax.get()}   ")

            self.txtarea.insert(END, "\n-----------------------------------------------------")

            self.txtarea.insert(END, f"\nTotal\t\t\t\t\t{self.total}")
            if self.total != 0:
                self.txtarea.insert(END, "\n-----------------------------------------------------")
                self.txtarea.insert(END, f"\nThank U For Shoping With Us ,Have a Nice Day!!!")
                self.save_bill()


root = Tk()
obj = BILL_App(root)
root.mainloop()
