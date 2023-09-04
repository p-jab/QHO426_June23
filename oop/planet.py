from human import Human
from robot import Robot

class Planet:

    def __init__(self, n="Planet"):
        self.name = n
        self.inhabitants = {"humans":[], "robots":[]}

    def __str__(self):
        x = [name for name in self.inhabitants.values()]
        return f"{self.name} contains {x}"

    def __repr__(self):
        return f"Planet(name={self.name}, inhabitants={self.inhabitants})"

    def add_inhabitant(self, inh):
        if isinstance(inh, Human):
            self.inhabitants["humans"].append(inh)
        elif isinstance(inh, Robot):
            self.inhabitants["robots"].append(inh)

    def remove_inhabitant(self, inh):
        if inh in self.inhabitants["humans"]:
            self.inhabitants["humans"].remove(inh)
        elif inh in self.inhabitants["robots"]:
            self.inhabitants["robots"].remove(inh)


if __name__ == "__main__":
    h1 = Human("Bob", 23)
    h2 = Human("Betty", 28)
    r1 = Robot("Wall-E", 2)
    r2 = Robot("RoboCop", 34)
    mars = Planet("Mars")
    print(mars)
    mars.add_inhabitant(r1)
    mars.add_inhabitant(r2)
    mars.add_inhabitant(h1)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.remove_inhabitant(h1)
    mars.remove_inhabitant(r2)
    print(repr(mars))