from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")

def TIME():
    STR11= strftime('%H:%M:%S:%p')
    label.config(text=STR11)
    label.after(1000,TIME)

label = Label(root,font=("Helvetica",80),background="black",foreground="blue")
label.pack(anchor='center')
TIME()
mainloop()
