def adding(lista = []):
    new_member = input("Enter name of new avenger: ")
    lista.append(new_member)

def remove(lista = []):
    rejected = input("Enter name of avenger to be removed: ")
    if rejected in lista:
        lista.remove(rejected)

def printing(lista = []):
    for hero in lista:
        print(f"The mighty {hero} is part of the avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add an Avenger\n2-Remove an Avenger\n3-Check on the Team\n4-Exit\nOption: "))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 4:
            break
        else:
            print("No such option. Go to Specsavers!")

run()