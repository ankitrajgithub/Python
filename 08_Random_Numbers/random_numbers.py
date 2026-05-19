import random

low=1
high=100
options=("Rock","Paper","Scissor")
cards=["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]

number=random.randint(1,20)
numbers=random.randint(low,high)

randoms=random.random()  # Between 0 & 1

option=random.choice(options)

random.shuffle(cards)
print(cards)

print(number)
print(randoms)
print(option)

#print(dir(random))
#print(help(random))