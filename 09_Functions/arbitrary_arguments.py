# *args = Allows you to pass multiple non-key arguments (Tuples)
# **kwargs = Allows you to pass multiple keyword arguments (Dictionary)
#            * unpacking operator
#            1. Positional, 2. Default, 3. Keyword, 4. ARBITRARY

def add(*args):
    print(type(args))
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5,6,7,8))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
    print()

display_name("Mr.","Ankit","Raj")

def print_address(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key}: {value}",end=" ")
    print()

print_address(apartment="100",street="123 Fake St.",city="Detroit",state="MI",zip="123456")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    for key,value in kwargs.items():
        print(f"{key}: {value}",end=" ")
    print()
    if "apartment" in kwargs:
        print(f"{kwargs.get('apartment')} {kwargs.get('street')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')} {kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr.","Ankit","Raj",apartment="100",street="123 Fake St.",city="Detroit",state="MI",zip="123456")