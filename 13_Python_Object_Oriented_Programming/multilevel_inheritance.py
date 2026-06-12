# Multilevel Inheritance = Inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Fish(Prey): # Multilevel Inheritance
    pass

fish = Fish("Nemo")
fish.eat()
fish.sleep()
fish.flee()