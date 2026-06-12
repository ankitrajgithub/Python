# Class Methods = Allow operations related to the class itself.
#                 Take (cls) as the first parameter. which represents the class itself.


class Student:
    count =0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1

    def get_info(self):
        return f"{self.name} -> {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students : {cls.count}"

student1=Student("Ankit",8.5)
student2=Student("Kashish",8.9)
student3=Student("Anuj",8.4)

print(Student.get_count())
