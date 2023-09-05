from abc import ABC

class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self, n="", a=0):
        self.name = n
        self.age = a
        self.energy = Inhabitant.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > Inhabitant.MAX_ENERGY:
            self.energy = Inhabitant.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0
