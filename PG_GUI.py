from tkinter import *
from tkinter.ttk import *

from PG_MAIN import *

root = Tk()
root.geometry("400x100")
root.title("Password Generator")



#password length
cur_pwd_length = Variable(value=16)
pwd_len_lbl = Label(root, text="Enter password length: ")
pwd_len_lbl.grid(column = 0, row = 0)

pwd_len = Spinbox(root, from_=8, to=40, textvariable= cur_pwd_length)
pwd_len.grid(column = 1, row = 0)

#uppercase
cur_upcase_len = Variable(value=1)
upcase_lbl = Label(root, text="Enter number of uppercase letters: ")
upcase_lbl.grid(column = 0, row = 1)

upcase_len = Spinbox(root, from_=0, to=40,textvariable= cur_upcase_len)
upcase_len.grid(column = 1, row = 1)

#lowercase
cur_lowcase_len = Variable(value=1)
lowcase_lbl = Label(root, text="Enter number of lowercase letters: ")
lowcase_lbl.grid(column = 0, row = 2)

lowcase_len = Spinbox(root, from_=0, to=40, textvariable= cur_lowcase_len)
lowcase_len.grid(column = 1, row = 2)

# #digits
# dgt_lbl = Label(root, text="Enter number of digits: ")
# dgt_lbl.grid(column = 0, row = 3)

# dgt_len = Spinbox(root, from_=0, to = max_number(), textvariable=  Variable(value = 0))
# dgt_len.grid(column = 1, row = 3)






# def generate_button():
#     pwd_lbl.config(text=generate_password(int(pwd_len.get())))
#     print(pwd_len.get())

# #password label
# pwd_lbl = Label(root)
# pwd_lbl.pack(side = "top")




# #add button
# generate = Button(root, text = "Generate", command=generate_button)
# generate.pack(side = "bottom")


root.mainloop()