from tkinter import *
from math import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import Image,ImageTk
import string
import random
import tkinter.messagebox as ms

#assign methods of ttkbootstrap to a variable or object
window=tb.Window(title="Rock-Paper-Scissor Game",themename="superhero")
window.geometry("350x400")

#icon for the window
window.iconbitmap("c:/Users/admin/Desktop/codsoft/task4/logo.ico")

#opening and resizing the images used in the project
img=Image.open("c:/Users/admin/Desktop/codsoft/task4/pic.png")
img=img.resize((250,250),Image.LANCZOS)
img=ImageTk.PhotoImage(img)

start=(Image.open("c:/Users/admin/Desktop/codsoft/task4/start.png")).resize((50,50),Image.LANCZOS)
start=ImageTk.PhotoImage(start)

roc=(Image.open("c:/Users/admin/Desktop/codsoft/task4/rock.png")).resize((80,100),Image.LANCZOS)
roc=ImageTk.PhotoImage(roc)

pap=(Image.open("c:/Users/admin/Desktop/codsoft/task4/paper.png")).resize((80,100),Image.LANCZOS)
pap=ImageTk.PhotoImage(pap)

scs=(Image.open("c:/Users/admin/Desktop/codsoft/task4/scissor.png")).resize((80,100),Image.LANCZOS)
scs=ImageTk.PhotoImage(scs)

lsr=(Image.open("c:/Users/admin/Desktop/codsoft/task4/loser.png")).resize((80,100),Image.LANCZOS)
lsr=ImageTk.PhotoImage(lsr)

wn=(Image.open("c:/Users/admin/Desktop/codsoft/task4/winner.png")).resize((80,100),Image.LANCZOS)
wn=ImageTk.PhotoImage(wn)


#variable which stores the scores of the user and computer
score_u=0
score_c=0

#on triggred the function calls the onclick function
def try_on():
    onclick()

# on triggered the function ends the game an displays results and scores of each party
def exit_on():
    for widgets in frame.winfo_children():
        widgets.destroy()

    global res
    #displays following if users wins
    if(score_u>score_c):
        win=tb.Label(frame,image=wn)
        win.place(x=120,y=50)
        res=tb.Label(frame,text=f"Congratulations! you won!",font=("roboto",14,"bold"),bootstyle="primary")
        res.place(x=10,y=150)

    #displays following if its a tie
    elif(score_u==score_c):
        res=tb.Label(frame,text=f"it's Tie! close game",font=("roboto",14,"bold"),bootstyle="primary")
        res.place(x=10,y=150)

    #displays following if computer wins
    else:
        lose=tb.Label(frame,image=lsr)
        lose.place(x=120,y=50)
        res=tb.Label(frame,text=f"you lose! better luck next time.",font=("roboto",14,"bold"),bootstyle="primary")
        res.place(x=10,y=150)

    u_score=tb.Label(frame,text=f"your Score: {score_u}",font=("roboto",14,"bold"),bootstyle="success")
    u_score.place(x=30,y=200)
    c_score=tb.Label(frame,text=f"computer Score: {score_c}",font=("roboto",14,"bold"),bootstyle="danger")
    c_score.place(x=30,y=230)


#the function evaluates the choice made by user with random choice of computer 
def play(x):
    for widgets in frame.winfo_children():
        widgets.destroy()

    global score_u,score_c,lab,lose,win,try_again,exit

    ch=["rock","scissors","paper"]
    ran_choice=random.choice(ch)

    if(x==ran_choice):
        lab=tb.Label(frame,text=f'\nits a tie! \nbetween your {x} and {ran_choice}',font=("roboto",15,"bold"),bootstyle="primary")
        lab.place(x=15,y=120)

    elif(x=="rock" and ran_choice=="scissors")or(x=="paper" and ran_choice=="rock")or(x=="scissors" and ran_choice=="paper"):
        score_u=score_u+1
        win=tb.Label(frame,image=wn)
        win.place(x=120,y=50)
        lab=tb.Label(frame,text=f'\tyou win!\nyour {x} beats {ran_choice}',font=("roboto",15,"bold"),bootstyle="primary")
        lab.place(x=30,y=150)
        


    elif((x=="rock" and ran_choice=="paper") or (x=="paper" and ran_choice=="scissors") or (x=="scissors" and ran_choice=="rock")):
        score_c=score_c+1
        lose=tb.Label(frame,image=lsr)
        lose.place(x=120,y=50)
        lab=tb.Label(frame,text=f'\tyou lose!\nyour {x} beaten by {ran_choice}',font=("roboto",15,"bold"),bootstyle="primary")
        lab.place(x=30,y=150)
        

    try_again=tb.Button(frame,text="Try Again!",bootstyle="success-outline",width=10,command=try_on)
    try_again.place(x=20,y=250)

    exit=tb.Button(frame,text="Exit",bootstyle="danger-outline",width=10,command=exit_on)
    exit.place(x=230,y=250)



#the function conatins interactive rockpaperscissor game gui and asks player to make choices
def onclick():
    for widgets in frame.winfo_children():
        widgets.destroy()
    global u_score,c_score,rock,paper,scissor,choice,score_u,score_c
    u_score=tb.Label(frame,text=f"your Score: {score_u}",font=("roboto",10,"bold"),bootstyle="success")
    u_score.place(x=1,y=5)
    c_score=tb.Label(frame,text=f"computer Score: {score_c}",font=("roboto",10,"bold"),bootstyle="danger")
    c_score.place(x=220,y=5)
    choice=tb.Label(frame,text="Make your Move!",bootstyle="info",font=("roboto",15,"bold"))
    choice.place(x=100,y=120)
    rock=tb.Button(frame,image=roc,bootstyle="dark-outline",command=lambda m="rock":play(m))
    rock.place(x=4,y=200)
    paper=tb.Button(frame,image=pap,bootstyle="dark-outline",command=lambda m="paper":play(m))
    paper.place(x=120,y=200)
    scissor=tb.Button(frame,image=scs,bootstyle="dark-outline",command=lambda m="scissors":play(m))
    scissor.place(x=220,y=200)



#intial frame or interface viewed by user
frame=tb.Frame(window,width=340,height=380)
l1=tb.Label(frame,image=img)
l1.place(x=50,y=30)
b1=tb.Button(frame,image=start,bootstyle="success-outline",command=onclick)
b1.place(x=140,y=300)
frame.pack()


window.mainloop()