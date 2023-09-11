from tech import Tech

class Laser(Tech):

    MAX_RANGE = 100

    def __init__(self):
        pass

    def __str__(self):
        return "Laser object with range 100m"

    def __repr__(self):
        return "Laser()"

    def fire(self, range):
        if range > Laser.MAX_RANGE:
            print("Enemy is safe")
        else:
            print("Pew-Pew...enemy is in trouble")

    def activate(self):
        print("Laser ready to fire!")

    def deactivate(self):
        print("Laser - turned off")

if __name__ == "__main__":
    laser = Laser()
    print(laser)
    laser.activate()
    laser.fire(120)
    laser.fire(80)
    laser.deactivate()