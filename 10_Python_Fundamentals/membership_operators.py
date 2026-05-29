# Membership Operators = Used to test whether a value or variable is found in a sequence.
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

word="APPLE"

letter=input("Guess a letter in the secret words : ")

if letter.upper() in word:
    print(f"There is a {letter} in the secret word")
else:
    print(f"Sorry, {letter} is not in the secret word")

if letter.upper() not in word:
    print(f"Sorry, {letter} is not in the secret word")
else:
    print(f"There is a {letter} in the secret word")

students={"Ankit","Ankur","Anuj","Aniket"}

student=input("Enter student name : ")

if student in students:
    print(f"{student} is in the students list")
else:
    print(f"{student} is not in the students list")

if student not in students:
    print(f"{student} is not in the students list")
else:
    print(f"{student} is in the students list")

grades={"Ankit":"A","Anuj":"B","Ankur":"C","Aniket":"D"}

student=input("Enter student name : ")

if student in grades:
    print(f"{student}'s grade is {grades.get(student)}")
else:
    print(f"{student} is not in the grades list")

email="ankit@gmail.com"

if "@" in email and "gmail.com" in email:
    print(f"{email} is a valid mail address")
else:
    print(f"{email} is not a valid mail address")