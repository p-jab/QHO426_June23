pop_dict = {"The Matrix":["Keanu Reeves", "Carrie-Anne Moss", "Hugo Weaving"],
            "Harry Potter":["Daniel Ratcliffe", "Emma Watson", "Rupert Grint"],
            "Friends": ["Jennifer Aniston", "Courtney Cox", "Lisa Kudrow"],
            "The Office": ["Steve Carell", "Rain Wilson", "John Krasinski"],
            "Jack Ryan": ["John Krasinski", "Abbie Cornish"],
            "DS:in MoM": ["Benedict Cumberbach", "John Krasinski"]}

def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        print(f"{title} is not part of the database")
        return []

def add_title(title, cast):
    pop_dict[title] = cast

def count_actors():
    actors = dict()
    for cast_list in pop_dict.values():
        for actor in cast_list:
            if actor in actors:
                actors[actor] += 1
            else:
                actors[actor] = 1
    return actors

print(count_actors())

#Homework - create a menu in run() to complete this demo


# add_title("The Boys", ["Anthony Starr", "William Butcher", "Hughie"])
# add_title("Friends", ["Jennifer Aniston"])
# t = input("What is the title of a movie you want to check? ")
# print(get_cast(t))