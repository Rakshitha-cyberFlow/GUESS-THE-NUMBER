##GUESS THE NUMBER PROGRAM

import random
secret_number=random.randint(1,10)
for i in range(6):
    user_guess=int(input("Guess the number: "))
    if(secret_number>user_guess):
        print("The guess is LOW")
    elif(secret_number<user_guess):
        print("The guess is HIGH")
    else:
        print("CONGRATS!!....The guess is CORRECT")
        break
if(user_guess!=secret_number):
    print("The SECRET NUMBER is: ",secret_number)
    print("Better LUCK next time!!!!.....TRY AGAIN")
