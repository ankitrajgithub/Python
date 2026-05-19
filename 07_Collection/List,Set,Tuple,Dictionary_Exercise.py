# Collection = Single "variable" used to store multiple values
# List = [] Ordered and changeable. Duplicates OK
# Set = {} Unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () Ordered and unchangeable. Duplicates OK. Faster

#Shopping Cart Program

foods=[]
prices=[]
total=0

while True:
    food=input("Enter food you want to add (q to quit) : ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter price of {food} : $"))
        foods.append(food)
        prices.append(price)

print("--------COSTCO--------")
print("--------Bill--------")

total=0

for x in range(0,len(foods)):
    print(foods[x],"->",prices[x])
    total+=prices[x]

print(f"Your total is : {total}")

#Quiz Game

questions=("How many elements are in the periodic table?",
           "Which animal lays largest eggs?",
           "What is the most abundant gas in Earth's atmosphere?",
           "How many bones are in the human body?",
           "Which planet in the solar system is the hottest?")

options=(("A. 116","B. 117","C. 118","D. 119"),
         ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
         ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
         ("A. 206","B. 207","C. 208","D. 209"),
         ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers=("C","D","A","A","B")

guesses=[]

score=0

question_num=0

for question in questions:
    print(f"--------QUESTION {question_num+1}--------")
    print(f"Question: {question}")
    for option in options[question_num]:
        print(f"{option}",end=" ")
    print()
    guess=input("Enter your guess (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print(f"Correct!")
    else:
        print(f"Incorrect. Try again.!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers :",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses :",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f"Your final score is {score}%")

#Concession Stand Program

print("----------- MENU -----------")
menu={"Pizza":3.00,
      "Nachos":4.50,
      "Popcorn":6.00,
      "Fries":2.50,
      "Chips":1.00,
      "Pretzel":3.50,
      "Soda":3.00,
      "Lemonade":4.25}
cart=[]
total=0

for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")

while True:
    food=input("What would you like to order (q to quit) : ")
    if food.lower()=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food} added to cart!")
    else:
        print("Item doesn't exist!")

print("----------BILL----------")
for food in cart:
    total=total+menu.get(food)
    print(food,"->",menu.get(food),end=" ┃ ")

print()
print(f"Total cost is ${total:.2f}")