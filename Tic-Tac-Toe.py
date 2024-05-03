from tkinter import *
import random
import row
def pc():
    rx_score.config(text="Pc: "+str(score_x))
    ry_score.config(text="player1 : "+str(score_y))

def bot():
    pass


def updT():
    rx_score.config(text="player X: "+str(score_x))
    ry_score.config(text="player Y: "+str(score_y))

def next(row,col):
    global   player
    global  score_x
    global  score_y
    if btns[row][col]['text'] == "" and win()== False:
        if player == players[0]:
            btns[row][col]['text'] = player

            if win()==False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif win()== True:
                score_x=score_x+1
                label.config(text=(players[0]+" Wins!"))
                updT()


            elif win()== 'tie':
                label.config(text=("Tie! No Winners"),font=("consolas", 18))
        elif player == players[1] :

            btns[row][col]['text'] = player

            if win()==False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            elif win()== True:
                score_y=score_y+1
                label.config(text=(players[1]+" Wins!"))
                updT()

            elif win()== 'tie':
                label.config(text=(" Tie! No Winners"))


def new_game():
    global score_x, score_y
    player= random.choice(players)
    for row in range(0,3):
        for col in range(0,3):
            btns[row][col].config(text=(""),bg="#F0F0F0")
    score_x=0
    score_y=0
    updT()
    label.config(text=player +" turn")

def win():
    for row in range(0,3):
     if btns[row][0]['text']==btns[row][1]['text'] == btns[row][2]['text'] !="":
         btns[row][0].config(bg="cyan")
         btns[row][1].config(bg="cyan")
         btns[row][2].config(bg="cyan")
         return True
     for col in range(0,3):
      if btns[0][col]['text']==btns[1][col]['text'] == btns[2][col]['text'] !="":
          btns[0][col].config(bg="cyan")
          btns[1][col].config(bg="cyan")
          btns[2][col].config(bg="cyan")
          return True
     if btns[0][0]['text']==btns[1][1]['text']==btns[2][2]['text'] !="":
         btns[0][0].config(bg="cyan")
         btns[1][1].config(bg="cyan")
         btns[2][2].config(bg="cyan")
         return True
     elif btns[0][2]['text']==btns[1][1]['text']==btns[2][0]['text'] !="":
         btns[0][2].config(bg="cyan")
         btns[1][1].config(bg="cyan")
         btns[2][0].config(bg="cyan")
         return True
     if is_empty()==False:
         for row in range(3):
             for col in range(3):
              btns[row][col].config(bg='red')
         return 'tie'
    else:
        return False
def continue_game():
 if win()== True or win()== 'tie':

    player= random.choice(players)
    for row in range(0,3):
        for col in range(0,3):
            btns[row][col].config(text=(""),bg="#F0F0F0")
    label.config(text=player +" turn")
 else:
     pass
def is_empty():
   for row in range(0,3):
       for col in range(0,3):
           if btns[row][col]['text']=="":
               return True
   else:
       return False

window = Tk()
window.geometry('700x620')
window.title("Tic Tac Toe !")
window.bg="#F0F0F0"
players = ["X", "O"]
player=random.choice(players)
btns=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
score_x=score_y=0
rx_score=Label(window,text="player X: "+str(score_x),font=("consolas", 15))
rx_score.place(x=5,y=0)
ry_score=Label(window,text="player Y: "+str(score_y),font=("consolas", 15))
ry_score.place(x=5,y=35)
con=Button(window,text="Continue" ,font=("consolas", 15),command=continue_game)
con.place(x=200,y=68)
label = Label (text=(player + " turn") , font=("consolas", 40))
label.pack(side="top")
restart = Button(window, text="Restart",font=("consolas",15), command=new_game)
Bot = Button(window, text="Bot",font=("consolas",15), command=bot)
Bot.place(x=420,y=68)
restart.place(x=315,y=68)
btns_frame = Frame(window)
btns_frame.place(x=0, y=120)
for row in range(0,3):
    for col in range(0,3):
        btns[row][col]=Button(btns_frame,text="",font=("consolas",40),width=8,height=2,
                     command=lambda row = row , col= col :next(row,col))
        btns[row][col].grid(row=row,column=col)
#score=Label(window,text="Score ",font=("consolas", 20))
#score.place(x=10,y=10)
window.mainloop()



