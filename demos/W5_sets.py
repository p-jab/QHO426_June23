#Initialise empty set
s = set()
#Initialise non-empty set using curly brackets
s1 = {1,2,3,4}
col = {"blue", "green", "red", "yellow", "black", "red", "blue"}
print(col)
#Adding items to the set
col.add("purple")
col.add("orange")
print(col)
#Adding more items at once
col = col.union({"white", "brown", "crimson", "magenta"})
print(col)
#Remove items from set
if "yellow" in col:
    col.remove("yellow")
print(col)
#Sets are heterogenous data structures
col.add(99)
col.add(False)
col.add(76.8)
print(col)
print("-"*20)
c = {"brown", "turquoise", "pink", "red", "cyan", "green"}
#Union = join 2 sets together, not keeping duplicates
c2 = col.union(c)
print(f"col is {col}")
print(f"c is {c}")
print(f"c2 is {c2}")

#Intersection - looking at common values in two sets
c3 = col.intersection(c)
print(f"c3 is {c3}")

#Difference - keep elements of one set that are NOT part of the other
c4 = c.difference(col)
c5 = col.difference(c)
print(f"c4 is {c4}")
print(f"c5 is {c5}")

#BREAK -> 10:45