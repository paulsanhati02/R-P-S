from tkinter import *
from PIL import ImageTk ,Image
from random import randint

root=Tk()
root.title("ROCK SCISSOR PAPER")
root.config(background="#FF7F50")

Image_icon=ImageTk.PhotoImage(file="R-P-S LOGO (2).png")
root.iconphoto(False,Image_icon)

rock_img=ImageTk.PhotoImage(Image.open("user Rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("user Paper (2).png"))
scissor_img=ImageTk.PhotoImage(Image.open("user sessior.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("comp rock.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("comp paper (4).png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("comp sessior.png"))

user_label=Label(root,image=scissor_img,bg="#9b59b6")
comp_label=Label(root,image=scissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0,padx=20,pady=10)
user_label.grid(row=1,column=4,padx=20,pady=10)

computer_score=Label(root,text=0,font=('arial',50,"bold"),fg="blue")
player_score=Label(root,text=0,font=('arial',50,"bold"),fg="blue")
computer_score.grid(row=1,column=1,padx=20,pady=10)
player_score.grid(row=1,column=3,padx=20,pady=10)

player_imdicator=Label(root,font=("arial",20,"bold"),text="USER",bg="white",fg="black")
computer_imdicator=Label(root,font=("arial",20,"bold"),text="COMPUTER",bg="white",fg="black")
computer_imdicator.grid(row=0,column=1)
player_imdicator.grid(row=0,column=3)

msg=Label(root,font=50,bg="#9b59b6",fg="white",text="You Loose")
msg.grid(row=1,column=2)

def updateMessage(a):
    msg['text']=a

def updateUserScore():
    score=int(player_score["text"])
    score+=1
    player_score["text"]=str(score)

def updateCompScore():
    score=int(computer_score["text"])
    score+=1
    computer_score["text"]=str(score)
    
def winner_check(p,c):
    if p == c:
        updateMessage("It's a tie",)
    elif p=="rock":
        if c == "paper":
            updateMessage("Computer Wins!!")
            updateCompScore()
        else:
            updateMessage("User Wins!!")
            updateUserScore()
        
    elif p=="paper":
        if c == "scissor":
            updateMessage("Computer Wins!!")
            updateCompScore()
        else:
            updateMessage("User Wins!!")
            updateUserScore()
    
    elif p=="scissor":
        if c == "rock":
            updateMessage("Computer Wins!!")
            updateCompScore()
        else:
            updateMessage("User Wins!!")
            updateUserScore()
    else:
        pass

choices=["rock","paper","scissor"]

def choice_update(a): 
    
    if a == "playagain":
        player_score["text"] = "0"
        computer_score["text"] = "0"
        updateMessage("Let's play again!")
        user_label.configure(image=scissor_img)
        comp_label.configure(image=scissor_img_comp)
        return
    
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    if a=="rock":
        user_label.configure(image=rock_img)
    elif a=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
        
    winner_check(a,compChoice)


rock=Button(root,width=32,height=2,text="ROCK",bg="#FF3E4D",fg="White",command=lambda:choice_update("rock")).grid(row=2,column=1)
paper=Button(root,width=30,height=2,text="PAPER",bg="#FF3E4D",fg="white",command=lambda:choice_update("paper")).grid(row=2,column=2)
scissor=Button(root,width=30,height=2,text="SCISSOR",bg="#FF3E4D",fg="white",command=lambda:choice_update("sessior")).grid(row=2,column=3)
PlayAgain=Button(root,width=20,height=2,text="PLAY AGAIN",bg="#FF3E4D",fg="white",command=lambda:choice_update("playagain")).grid(row=10,column=2)


root.mainloop()