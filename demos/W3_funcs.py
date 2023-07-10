#Definition of a function  - specifying what the procedure is, what it does and how so that it can be later called/used (maybe multiple times)

#Parameter - data given into/injected into your function
#Default Parameter - assumed if nothing is passed as argument
def t_area(b=1,h=1):
    area = 0.5*h*b
    return area



#Call to the function - make your program execute the function
total = t_area() + t_area(h=5) + t_area(10,18)
print(f"Total area of 3 triangles is {total}")

height = float(input("Enter Height: "))
base = float(input("Enter Base: "))
t_area(height, base)