fruits=["apple","mango","watermelon","guava"]
vegetables=["potato","onion","tomato"]
meats=["fish","chicken","turkey"]

groceries=[fruits,vegetables,meats]

for x in range(0,len(groceries)):
    for y in range(0,len(groceries[x])):
        print(groceries[x][y],end=" ")
    print()

print()

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()

print(groceries[0][3])

#groceries=[("apple","mango","watermelon","guava"),("potato","onion","tomato"),("fish","chicken","turkey")]
#groceries=(("apple","mango","watermelon","guava"),("potato","onion","tomato"),("fish","chicken","turkey"))
#groceries=({"apple","mango","watermelon","guava"},{"potato","onion","tomato"},{"fish","chicken","turkey"})

#Num Pad Program
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))

print("Nokia")
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()