import random
option = ["Snake","Water", "Gun"]
computer = random.choice(option)
user = False
computer_score = 0
user_score = 0

while True:
    user = input("Snake, water, or gun?").capitalize()
    if(computer == user):
        print("Choice drawn")
    elif(computer == "Snake"):
        if(user == "Water"):
          print("user won")
          user_score+=1
        else:
            print("computer won")
            computer_score+=1
    elif(computer =="snake"):
        if(user == "gun" ):
            print("user won")
            user_score+=1
        else:
             print("computer won")
             computer_score+=1
    elif(computer == "water"):
        if(user == "snake"):
            print("computer won")
            computer_score+=1
        else:
            print("user won ")
            user_score+=1
    elif(computer == "water"):
        if(user == "gun"):
            print("user won")
            user_score+=1
        else:
             print("computer won")
             computer_score+=1
    elif(computer == "gun"):
        if(user == "snake"):
            print("computer won")
            computer_score+=1
        else:
            print("user won")
            user_score+=1
    elif(computer == "gun"):
        if(user == "water"):
            print("user won")
            user_score+=1
        else:
             print("computer won")
             computer_score+=1
    elif(user == "end"):
        print("the final score is: " )
        print(f"computer's final score s {computer_score}")
        print(f"The user's final scoe is {user_score}")
        break
                