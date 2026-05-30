# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance}")

def deposit():
    amount=float(input("Enter amount you want to deposit : "))
    if amount<0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount you want to withdraw : "))
    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount<0:
        print("That's not a valid amount")
        return 0
    else:
        return amount


def main():
    balance=0.0
    is_running=True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        choice=input("Enter your choice (1-4) : ")
        if choice=="1":
            print("*********************")
            show_balance(balance)
        elif choice=="2":
            print("*********************")
            balance+=deposit()
        elif choice=="3":
            print("*********************")
            balance-=withdraw(balance)
        elif choice=="4":
            print("*********************")
            print("Thank you for banking with us!!")
            is_running=False
            print("*********************")
        else:
            print("*********************")
            print("Please enter a valid choice")

if __name__=="__main__":
    main()