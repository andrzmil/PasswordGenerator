from tkinter import *
from tkinter.ttk import *

from PG_MAIN import *

root = Tk()
root.geometry("400x100")
root.title("Password Generator")


#password length
cur_pwd_length = StringVar(value=16)
pwd_len = Spinbox(root, from_=8, to=40, textvariable= cur_pwd_length)
pwd_len.pack()

def generate_button():
    pwd_lbl.config(text=generate_password(int(pwd_len.get())))
    print(pwd_len.get())

#password label
pwd_lbl = Label(root)
pwd_lbl.pack(side = "top")




#add button
generate = Button(root, text = "Generate", command=generate_button)
generate.pack(side = "bottom")


root.mainloop()