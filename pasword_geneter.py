from tkinter import *
import string
import random

root = Tk()
root.geometry("480x300")
root.title("password generator aap")

def gen():

    num = int(e1.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
     
    random.shuffle(s)
    password = S [0:num]


    l4 = Label(root, text = "password :", font =" time 15 bold")
    l4.place(x = 30, y = 250)

    l5 = Label(root, text = password , font =" time 15 bold", width = 24, bg = "white")
    l5.place(x = 150, y = 250)





l1 = Label(root, text = "password generator app", font =" time 15 bold")
l1.place(x = 30, y = 30)

l2 = Label(root, text = "Enter password Length", font =" time 15 bold")
l2.place(x = 30, y = 90)

e1 = Entry(root,width=46,bd=2,font="time 13 bold")
e1.place(x=30, y=133)
Button= Button(root,text="generator password", fg = "white",bg = "blue",font="time 15 bold",width=34,command = gen )
Button.place(x=30,y=180)

root.mainloop()
