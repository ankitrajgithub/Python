# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

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