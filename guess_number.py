import random

User_number=input("Enter a number: ")

if User_number.isdigit():
    User_number=int(User_number)

    if User_number <= 0:
       print("PLease give us a number greater than zero")
       quit()
else:
    print("please type a number next time")
    quit()

random_number=random.randint(0,User_number)
gussess=0

while True:
    gussess+=1
    user_guess=input("Guess the number: ")
    if user_guess.isdigit():
         user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    if user_guess==random_number:
             print("your guess is right")
             break
    elif user_guess > random_number:
            print("you were above the number")
    else:
            print("you were below the number")

print("the total guesses you made are {}".format(gussess))





