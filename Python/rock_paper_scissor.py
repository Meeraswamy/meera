#This is sample program

import random
print("WELCOME TO ROCK - PAPER - SCISSORS GAME\n")
choices=["Rock","Paper","Scissors"]
while True:
    try:
        print("Available Choices :\n 1 Rock\n 2 Paper\n 3 Scissors\n Enter number of your choice")
        choice=choices[int(input("Enter choice here : "))]
    except ValueError:
        print("please choose numbers between 1-3 choice")
        continue
    sys_choice=random.choice(["Rock","Paper","Scissors"])
    if choice==sys_choice :
        print("Game Tied\n")
    if choice == "Rock" and sys_choice == "Paper" :
        print("You Lost!! Better Luck Next Time.")
    if choice == "Rock" and sys_hoice == "Scissors" :
        print("You Won!!!!")
    if choice == "Paper" and sys_choice == "Scissors" :
        print("You Lost!! Better Luck Next Time.")
    if choice == "Paper" and sys_choice == "Rock" :
        print("You Won!!!!")
    if choice == "Scissors" and sys_choice == "Paper" :
        print("You Won!!!!")
    if choice == "Scissors" and sys_choice == "Rock" :
        print("You Lost!! Better Luck Next Time.")

    end=input("Enter q to quit or r to replay : ")
    if end == "r" :
        continue
    else :
        break
    
