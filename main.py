from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)


lable = Label(root,font=("DAGGERSQUARE", 50), background="black", foreground="white")
lable.pack(anchor="center")
time()

mainloop()
