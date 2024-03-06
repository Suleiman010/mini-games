
from player import player
import random
import time

def player_info():
    name = input("What is your name")
    return name

pl = player(player_info, 0)

def rps_logic(palyer_choice, cpu):
     rps = {1: "rock", 2:"paper", 3:"scissors"}
     if rps[palyer_choice] == rps[cpu]:
        return "draw"
     elif (palyer_choice == 1 and cpu == 3 ) or (palyer_choice==2 and cpu == 1) or (palyer_choice == 3 and cpu ==2):
        return "win"
     else:
        return "lose"


def rps_game():
    rps = {1: "rock", 2:"paper", 3:"scissors"}
    cpu = random.randint(1,3)
    player_choice = int(input("choose a number between 1-3  \n 1: rock , 2: paper, 3: scissors"))
    while player_choice < 1 or player_choice > 3:
            player_choice = int(input("choose a number between 1-3  \n 1: rock , 2: paper, 3: scissors"))
    time.sleep(1)
    print("Player: "+ rps[player_choice])
    time.sleep(2)
    print("CPU: "+ rps[cpu]+"\n")
    if rps_logic(player_choice,cpu) == "win":
        print("You won")
        return pl.score+10
    elif rps_logic(player_choice,cpu) == "lose":
        print("you lost")
        choise = lose_draw()
        if choise ==1:
            rps_game()
        else:
            print ("game over")
            return "game over"
    else:
        print("its a draw")
        rps_game()



def lose_draw():
    choise=int(input("try agian = 1 \nquit = 0\n"))
    while(choise<0 or choise >1):
        choise=int(input("try agian = 1 \nquit = 0\n"))
    return choise
    



def coin_flip():
    coin = {1: "head", 2: "tail"}
    choice = int(input("1 : head \n 2: tail \n"))
    coin_state = random.randint(1,2)
    
    while choice > 2 or choice < 1:
        print("You can only choose on of these two states")
        choice = int(input("1 : head \n 2: tail \n"))

    if choice == coin_state :
        print("You won ")
        return pl.score +10
    else:
        print("wrong")
        end_choice = lose_draw()
        if end_choice == 1:
            coin_flip()
        return "gg"

def guessing_game():
    ran_num = random.randint(1,10)
    choice = int(input("please enter your guess the number is between 1,10"))
    while choice >10 | choice < 1:
            choice = int(input("please enter your guess the number is between 1,10"))
    if choice == ran_num:
        print("your guess is correct")
        return pl.score +20
    
    else:
        end_choice = lose_draw()
        if end_choice == 1:
            guessing_game()
    
        else:   
            print("gg") 
            return pl.score 

guessing_game()    