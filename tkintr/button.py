import calendar
import tkinter as tk
from tkinter import*

# import fun as fun
from tkinter import messagebox

root = tk.Tk()
root.title("Buttons of Tkinter")
root.geometry("500x500")
def msg():
    messagebox.showinfo("Hello", "Simple Button clicked")

def msg1():
    messagebox.askquestion("Hello", "Red Button clicked")

def msg2():
    messagebox.showerror("Hello", "Blue Button clicked")

b1 = tk.Button(root,text = "Simple",command =msg)
b2 = tk.Button(root,text = "Red",command=msg1,activeforeground = "red",activebackground = "pink",pady=25,padx=25)
b3 = tk.Button(root,text = "Blue",command=msg2,activeforeground = "blue",activebackground = "Purple",pady=25,padx=25)


c = tk.Canvas(root, bg ="pink", height ="200")

arc = c.create_arc((5,10,150,200),start = -180,extent = -180, fill= "white")
name = tk.Label(root, text = "Name")
e1 = Entry(root).place(x = 80, y = 50)



b1.pack(side=LEFT)
b2.pack()
b3.pack()
c.pack()
name.pack()

root.mainloop()

