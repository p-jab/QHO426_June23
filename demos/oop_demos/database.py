from person import Person

class Database:

    def __init__(self, name):
        self.name = name + "'s database"
        self.people = []
        self.num = len(self.people)

    def add_person(self, p):
        self.people.append(p)
        self.num += 1

    def remove_person(self,p):
        if p in self.people:
            self.people.remove(p)
        else:
            print("Person does not exist in this database")

    def display_all(self):
        for person in self.people:
            print(person)

if __name__ == "__main__":
    p1 = Person("Mary", 55, "Truck Driver", 68)
    p2 = Person("Urdoh", 19, "Waiter", 54)
    p3 = Person("Alek", 22, w=800)
    db = Database("QAHE")
    db.add_person(p2)
    db.add_person(p3)
    db.add_person(p1)
    db.display_all()
    print("*"*20)
    db.remove_person(p3)
    db.display_all()