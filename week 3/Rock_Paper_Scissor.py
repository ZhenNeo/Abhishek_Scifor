import random 

def RPS():
    data = ['Rock', 'Paper', 'Scissor']
    computer = random.choice(data)
    player = False

    while player == False:
        player = input("\n Rock, Paper, Scissors?: ")
        
        if player == computer:
            print("Tie")
        elif player == "Rock":
            if computer == "Paper":
                print("you lose", computer, "beats", player)
            else:
                print("you win", player, "beats", computer)
        elif player == "Paper":
            if computer == "Scissor":
                print("you lose", computer, "beats", player)
            else:
                print("you win", player, "beats", computer)
        elif player == "Scissor":
            if computer == "Rock":
                print("you lose", computer, "beats", player)
            else:
                print("you win", player, "beats", computer)
        else:
            print("Invalid input")
            break
        player = False
        computer = random.choice(data)

RPS()