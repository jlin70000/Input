
#IDLE Open Source
#Note to Viewer: Steps are said. Make sure to press enter after each input. 
#Jeremy Luo



# Ask user for dimensions of the two rectangles
length1 = int(input("Enter the length for Rectangle #1: "))
width1 = int(input("Enter the width for Rectangle #1: "))
length2 = int(input("Enter the length for Rectangle #2: "))
width2 = int(input("Enter the width for Rectangle #2: "))

# Calculate the area of each rectangle
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle is larger
if area1 > area2:
    print("Rectangle #1 has an area of", area1)
    print("Rectangle #2 has an area of", area2)
    print("Rectangle #1 is larger than Rectangle #2")
elif area2 > area1:
    print("Rectangle #1 has an area of", area1)
    print("Rectangle #2 has an area of", area2)
    print("Rectangle #2 is larger than Rectangle #1")
else:
    print("Rectangle #1 has an area of", area1)
    print("Rectangle #2 has an area of", area2)
    print("Rectangle #1 and Rectangle #2 are the same size")

# Determine if either rectangle is a square
if length1 == width1:
    print("Rectangle #1 is a square")
if length2 == width2:
    print("Rectangle #2 is a square")
