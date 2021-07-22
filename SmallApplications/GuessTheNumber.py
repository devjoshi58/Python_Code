#Guess the number

import random

def guess(x):

    rand_number = random.randint(1,x)
    user_number = 0

    while user_number!= rand_number:
        user_number = int(input("Please guess the number: "))

        if user_number>rand_number:
            print("Your number is higher than the correct numbber")
        
        elif user_number<rand_number:
            print("Your number is lower than the correct number")
    
    print(f"Congrats you got the number right, which is {user_number}")

guess(10)