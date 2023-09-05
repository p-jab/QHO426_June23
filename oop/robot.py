from inhabitant import Inhabitant

class Robot(Inhabitant):

    LAWS = "Protect and Obey!"

    @staticmethod
    def the_laws():
        print(Robot.LAWS)

    def __init__(self, n="Robot", a=0):
        super().__init__(n)

    def __str__(self):
        return f"Robot named {self.name} is {self.age} years old and has {self.energy} energy"

    def __repr__(self):
        return  f"Robot(name={self.name}, age={self.age}, energy={self.energy})"


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
