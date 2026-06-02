# Multiple Inheritance = Inherit from more than one parent class
#                        C(A,B)

class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Predator:
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

rabbit = Rabbit()
rabbit.flee()

hawk = Hawk()
hawk.hunt()