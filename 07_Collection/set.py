# Collection = Single "variable" used to store multiple values
# List = [] Ordered and changeable. Duplicates OK
# Set = {} Unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () Ordered and unchangeable. Duplicates OK. Faster

fruits={"apple","banana","mango","pineapple"}

print(fruits)
print(len(fruits))

print("pineapple" in fruits)

fruits.add("orange")

fruits.remove("orange")

fruits.pop()

fruits.clear()

print(fruits)

#print(dir(fruits))
#print(help(fruits))