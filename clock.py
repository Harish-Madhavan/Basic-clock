from time import strftime
import customtkinter

root = customtkinter.CTk()
root.title("clock")

def TIME():
    STR11= strftime('%H:%M:%S:%p')
    label.configure(text=STR11)
    label.after(1000,TIME)

label = customtkinter.CTkLabel(root,font=("Helvetica",80), fg_color="blue")
label.pack(anchor='center')
TIME()
root.mainloop()
