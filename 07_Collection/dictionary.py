# Dictionary - Collection of {key : value} pairs. Ordered and changeable. No Duplicates

capitals = {"USA":"Washington DC","India":"New Delhi","China":"Beijing","Russia":"Moscow"}

print(capitals)

print(capitals["China"])
print(capitals.get("China"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Japan":"Tokyo"})

capitals.pop("China")

capitals.popitem()

key=capitals.keys()
print(key)

for key in capitals.keys():
    print(key,end=" ")
print()

values=capitals.values()
print(values)

for value in capitals.values():
    print(value,end=" ")
print()

items=capitals.items()
print(items)

for key,value in capitals.items():
    print(key,"->",value)

capitals.clear()

#print(dir(capitals))
#print(help(capitals))