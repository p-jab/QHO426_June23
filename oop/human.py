from inhabitant import Inhabitant
from clothing import Clothing

class Human(Inhabitant):

    def __init__(self, n="Human", a=0):
        super().__init__(n, a)
        self.clothing = []

    def __str__(self):
        return f"Human called {self.name} is {self.age} years old and has {self.energy} energy. They wear {self.clothing}"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy}, clothing={self.clothing})"

    def dress(self, clothing):
        self.clothing.append(clothing)

    def undress(self, clothing):
        if clothing in self.clothing:
            self.clothing.remove(clothing)

if __name__ == "__main__":
    h = Human()
    h.display()
    print(h)
    print(repr(h))
    for i in range(4):
        h.grow()
    h.move(56)
    print(h)
    h.eat(20)
    print(h)
    trousers = Clothing(material="jeans")
    h.dress(trousers)
    print(h)