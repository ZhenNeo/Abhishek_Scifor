import time
def Introduction():
    print("Welcome to an Adventure.")
    time.sleep(1)
    print("You have found yourself in a forest.")
    time.sleep(1)
    print("You have to find your way back home.")
    time.sleep(1)

def user_choice(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Please enter a number between 1 and", len(options))
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_adventure():
    Introduction()
    choice = user_choice("The road infront of you splits in two, left and right. which one do you choose?",["go left","go right"])  
    if choice == 1:
        print("You chose to go left. This path leads to a river.")
        time.sleep(1)
        choice = user_choice("The river has no bridge. Do you want to swim accross or head back?", ["swim accross", "Head back"])
        if choice == 1:
            print("You have crossed the River")
            time.sleep(1)

            choice = user_choice("You can see your home. Do you want to go there or head back into the forest to explore?",["Head home","Go back"])
            if choice == 1:
                print("Congratsss!!! you have completed the game")
                time.sleep(1)
            else:
                print("You have chosen to go back to explore the forest. The only path is to go back to the fork of the road and go right")
                time.sleep(1)
        else:
            print("You have went back to the fork of road and have went right. This path goes even deeper into the forest.")
            time.sleep(1)
    elif choice == 2:
        print("You chose to go right. This path goes even deeper into the forest.")      
        time.sleep(1)
        choice = user_choice("You see a wolf. Do you want to fight it or run away?",["Fight","Run"])
        if choice == 1:
            print("You have killed the wolf and now you see your home. You have found your way back. Congratss!!")
        else:
            print("You went around the wolf and found your home. Congratss!!!")
        

forest_adventure()
    
