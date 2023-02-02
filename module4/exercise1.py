# number guessing game 
import random
winning_number = random.randint(0,100)
user_inp=int(input("enter any number between 0 to 100 "))
if user_inp==winning_number :
    print("hey you're the winnner")
else :
    if user_inp>winning_number :
        print("too high")
    else:
        print("too low")
