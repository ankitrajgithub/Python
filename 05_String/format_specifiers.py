# Format Specifiers : {:flags} Format a value based on what flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

pi=3.14159265359
price=10.846744
neg_price=-100
prices=1000235894952.125311

print(f"Value of pi upto 2 decimal places : {pi:.2f}")
print(f"Value of pi upto 5 decimal places : {pi:.5f}")

print(f"Price : {price:15}")

print(f"Price : {price:015}")

print(f"Price : {price:<15}")

print(f"Price : {price:>15}")

print(f"Price : {price:^15}")

print(f"Price : {price:+}")

print(f"Price : {neg_price:+}")

print(f"Price : {price: }")

print(f"Price : {neg_price:=10}")

print(f"Price : {prices:,}")

print(f"Price : {prices:+,.2f}")

print(f"{price=}")