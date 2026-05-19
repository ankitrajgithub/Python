#Rock, Paper, Scissor
import random

options=("Rock","Paper","Scissor")
playing=True

#while True:
#    player = input("Enter a choice (Rock, Paper, Scissor) : ")
#    if options.__contains__(player):
#        break
#    else:
#        print("Invalid Input")

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissor) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player==computer:
        print("It's a tie")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose")
        else:
            print("You win")
    elif player=="Paper":
        if computer=="Scissor":
            print("You lose")
        else:
            print("You win")
    else:
        if computer=="Rock":
            print("You lose")
        else:
            print("You win")
#   play_again=input("Do you want to play again? (y/n) : ").lower()
    if not input("Do you want to play again? (y/n) : ").lower() =="y":
        playing=False

print("Thanks for playing!!")