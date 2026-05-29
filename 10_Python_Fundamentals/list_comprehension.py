# List Comprehension = A way to create lists in python.
#                      Compact and easier to read than traditional
#                      [expression for value in iterable if condition]

doubles=[]

for x in range(1,11):
    doubles.append(x*2)

print(doubles)
doubles=doubles.clear()
print(doubles)

doubles=[x*2 for x in range(1,11)]

print(doubles)

triples=[y*3 for y in range(1,11)]

print(triples)

squares=[z*z for z in range(1,11)]

print(squares)

fruits=["apple","banana","orange","mango"]

fruits=[fruit.capitalize() for fruit in fruits]
print(fruits)

fruit_char=[fruit[0] for fruit in fruits]
print(fruit_char)

numbers=[-1,-2,3,-5,12,-6,4]

only_positive_numbers=[num for num in numbers if num>=0]
print(only_positive_numbers)

only_negative_numbers=[num for num in numbers if num<0]
print(only_negative_numbers)

even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)

odd_numbers=[num for num in numbers if not num%2==0]
print(odd_numbers)

positive_numbers=[abs(x) for x in numbers]
print(positive_numbers)

grades=[85,42,79,90,56,61,30]

passing_grades=[x for x in grades if x>=60]
print(passing_grades)