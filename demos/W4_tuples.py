#Declare a tuple
x = ("Piotr", 62, True)
y = tuple(["Gary", 23, False])
#Print tuples
print(x)
print(y)
print(x[2])
print(y[0:2])
#Cannot change individual items (immutability)
#x[1] += 1

#Concatenate Tuples
z = x + y
print(z)
print(x)
print(y)

#Use min and max functions on tuples
t = (74, 35, 1, 83, 65, 62)
print(max(t))
print(min(t))

#Fixing errors on tuples
print(x)
l1 = list(x)
l1[2] = False
x = tuple(l1)
print(x)

