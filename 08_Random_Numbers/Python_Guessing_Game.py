#Python Number Guessing Game
import random

highest=100
lowest=0
guesses=0
no=random.randint(lowest,highest)


print("Python Number Guessing Game")
print(f"Select a number between {lowest} and {highest}")
while True:
    guess=input(f"Enter your guess : ")
    if guess.isdigit():
        guess=int(guess)
        if guess>highest or guess<lowest:
            print(f"Your guess should be between {lowest} and {highest}")
            guesses+=1
        elif guess>no:
            print("Your guess is too high")
            guesses+=1
        elif guess<no:
            print("Your guess is too low")
            guesses+=1
        else:
            print(f"Congratulations! Number {guess} was Correct!")
            guesses+=1
            print(f"You took {guesses} chances to guess!")
            break
    else:
        print("Invalid Input")