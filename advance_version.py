# snake water gun game

import random

def chack_winner(user,computer):
    if user == computer:
        return "draw"
    
    elif(
        (user == "s" and computer == "w")or
        (user == "w" and computer == "g")or
        (user == "g" and computer == "s")
         ):
    
        return "user"

    else:
        return "computer" 

print ("Snake Water Gun game:")
print("choose:\n s for snake,\n w for water, \n g for gun")

rounds = int(input("Enter the round you want to play:"))
user_score = 0
computer_score = 0

for i in range(rounds):
    print("round:",i+1)
    user = input("Enter your choice:")
    if (user != "s" and user != "w" and user != "g"):
        print("Invalid choice. Try again:")
        continue
    computer = random.choice(["s","w","g"])   
    print("computer choose:",computer)

    result = chack_winner(user,computer)

    if result == "draw":
        print("The Round is draw")
    elif result == "user":
        print("you win the Round")
        user_score += 1
    else:
        print("you loss the Round")
        computer_score += 1
    
print("final score")
print("your score:",user_score)
print("computer score:",computer_score)

if (user_score > computer_score):
    print("congratulation:you won the game")
elif (computer_score > user_score):
    print("soory you loose the game")
else:
    print("game draw")

print("thanks for play the game")
    