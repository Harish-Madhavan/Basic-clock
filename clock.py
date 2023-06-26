from tkinter import *
from time import strftime
import customtkinter

#customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
#customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title("clock")

def TIME():
    STR11= strftime('%H:%M:%S:%p')
    label.configure(text=STR11)
    label.after(1000,TIME)

#label = Label(root,font=("Helvetica",80),background="black",foreground="blue")
label = customtkinter.CTkLabel(root,font=("Helvetica",80), fg_color="blue")
label.pack(anchor='center')
TIME()
root.mainloop()
