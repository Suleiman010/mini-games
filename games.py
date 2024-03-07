
from player import player
import random
import time

def player_info():
    name = input("What is your name")
    return name

pl = player(player_info, 0)

def difficulty():
    dif = int(input("Easy: 1\nnormal: 2\nhard: 3\n "))
    
    while dif > 3 or dif < 1:
            dif = int(input("Easy: 1\nnormal: 2\nhard: 3\n "))
    if dif == 1 :
         return 5
    elif dif ==2:
         return 3
    else:
         return 1        
    

def choice_checker(mini, maxi, choice, massage):
     while choice < mini or choice > maxi:
        choice =int(input(massage)) 


def rps_game(diff):
    rps = {1: "rock", 2:"paper", 3:"scissors"}
    cpu = random.randint(1,3)
    player_choice = int(input("choose a number between 1-3  \n 1: rock  2: paper 3: scissors\n chances left " + str(diff)))
    score = 15/diff
    
    choice_checker(1,3,player_choice,"choose a number between 1-3  \n 1: rock  2: paper 3: scissors\n")
    
    while diff != 0:
        diff = diff-1
        if (player_choice == 1 and cpu == 3 ) or (player_choice==2 and cpu == 1) or (player_choice == 3 and cpu ==2):
            time.sleep(1)
            print(rps[player_choice]+" X " + rps[cpu]+"\n**********you won**********")
            pl.score += score
            return pl.score
        else:
            if diff ==0:
                 break
            time.sleep(1)
            print(rps[player_choice]+" X " + rps[cpu])
            player_choice = int(input("Trye again\nchoose a number between 1-3  \n 1: rock  2: paper 3: scissors\n chances left "+ str(diff)))
            choice_checker(1,3,player_choice,"choose a number between 1-3  \n 1: rock  2: paper 3: scissors\n")
            cpu = random.randint(1,3)

    print("You lost")       
    return pl.score




def coin_flip(diff):
    coin = {1: "head", 2: "tail"}
    choice = int(input("1 : head \n 2: tail \n"))
    coin_state = random.randint(1,2)
    
    choice_checker(1,2,choice,"You can only choose on of these two states\n1 : head \n 2: tail \n")
    score = 30/diff
    while diff != 0:
        diff-=1
        if choice == coin_state:
            pl.score += score
            time.sleep(1)
            print(coin[coin_state]+ " X "+ coin[choice] + "\n**********you won**********")
            return pl.score
        else:
            time.sleep(1)
            choice = int(input(str(coin[coin_state])+ " X "+ str(coin[choice]) +"\nTry again \n1 : head \n 2: tail \n"))
            choice_checker(1,2,choice,"You can only choose on of these two states\n1 : head \n 2: tail \n")
            coin_state = random.randint(1,2)

    return pl.score        
         

def guessing_game(diff):
    ran_num = random.randint(1,10)
    choice = int(input("enter your guess the number is between 1,10 \nchances left"+str(diff)))
    choice_checker(1,10,choice,"please enter your guess the number is between 1,10")

    score = 60/diff
    while diff != 0:
        diff -=1 
        if ran_num == choice:
            pl.score += score
            time.sleep(1)
            print("**********you won**********")
            return pl.score
        
        elif ran_num != choice:
            time.sleep(1)
            if diff ==0:
                break
            
            if choice > ran_num:
                choice = int(input("Guess lower " +str(diff)))
                choice_checker(1,10,choice,"please enter your guess the number is between 1,10")
            else:
                choice = int(input("Guess higher "+ str(diff)))
                choice_checker(1,10,choice,"please enter your guess the number is between 1,10")  
    return pl.score            
while True:
    diff = difficulty()
    guessing_game(diff)
