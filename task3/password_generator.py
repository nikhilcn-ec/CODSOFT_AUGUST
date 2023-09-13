from tkinter import *
from math import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import Image,ImageTk
import string
import random
import tkinter.messagebox as ms

#assigning the methods of ttkbootstarp to a variable object
window=tb.Window(themename="solar",title="password generator")
window.geometry("300x350")

#icon and resizing of images used in this project
window.iconbitmap("C:/Users/admin/Desktop/codsoft/task3/icon.ico")
image=Image.open("C:/Users/admin/Desktop/codsoft/task3/img.png")
image=image.resize((100,100),  Image.LANCZOS)
img=ImageTk.PhotoImage(image)


#the function evaluates trhe password entered by user
def submit():
   pswrd_length=eval(entry.get())
   pswrd=[]
   if(pswrd_length<8):
        ms.showinfo("unexpected input","length of the password should be atleast 8")
   else:
    charset=string.ascii_uppercase+string.ascii_uppercase+string.punctuation+string.digits
    pswrd.append(random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.punctuation)+random.choice(string.digits))
   for i in range(0,pswrd_length-4):
    pswrd.append(random.choice(charset))

    random.shuffle(pswrd)
    password="".join(pswrd)

#this deletes entire content in the frame
    for widgets in frame.winfo_children():
      widgets.destroy()

#prints generated password to the screen
    global l2,l3
    l2=tb.Label(frame,text="Generated Password",font=("Roboto",14,"bold"),bootstyle="info")
    l2.place(x=40,y=50)
    l3=tb.Label(frame,text=password,font=("Roboto",14),bootstyle="danger")
    l3.place(x=70,y=100)
   





#on triggered this function prompt user to enter the length of passowrd 
def onclick():
    for widgets in frame.winfo_children():
      widgets.destroy()
    global entry,l1,b2
    l1=tb.Label(frame,text="Enter length of password",font=("roboto",12))
    l1.place(x=48,y=50)
    b2=tb.Button(frame,text="submit",bootstyle="danger-outline",width=7,command=submit)
    b2.place(x=100,y=180)
    entry=tb.Entry(frame,bootstyle="danger",font=("Roboto",14),width=10)
    entry.place(x=70,y=100)



#the home frame that is viewed intially by user
frame=tb.Frame(window,width=250,height=300)
img_label=tb.Label(frame,image=img)
img_label.place(x=75,y=70)
b=tb.Button(frame,text="generate password",bootstyle="success-outline",command=onclick)
b.place(x=63,y=200)
frame.pack(padx=20,pady=10)

#create gui window with all above widgets or encloseed init
window.mainloop()