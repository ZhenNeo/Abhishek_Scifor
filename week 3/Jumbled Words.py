import random

def choose_word():
    data = ["wisdom",'health','hospital','allergy','ambulance']
    return random.choice(data)

def jumble_word(word):
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def play():
    original = choose_word()
    jumbled_word = jumble_word(original)

    print("Welcome to Jumbled Words")
    print("Guess the correct word from the jumbled word")

    while True:
        print(f"Jumbled word : {jumbled_word}")
        user_guess = input("your Guess: ").lower()

        if user_guess == original:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            print("Incorrerct. Try again")

play()
