#IDLE Open Source
#Note to Viewer: Notes given in between functions
#Jeremy Luo



import math

print("Triangle Tester")
print('\n')

# take input from the user
a = float(input("What is the length of side 1? "))
b = float(input("What is the length of side 2? "))
c = float(input("What is the length of side 3? "))

# check if the sides form a valid triangle
if a + b > c and b + c > a and a + c > b:
    print("This is a valid triangle!")
    
    # calculate the perimeter of the triangle
    perimeter = a + b + c
    print(f"The perimeter of the triangle is {perimeter:.1f}.")
    
    # check the type of the triangle
    if a == b == c:
        print("This is an equilateral triangle")
    elif a == b or b == c or c == a:
        print("This is an isosceles triangle")
    else:
        print("This is a scalene triangle")
        
    # check if the triangle is a right triangle
    sides = [a, b, c]
    sides.sort() # sort the sides in ascending order
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9):
        print("This is also a right triangle")
else:
    print("This is not a valid triangle.")
