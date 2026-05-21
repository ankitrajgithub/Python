# keyword arguments = An argument preceded by an identifier
#                     Helps with readability
#                     Order of arguments doesn't matter
#                     1. Positional, 2. Default, 3. KEYWORD, 4. Arbitrary

def hello(greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello",title="Mr.",first="Ankit",last="Raj")

for x in range(1,11):
    print(x,end=" ")   # end = Keyword argument
print()

print("1","2","3","4","5","6","7","8","9","10",sep="-")  # sep = Keyword argument

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

my_phone_number=get_phone(country="+91",area=123,first=456,last=7890)
print(my_phone_number)