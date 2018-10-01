from random import randint

Game = ["Rock", "Paper", "Scissors"]

computer = Game[randint(0, 2)]

Player = False

while Player == False:
    Player = input()
    if Player == computer:
        print("Equal")

    elif Player == "Rock":
        if computer == "Paper":
            print("you lost by the paper")
        elif computer == "Scissors":
            print("you won, you smashed the scissors with the rock")

    elif Player == "Paper":
        if computer == "Rock":
            print("you won by wrapping the rock with the paper")
        elif computer == "Scissors":
            print("you lost and get cut")

    elif Player == "Scissors":
        if computer == "Rock":
            print("you lost by the rock")
        elif computer == "Paper":
            print("you won ")
    Player = False
    computer = Game[randint(0,2)]
