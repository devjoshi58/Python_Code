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

    feedback = ' '
    #computer_number = 0
    high =x
    low =1 

    while feedback != 'c':
        
        if low!=high:
            computer_number = random.randint(low,high) # randint gives error when low and high are same
        else:
            computer_number = high # could be low as well as high = low
        
        print(f"{computer_number}")
        feedback = input(f"if the number is high then (h) or if the number is low then (l) or if the guess is correct then c :: ").lower()
        
        if feedback == 'l':
            low+=1
        elif feedback == 'h':
            high-=1

        
    print(f"Computer guessed it right")

computer_guess(100)

