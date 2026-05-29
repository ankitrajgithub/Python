# variable scope = Where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

x=3

def func1():
#    x=1
    print(x)

def func2():
#    x=2
    print(x)

func1()
func2()

from math import e

e=3

def func3():
    print(e)

func3()

print(e)