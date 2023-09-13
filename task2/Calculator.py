from tkinter import *
from math import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import ttkbootstrap.icons
from PIL import Image,ImageTk

#creating object and assigning  tkkbootstrap methods 
window=tb.Window(title="CALCULATOR",themename="darkly")
window.iconbitmap("c:/Users/admin/Desktop/codsoft/task2/logo.ico")
window.geometry("300x330")

#creating a coustamize style for button
my_style=tb.Style()
my_style.configure("danger.TButton",font=("Roboto",18))
my_style.configure("info.Outline.TButton",font=("Roboto",18))
my_style.configure("success.TButton",font=("Roboto",18))
my_style.configure("light.Outline.TButton",font=("Roboto",18))


#cal function evaluates or calculates and configures the value on screnn
def cal():
    value=str(eval(str1)) 
    d_label.configure(text=value)   
    d_label.place_configure(x=280-(15*len(value)))

#def functions displays the content of button pressed on triggered
def disp(x):
    global str1
    global d_str
    if(x=="%" ):
        str1=str1+"/100*"
    elif(x=="x"):
        str1=str1+"*"
    else:     
        str1=str1+x
    d_str=d_str+x
    d_label.configure(text=d_str)
    d_label.place_configure(x=280-(15*len(d_str)))

#function clears entire content on screen when triggered
def clear():
    d_label.configure(text="")
    global str1,d_str
    str1=""
    d_str=""



# string variables to store entry value in string
str1=""
d_str=""

#entry frame which dispalys users input and the result
e_frame=tb.Frame(window,bootstyle="secondary",width=290,height=60)
d_label=tb.Label(e_frame,text=d_str,font=("roboto",20),bootstyle="inverse-secondary")
d_label.place(x=280,y=8)
e_frame.pack(pady=10)


#button frame which consists of all buttons in calculator
b_frame=tb.Frame(window,width=290,height=245)
c_but=tb.Button(b_frame,text="C",bootstyle="danger",style="danger.TButton",width=6,command=clear)
c_but.place(x=1,y=2)
p_but=tb.Button(b_frame,text="%",bootstyle="info-outline",width=5,command=lambda :disp("%"))
p_but.place(x=107,y=1)
d_but=tb.Button(b_frame,text="/",bootstyle="info-outline",width=5,command=lambda :disp("/"))
d_but.place(x=200,y=1)
m_but=tb.Button(b_frame,text="x",bootstyle="info-outline",width=5,command=lambda :disp("x"))
m_but.place(x=200,y=50)
min_but=tb.Button(b_frame,text="-",bootstyle="info-outline",width=5,command=lambda :disp("-"))
min_but.place(x=200,y=100)
a_but=tb.Button(b_frame,text="+",bootstyle="info-outline",width=5,command=lambda :disp("+"))
a_but.place(x=200,y=150)
s_but=tb.Button(b_frame,text="=",bootstyle="success",width=5,command=cal)
s_but.place(x=200,y=200)

but1=tb.Button(b_frame,text="1",bootstyle="light-outline",width=3,command=lambda :disp("1"))
but1.place(x=1,y=50)
but2=tb.Button(b_frame,text="2",bootstyle="light-outline",width=3,command=lambda :disp('2'))
but2.place(x=67,y=50)
but3=tb.Button(b_frame,text="3",bootstyle="light-outline",width=3,command=lambda :disp('3'))
but3.place(x=134,y=50)

but4=tb.Button(b_frame,text="4",bootstyle="light-outline",width=3,command=lambda :disp('4'))
but4.place(x=1,y=100)
but5=tb.Button(b_frame,text="5",bootstyle="light-outline",width=3,command=lambda :disp('5'))
but5.place(x=67,y=100)
but6=tb.Button(b_frame,text="6",bootstyle="light-outline",width=3,command=lambda :disp('6'))
but6.place(x=134,y=100)

but7=tb.Button(b_frame,text="7",bootstyle="light-outline",width=3,command=lambda :disp('7'))
but7.place(x=1,y=150)
but8=tb.Button(b_frame,text="8",bootstyle="light-outline",width=3,command=lambda :disp('8'))
but8.place(x=67,y=150)
but9=tb.Button(b_frame,text="9",bootstyle="light-outline",width=3,command=lambda :disp('9'))
but9.place(x=134,y=150)

but00=tb.Button(b_frame,text="00",bootstyle="light-outline",width=3,command=lambda :disp("00"))
but00.place(x=1,y=200)
but0=tb.Button(b_frame,text="0",bootstyle="light-outline",width=3,command=lambda :disp('0'))
but0.place(x=67,y=200)
butp=tb.Button(b_frame,text=".",bootstyle="light-outline",width=3,command=lambda :disp("."))
butp.place(x=134,y=200)

b_frame.pack()

#grip for extending the screen
size=tb.Sizegrip(window)
size.pack(anchor="se",fill="both",expand=True)

#closure and creates the window screen with above widgets
window.mainloop()
