#Open file for reading
f = open("files/song.txt")
#Print single line
# print(f.readline(), end="")
# print(f.readline(), end="")
#Print full content of the file
#print(f.read())
#Grab content of txt file and save it as a list
lista = f.readlines()
print(lista)
print(lista[2])
f.close() #Close file to make it available again
g = open("files/song.txt", "a")
#Write a single line into the end of the file
g.write("\nAnd it's everlasting, infinite\n")
#Write multiple lines into a file
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love\n"])
g.close()