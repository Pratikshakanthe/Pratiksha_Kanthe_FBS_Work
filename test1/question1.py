## WAP to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
r = int(input(" Enter the radius: "))

# Area
area = (l * b) + (1/2 * 3.14 * r * r)

# Perimeter
perimeter = (l + 2*r) + (3.14 * r)

# Output
print("Area  =", area)
print("Perimeter  =", perimeter)