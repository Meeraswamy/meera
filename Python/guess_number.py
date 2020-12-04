# Guessing number program

import random

while True:
    choice=int(input("Enter Your Choice : "))
    if choice > 50 :
        print("Please chosse number below 50")
        continue
    sys_choice=random.randrange(1,50)
    if sys_choice == choice :
        print("Congratulation Your Guess is correct!!!!")
        
    else : print("Oops Your Guess is wrong!!!")
    end=input("Enter q to quit or r to replay : ")
    if end == "q" : break
    if end == "r" : continue
