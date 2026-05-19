#input() -  A function that prompts the user to enter data.
#           Returns the entered data as a string

name=input("What is your name? : ")
age=int(input("What is your age? : "))

age+=1

print(f"Hello {name}!")
print(f"You are {age} years old!")

#Exercise 1 Rectangle Area Calculation
length=float(input("Enter length of the rectangle(in cm) : "))
width=float(input("Enter width of the rectangle(in cm) : "))

print(f"The length of the rectangle is {length*width} cm²")

#Exercise 2 Shopping Cart Program
item=input("What item would you like to buy? : ")
price=float(input("What is the price? : $"))
quantity=int(input("How many items would you like? : "))

total_price=price*quantity
print(f"The total price of {quantity} {item} is ${total_price}")

#Madlibs game
#Word game where you create a story by filling in blanks with random words
adjective1=input("Enter an adjective (Description) : ")
noun1=input("Enter a noun (Person, Place, Thing) : ")
adjective2=input("Enter an adjective (Description) : ")
verb1=input("Enter a verb ending with 'ing' : ")
adjective3=input("Enter an adjective (Description) : ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")