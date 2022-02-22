#snake water gun
#play game 10 times take input count how many times person wins and decide the final winner
import random

choose = ["Snake", "Water", "Gun"]

print("Welcome to the game of snake, water and gun\nChoose any of the following:\n",choose)

# print(computer_choice)
your_score = 0
computer_score= 0
try_number = 0
while (try_number<= 9):
    your_choice = str(input("Enter Your choice: "))
    computer_choice = random.choice(choose)
    if (your_choice == "Snake")&(computer_choice == "Snake"):
        print("Computers choice = ",computer_choice)
        print("Draw this Time:")
        your_score +=1
        computer_score +=1
        try_number +=1
        print("Your", try_number,"Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Snake")&(computer_choice == "Water"):
        print("Computers choice = ",computer_choice)
        print("You Won")
        your_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Snake") & (computer_choice == "Gun"):
        print("Computers choice = ",computer_choice)
        print("You loose")
        computer_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Water") & (computer_choice == "Snake"):
        print("Computers choice = ",computer_choice)
        print("You loose")
        computer_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Water") & (computer_choice == "Water"):
        print("Computers choice = ",computer_choice)
        print("Draw this Time")
        your_score += 1
        computer_score += 1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Water") & (computer_choice == "Gun"):
        print("Computers choice = ",computer_choice)
        print("You Won")
        your_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Gun") & (computer_choice == "Snake"):
        print("Computers choice = ",computer_choice)
        print("You Win")
        your_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Gun") & (computer_choice == "Water"):
        print("Computers choice = ",computer_choice)
        print("You loose")
        computer_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue
    elif (your_choice == "Gun") & (computer_choice == "Gun"):
        print("Computers choice = ",computer_choice)
        print("Draw This Time")
        your_score +=1
        computer_score +=1
        try_number += 1
        print("Your", try_number, "Try")
        print("Your score", your_score, "Computer Score", computer_score)

        continue

print("Your score",your_score,"Computer Score",computer_score)
if your_score > computer_score:
    print("Hurray you win")
elif your_score < computer_score:
    print("Sorry you loose try again")
else:
    print("Draw")
