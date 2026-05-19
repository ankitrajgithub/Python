# Collection = Single "variable" used to store multiple values
# List = [] Ordered and changeable. Duplicates OK
# Set = {} Unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () Ordered and unchangeable. Duplicates OK. Faster

fruits=("orange","apple","banana","strawberry","apple")

print(fruits)
print(len(fruits))
print("apple" in fruits)

print(fruits.index("apple"))

print(fruits.count("strawberry"))

for x in range(0,len(fruits)):
    print(fruits[x])

print(dir(fruits))
#print(help(fruits))