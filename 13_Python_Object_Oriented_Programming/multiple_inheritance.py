# Multiple Inheritance = Inherit from more than one parent class
#                        C(A,B)

class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Predator:
    def hunt(self):
        print("This animal is hunting.")

class Fish(Prey, Predator):
    pass

fish = Fish()
fish.hunt()
fish.flee()