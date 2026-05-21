# function = A block of reusable code. Place () after a function name to invoke it.

def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Ankit",22)
happy_birthday("Kashish",20)
happy_birthday("Anuj",14)
happy_birthday("Mehul",10)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

display_invoice("Ankit Raj",45.50,"01-01-2027")

# return = statement used to end a function and send a result back to the caller

def sum(a,b):
    z=a+b
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(a,b):
    z=a/b
    return z

print(sum(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=create_name("ankit","raj")
print(full_name)