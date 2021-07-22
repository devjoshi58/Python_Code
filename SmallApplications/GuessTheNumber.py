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

#guess(10)

def computer_guess(x):

    user_number = x
    computer_number = 0
    high =x
    low =1 

    while user_number != computer_number:
        print(f"{computer_number} is Wrong choice, guess again")
        computer_number = random.randint(low,high)

        if computer_number > user_number:
            print(f"{computer_number} too high")
            high = computer_number-1
        
        elif computer_number < user_number:
            print(f"{computer_number} too low")
            low = computer_number+1
        
    
    print(f"Computer guessed it right, the number is {computer_number}")

computer_guess(7)

