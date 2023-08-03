import json

with open("song.txt") as s:
    lista = s.readlines()
s = set()
all_words = []
for item in lista:
    x = item.strip("\n").replace(",", "").replace("1", "one").replace("\u00C2£", "").replace("5", "five").replace("6","six").lower().split()
    all_words.extend(x)
    s1 = set(x)
    s = s.union(s1)

print(f"You only need {len(s)} unique words to create a viral song!")
dictio = {}
for thing in all_words:
    dictio[thing] = dictio.get(thing, 0) + 1
print(dictio) # lambda functions and sort

with open("onePoundFish.json", "w") as f:
    json.dump(dictio, f, indent=4)

with open("onePoundFish.json") as f:
    d = json.load(f)
print(d)