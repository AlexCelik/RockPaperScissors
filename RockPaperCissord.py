from random import randint

Game = ["Rock", "Paper", "Scissors"]

Npc = Game[randint(0, 2)]

Player = False
print("Welcome to Rock Paper Scissors Game !!")
print("If you want to exit, just type 'exit' ")


while Player == False:
    Player = input().capitalize()
    if Player == Npc:
        print("Equal")

    elif Player == "Rock":
        if Npc == "Paper":
            print("you lost by the paper")
        elif Npc == "Scissors":
            print("you won, you smashed the scissors with the rock")

    elif Player == "Paper":
        if Npc == "Rock":
            print("you won by wrapping the rock with the paper")
        elif Npc == "Scissors":
            print("you lost and get cut")

    elif Player == "Scissors":
        if Npc == "Rock":
            print("you lost by the rock")
        elif Npc == "Paper":
            print("you won ")
    elif Player == "exit":
        break
    Player = False
    Npc = Game[randint(0,2)]
