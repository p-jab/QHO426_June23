from planet import Planet
from random import randint
from human import Human
from robot import Robot

class Universe:

    def __init__(self):
        self.planets = []

    def generate(self, n=""):
        planet = Planet(n)
        for i in range(randint(1,12)):
            h = Human()
            planet.add_inhabitant(h)
        for i in range(randint(1,12)):
            r = Robot()
            planet.add_inhabitant(r)
        self.planets.append(planet)

if __name__ == "__main__":
    u = Universe()
    u.generate("Earth")
    u.generate("Jupiter")
    print(u.planets)


