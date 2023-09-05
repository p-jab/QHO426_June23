from planet import Planet
from random import randint
from human import Human
from robot import Robot
import matplotlib.pyplot as plt

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

    def show_population(self):
        n_planets = len(self.planets)
        fig = plt.figure()
        for i in range(n_planets):
            planet = self.planets[i]
            n_humans = len(planet.inhabitants["humans"])
            n_robots = len(planet.inhabitants["robots"])
            ax = fig.add_subplot(n_planets, 1, i+1)
            ax.bar(["Humans", "Robots"], [n_humans, n_robots])
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":
    u = Universe()
    for i in range(6):
        u.generate("Jupiter")
    u.show_population()


