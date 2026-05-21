#default arguments = A default value for certain parameters.
#                    Default is used when that argument is omitted.
#                    Make your functions more flexible, reduces number of arguments
#                    1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary
import time

def net_price(list_price, discount=0.0, tax=0.05):
    return list_price*(1-discount)*(1+tax)

price=net_price(500,0,0.05)
print(price)

print(net_price(500,0.1))

print(net_price(500,0.1,0))

def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Time is up!")

count(10)
count(30,15)