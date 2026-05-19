#Indexing - Accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number="1234-5678-9101-1121"

print(credit_number[0])

print(credit_number[0:4])

print(credit_number[:4])

print(credit_number[5:])

print(credit_number[-1])

print(credit_number[:])

print(credit_number[::2])

#Exercise 1 - Last 4 digits of credit number
last_digits=credit_number[-4:]
print(f"Last 4 digits : {last_digits}")

#Exercise 2 - Reverse credit number
reverse_credit_number=credit_number[::-1]
print(f"Reverse credit number : {reverse_credit_number}")