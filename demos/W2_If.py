name = input("Enter your name: ")
#len() ->  function which returns the length of an item
#name = "piotr"
#len(name) = 5

if len(name) > 7:
    print("Your name is very long. Please provide a nickname:")
    name = input()
elif len(name) <= 3:
    print("You have a very short name")
elif name.upper() == "MARTHA":
    print("Why did you say that name!!!")
else:
    print("You have a medium name")
print(f"Welcome {name}!")

