# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year=2024
    num_of_students=0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

print(Student.num_of_students)

student1=Student("Ankit",22)
student2=Student("Ankur",23)

print(Student.num_of_students)

print(Student.class_year)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(student1.num_of_students)

print(student2.name)
print(student2.age)
print(student2.class_year)
print(student2.num_of_students)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students")