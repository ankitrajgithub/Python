# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over a loop.

numbers=[1,2,3,4,5,6,7,8]
nums=(1,2,3,4,5,6,7,8)
fruits={"Apple","Orange","Banana","Strawberry"}

for num in numbers:
    print(num,end=" ")
print()

for num in reversed(numbers):
    print(num,end=" ")
print()

for num in nums:
    print(num,end=" ")
print()

for fruit in fruits:
    print(fruit,end=" ")
print()

name="Ankit Raj"

for char in name:
    print(char,end=" ")
print()

my_dict={"A":1,"B":2,"C":3,"D":4,"E":5}

for key,value in my_dict.items():  # my_dict.keys() my_dict.values() my_dict.items()
    print(key,"->",value,end=" I ")