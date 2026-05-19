# Collection = Single "variable" used to store multiple values
# List = [] Ordered and changeable. Duplicates OK
# Set = {} Unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () Ordered and unchangeable. Duplicates OK. Faster

fruits=["apple","orange","mango","banana"]

print(fruits)
print(fruits[0])
print(len(fruits))

for fruit in fruits:
    print(f"This fruit is {fruit}")

for x in range(0,len(fruits)):
    print(f"Fruit : {fruits[x]}")

print(fruits[::-1])

print("apple" in fruits)

fruits[0]="pineapple"

fruits.append("apple")

fruits.remove("pineapple")

fruits.insert(0,"pineapple")

fruits.sort()

fruits.reverse()

print(fruits.index("apple"))

print(fruits.count("banana"))

fruits.clear()

for x in range(0,len(fruits)):
    print(f"Fruit : {fruits[x]}")

#print(dir(fruits))
#print(help(fruits))