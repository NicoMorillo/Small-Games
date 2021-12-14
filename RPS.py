from random import choice
    
def RPS_game():
    player = input("Type your choice: ")
    player = player.lower()

    consol = choice(["scissor", "rock", "paper"])



    if player == "scissor" and consol == "rock":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Consol win with {}".format(consol.upper()))
    elif player == "scissor" and consol == "paper":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Player win with {}".format(player.upper()))

    elif player == consol:
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Draw, try again.")

    elif player == "rock" and consol == "paper":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Consol win with {}".format(consol.upper()))
    elif player == "rock" and consol == "scissor":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Player win with {}".format(player.upper()))


    elif player == "paper" and consol == "rock":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Player win with {}".format(player.upper()))
    elif player == "paper" and consol == "scissor":
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))
        print("Consol win with {}".format(consol.upper()))
        print("You pick {} and the consol pick {}".format(player.upper(), consol.upper()))


RPS_game()