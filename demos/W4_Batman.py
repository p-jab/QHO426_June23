from random import randint


def batman_punch(str=5, technique=8):
    punch_power = 0.4 * str + 0.6 * technique
    return punch_power


def fight_scene(n=2, enemy_str=3):
    total_str = n * enemy_str
    bat_str = batman_punch(randint(0,10), randint(0,10))
    if bat_str >= total_str:
        return "Batman Wins!"
    else:
        return "Batman Looses!"


def roberry_escape(n_of_cars):
    if n_of_cars > 5:
        return "Batman is caught"
    else:
        return "Batman escapes"


def run():
    scene = fight_scene(randint(1,8))
    escape = roberry_escape(randint(2,12))
    print(f"After a long fight, {scene} Afterwards, police chase him and {escape}")

run()