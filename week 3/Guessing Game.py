import random

def choose_number():
    return random.randint(1,20)


def get_user_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def guess():
    chance = 10
    comp = choose_number()
    print("Guess the correct number between 1 - 20. \nYou have 10 chances to guess the correct answer")
    while chance > 0:
        user_input = get_user_guess()
        if user_input == comp:
            print("You Won")
            break
        chance -= 1
    if chance == 0:
        print("You lose")
        print("The correct answer was " + str(comp))
    
guess()