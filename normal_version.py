# sanke water gun game:

import random

print ("Snake Water Gun game:")
print("choose:\n s for snake,\n w for water,\n g for gun")

user = input("Enter your choice:")


if (user != "s" and user != "w" and user != "g"):
    print("Invalid choice. Try again:")

else:
    computer = random.choice(["s","w","g"])   
    print("computer choose:",computer)

    if (user == computer):
    
        print("Match draw")

    elif(
        (user == "s" and computer == "w")or
        (user == "w" and computer == "g")or
        (user == "g" and computer == "s")
         ):
    
        print("you win")

    else:
        print("you loss")   


print("thankyou")