import random 
options = ["Rock","Paper","Scissor"] 
machine = random.choice(options)  
user = False    
machine_score = 0
user_score = 0

while True:
    user = input("Rock,Paper,Scissor?").capitalize()   
    if (user == machine):
        print("tie")  
    elif(user == "Rock"): 
        if(machine == "Paper"):
            print("You lose!", machine, "covers", user)
            machine_score+=1
        else:
            print("You win", user, "smashes", machine)
            user_score+=1
    elif(user == "Paper"):
        if(machine == "Scissors"):
            print("you lose", machine, "cut", user)
            machine_score+=1
        else:
            print("You win", user, "cover", machine)
            user_score+=1
    elif(user == "Scissor"):
        if(machine == "Rock"):
            print("You lose...", machine, "smashes", user)
            machine_score+=1
        else:
            print("You win!", user, "cut", machine)
            user_score+=1
    elif (user == "End"):
        print("Final scores: ")
        print(f"computer's score is:{machine_score}")
        print(f"Your score is: {user_score}")
        break