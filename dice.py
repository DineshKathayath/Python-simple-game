import random
import time

player1 = 0
player2 = 0

rounds_to_play = 5

for round_number in range(1, rounds_to_play, 1):
    print("Round", round_number, "is about to start!")
    time.sleep(2)
    roll = input("player 1, are you ready to throw your dice? (y/n)" )
    if roll == "y":
        print("Rolling the dice...")
        time.sleep(.5)
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)
        
        print("You rolled:")
        print(dice1, dice2, dice3, dice4)
        time.sleep(1)
        
        if (dice1 == dice2 or dice1 == 3 or dice1 == 4 or dice2 == 3 or dice2 == dice4 or dice3 == dice4):
            print("well done you roled a pair(1p)")
            player1 = player1 + 1
            print("player1", player1)
        elif(dice1 == dice2 == dice3 == dice4):
            print("Nice! you hit a three of a kind! (5p)")
            player1 = player1+5
            print("player1", player1)
        else:
            print("oops! you missed!")
            roll = 0
    else:
            print("Great!")
            time.sleep(5)
            
            roll = input("player 2, are you ready to throw your dice? (y/n)" )
    if roll == "y":
        while (roll =="y"):
            print("Rolling the dice...")
            time.sleep(4)
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)
        
        print("You rolled:")
        print(dice1, dice2, dice3, dice4)
        time.sleep(1)
        
        if (dice1 == dice2 or dice1 == 3 or dice1 == 4 or dice2 == 3 or dice2 == dice4 or dice3 == dice4):
            print("well done you roled a pair(1p)")
            player2 = player2 + 1
            print("player2", player2)
        elif(dice1 == dice2 == dice3 == dice4):
            print("Nice! you hit a three of a kind! (5p)")
            player2 = player2 + 5
            print("plyaer2", player2)
        else:
            print("oops! you missed!")
            roll = 0
    else:
            print("Great!")
            time.sleep(3)

print("calculating the dice winner is....")
time.sleep(3)
if(player1 > player2):
    print("player1 is the winner!")
elif(player2 > player1):
    print("player2 is the winner!")
else:
    print("Its an draw!")
            
            
            