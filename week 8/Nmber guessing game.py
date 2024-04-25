import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.num_guesses = 0
    
    def play_game(self):
        print("Welcome to the Number Guessing Game!")
        print("I have chosen a number between 1 and 100. Try to guess it!")
        
        while True:
            guess = int(input("Enter your guess: "))
            self.num_guesses += 1
            
            if guess < self.target_number:
                print("Too low! Try again.")
            elif guess > self.target_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number in", self.num_guesses, "guesses.")
                break


game = NumberGuessingGame()
game.play_game()
