import math
 
def find_Diameter(radius): # Function to find the diameter of a circle
    return 2 * radius
 
def find_Circumference(radius): # Function to find the circumference of a circle
    return 2 * math.pi * radius
 
def find_Area(radius): # Function to find the area of a circle
    return math.pi * radius * radius
 
r = float(input(' Please Enter the radius of a circle: '))
 
diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)
 
print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)
