#Conditional Expression - A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

num=-5
a=2
b=3
age=19
temperature=30
user_role="admin"

print("Positive" if num>0 else "Negative")

result="Even" if num%2==0 else "Odd"
print(result)

max_num= a if a>b else b
print(max_num)

min_num=a if b>a else a
print(min_num)

status="Adult" if age>=18 else "Minor"
print(status)

weather="Hot" if temperature>20 else "Cold"
print(weather)

access_level= "Full access" if user_role=="admin" else "Limited access"
print(access_level)