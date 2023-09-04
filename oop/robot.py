class Robot:
    MAX_ENERGY = 100

    def __init__(self, n="Robot", a=0):
        self.name = n
        self.age = a
        self.energy = 0

    def __str__(self):
        return f"Robot named {self.name} is {self.age} years old and has {self.energy} energy"

    def __repr__(self):
        return  f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > Robot.MAX_ENERGY:
            self.energy = Robot.MAX_ENERGY

    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0

if __name__ == "__main__":
    r = Robot()
    r.display()
    print(r)
    print(repr(r))
    for i in range(9):
        r.grow()
    r.eat(72)
    print(r)
    r.move(90)
    print(r)
