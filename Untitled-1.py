# import random
# print(random.random()*10)
# print(random.random())
# print (random.randint(0,9))

import random

def number_game():
    
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    number = random.randint(lower, upper)

    print(f"\nA random number between {lower} and {upper} has been generated.")
    print("Try to guess it!")


    while True:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < number:
            print("The number is higher. Try again.")
        else:
            print("The number is lower. Try again.")


number_game()
