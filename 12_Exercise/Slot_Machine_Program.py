# Python Slot Machine
import random

def spin_row():
    symbols=["🍒","🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*3
        elif row[0]=="🍉":
            return bet*4
        elif row[0]=="🍋":
            return bet*5
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*20
        else:
            return 0
    else:
        return 0

def main():
    balance=100.0

    print("*************************")
    print(" Welcome to Python Slots ")
    print("Symbols : 🍒 🍉 🍋 ⭐ 🔔")
    print("*************************")

    while balance>0:
        print(f"Current balance : ${balance}")
        bet=input("Enter your bet : $")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet=int(bet)

        if bet>balance:
            print("Insufficient funds")
            continue

        if bet<=0:
            print("Your bet should be greater than 0")
            continue

        balance=balance-bet

        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=get_payout(row,bet)

        if payout>0:
            print(f"You won ${payout}.")
        else:
            print("Sorry! You lost.")
        balance+=payout

        play_again=input("Do you want to play again? (y/n) ").lower()

        if play_again!="y":
            break

    print(f"Game Over! Your final balance : ${balance}")

if __name__ == "__main__":
    main()