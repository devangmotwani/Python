#Implementation of while loops and import in python

import random
highest_rm_number=10
answer= random.randint(1,highest_rm_number)
guess=0
print("Guess a number between 1 and {}. Enter 0 to terminate: ".format(highest_rm_number))
guess = int(input())
while guess !=answer:
    if guess==0:
        print("Terminated by user input")
        break
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess==answer:
        print("Guessed it right!!")
        break
    else:
        print("Not guessed correctly!!")
else:
    print("Got it the first time!")