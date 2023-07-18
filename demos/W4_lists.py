#Declare empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["chocolate", "pizza", "doughnouts", "subway"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[-4])
#Print some items off the list
print(yummy[0:4:2])
#Add elements to our list (expand it) - adding at the end of the list
print(bleh)
bleh.append("spinach")
bleh.append("brocolli")
bleh.append("aubergine")
bleh.append("pesto")
print(bleh)
#Add items to a list (multiple items)
bleh.extend(["liver", "bigos", "tomatoes"])
print(bleh)
#Remove item from a list
if "bigos" in bleh:
    bleh.remove("bigos")
print(bleh)
#Insert items at specific positions
bleh.insert(1, "carrot")
print(bleh)
bleh.insert(4, "cabbage")
print(bleh)
#Remove items by index
x = bleh.pop(3)
y = bleh.pop(5)
print(bleh)
print(x, y)
#Mutate your list
print(yummy)
yummy[2] = "pancakes"
print(yummy)
#Check a list for a partifcular data type/traverse a list
lista = ["Fred", 56, True, 99.4, "Potato", False, 82]
sum = 0
for item in lista:
    if isinstance(item, int):
        sum += item
print(sum)