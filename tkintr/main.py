import tkinter as tk
root = tk.Tk()
from tkinter.messagebox import showinfo, showwarning

root.geometry("600x600")
root.title("Restaurant Mnagement System")
# root.attributes('-alpha',0.88)
message = tk.Label(root, text="Welcome to mr prince")
# img = tk.PhotoImage(file = "icon.png")


def showLogin(title,message):
        showinfo(title=title, message=message)

def callDialog():
    showLogin("hello","hi")


login =tk.Button(root, text="Login", command=callDialog, compound=tk.LEFT)
signup = tk.Button(root, text="Signup", command=callDialog)
ck = tk.Checkbutton(root,text= "check krbo ki naahi")
message.pack()
login.pack()
signup.pack(ipadx=30,ipady=5)
ck.pack()
root.mainloop()
