from tkinter import *
from tkinter.ttk import *

from PG_MAIN import *

root = Tk()
root.geometry("400x150")
root.title("Password Generator")

def cur_value():
    pwd_len.config(from_=int(upcase_len.get())+int(lowcase_len.get())+int(dgt_len.get())+int(punct_len.get()))
    upcase_len.config(to=int(pwd_len.get())-int(lowcase_len.get())-int(dgt_len.get())-int(punct_len.get()))
    lowcase_len.config(to=int(pwd_len.get())-int(upcase_len.get())-int(dgt_len.get())-int(punct_len.get()))
    dgt_len.config(to=int(pwd_len.get())-int(upcase_len.get())-int(lowcase_len.get())-int(punct_len.get()))
    punct_len.config(to=int(pwd_len.get())-int(upcase_len.get())-int(lowcase_len.get())-int(dgt_len.get()))

#password length
cur_pwd_length = Variable(value=16)
pwd_len_lbl = Label(root, text="Enter password length: ")
pwd_len_lbl.grid(column = 0, row = 0)

pwd_len = Spinbox(root, from_=8, to=70, textvariable= cur_pwd_length, state = "readonly")
pwd_len.grid(column = 1, row = 0)

#uppercase
cur_upcase_len = Variable(value=1)
upcase_lbl = Label(root, text="Enter number of uppercase letters: ")
upcase_lbl.grid(column = 0, row = 1)

upcase_len = Spinbox(root, from_=0, to=40,textvariable= cur_upcase_len, command = cur_value, state = "readonly")
upcase_len.grid(column = 1, row = 1)

#lowercase
cur_lowcase_len = Variable(value=1)
lowcase_lbl = Label(root, text="Enter number of lowercase letters: ")
lowcase_lbl.grid(column = 0, row = 2)

lowcase_len = Spinbox(root, from_=0, to=40, textvariable= cur_lowcase_len, command = cur_value, state = "readonly")
lowcase_len.grid(column = 1, row = 2)

#digits
cur_dgt_len = Variable(value=1)
dgt_lbl = Label(root, text="Enter number of digits: ")
dgt_lbl.grid(column = 0, row = 3)

dgt_len = Spinbox(root, from_=0, to = 40, textvariable = cur_dgt_len, command = cur_value, state = "readonly")
dgt_len.grid(column = 1, row = 3)

#punct
cur_punct_len = Variable(value=1)
punct_lbl = Label(root, text="Enter number of punct: ")
punct_lbl.grid(column = 0, row = 4)

punct_len = Spinbox(root, from_=0, to = 40, textvariable = cur_punct_len, command = cur_value, state = "readonly")
punct_len.grid(column = 1, row = 4)





def generate_button():
     pwd_lbl.delete(0,END)
     pwd_lbl.insert(0,generate_password(int(pwd_len.get()), int(upcase_len.get()), 
     int(lowcase_len.get()), int(dgt_len.get()), int(punct_len.get())))
     print(pwd_len.get())

#password label
pwd_lbl = Entry(root)
pwd_lbl.grid(row = 5, column=0, columnspan = 2, ipadx=130)




#add button
generate = Button(root, text = "Generate", command=generate_button)
generate.grid(column = 0, row = 6)


root.mainloop()