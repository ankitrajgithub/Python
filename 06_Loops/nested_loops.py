#nested loop - A loop within another loop (outer, inner)
#              outer loop:
#                  inner loop:

for x in range(5):
    for y in range(1, 11):
        print(y, end=" ")
    print()

rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
symbol=input("Enter the symbol: ")

for row in range(rows):
    for column in range(columns):
        print(symbol, end=" ")
    print()

for x in range(1,11):
    for y in range(1,11):
        print(f"{x}*{y}={x*y}")