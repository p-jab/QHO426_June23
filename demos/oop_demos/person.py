#The class Person which is a blueprint for my objects to store information about people
class Person:

    #CLASS Attribute -> attribute/feature accessible to every object
    MAX_W = 150

    #Static Method -> Utility function that does NOT require an object to work on
    def is_mature(age):
        if age >= 18:
            return "Person is mature"
        else:
            return "Person is immature"

    #Initialiser/Constructor -> function automatically called when and objec
    #is instantiated (magic method)
    #Initialiser of ANY class has the same name
    #self - reference to an object instantiated
    #DUNDER - Double Underscore
    def __init__(self, name="John", age=0, job="None", w=MAX_W):
        #Instance Attributes (features of an object)
        self.name = name
        self.age = age
        self.job = job
        if w > Person.MAX_W:
            self.weight = Person.MAX_W
        else:
            self.weight = w

    #Magic mathod str provides "informal" representation of an object via string
    #Automatically invoked when passing your object to print()
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}"

    #Magic method repr provides "formal" representation of an object via string
    #How you wish to store/restore object later
    def __repr__(self):
        return f"Person(name={self.name},age={self.age},job={self.job},w={self.weight})"

    #Method - function attached to a specific data type (class!)
    #Instance Method - a method that applies to a specific instance of the class
    def eat(self, food, w):
        print(f"{self.name} has eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight} kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} now weights {self.weight} kg")


#Object instantiation - creating new instance from the class
if __name__ == "__main__":
    print(Person.is_mature(12))
    p1 = Person("Piotr", 77, "Tutor", 83)
    p2 = Person("Harry", 27, "Plumber", 70)
    print(Person.is_mature(p2.age))
    print(p1)
    p1.eat("Ice Cream", 0.3)
    p2.eat("Goulash", 1)
    p1.exercise(0.1)
    p1.exercise(0.45)
    p2.exercise(0.2)
