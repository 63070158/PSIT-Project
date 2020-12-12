#importing 

from tkinter import *
import random, string
import pyperclip

###initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PSIT PROJECT - PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold', fg="blue").pack()
Label(root, text ='PSIT PROJECT', font ='arial 15 bold', fg="green").pack(side = BOTTOM)


###select password length
pass_label = Label(root, text = 'RECOMMEND PASSWORD LENGTH UP TO 12 CHARACTER', font = 'arial 10 bold', fg="white", bg="red").pack()
##pass_len = IntVar()
##length = Spinbox(root, from_ = 12, to_ = 32 , textvariable = pass_len , width = 15).pack()
pass_label = Label(root, text = 'UPPER CHARACTER', font = 'arial 10 bold').pack()
pass_len2 = IntVar()
length = Spinbox(root, from_ = 0, to_ = 32 , textvariable = pass_len2 , width = 15).pack()
pass_label = Label(root, text = 'LOWER CHARACTER', font = 'arial 10 bold').pack()
pass_len3 = IntVar()
length = Spinbox(root, from_ = 0, to_ = 32 , textvariable = pass_len3 , width = 15).pack()
pass_label = Label(root, text = 'DIGITS CHARACTER', font = 'arial 10 bold').pack()
pass_len4 = IntVar()
length = Spinbox(root, from_ = 0, to_ = 32 , textvariable = pass_len4 , width = 15).pack()
pass_label = Label(root, text = 'PUNCTUATION CHARACTER', font = 'arial 10 bold').pack()
pass_len5 = IntVar()
length = Spinbox(root, from_ = 0, to_ = 32 , textvariable = pass_len5 , width = 15).pack()


#####define function

pass_str = StringVar()

def test():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

def Generator():
    """ส่วนที่ทำ Pass"""
    password = ""
    for _ in range(pass_len2.get()):
        cha = random.choice(string.ascii_uppercase)
        password += cha
    for _ in range(pass_len3.get()):
        cha = random.choice(string.ascii_lowercase)
        password += cha
    for _ in range(pass_len4.get()):
        cha = random.choice(string.digits)
        password += cha
    for _ in range(pass_len5.get()):
        cha = random.choice(string.punctuation)
        password += cha
    password_tosup = list(password)
    password = ""
    random.shuffle(password_tosup)
    password = "".join(password_tosup)
    pass_str.set(password)

###button

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
