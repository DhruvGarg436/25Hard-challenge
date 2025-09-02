# Area Of Triangle
import math
side1 = int(input("Enter 1st side of triangle(in cm) "))
side2 = int(input("Enter 2nd side of triangle(in cm) "))
side3 = int(input("Enter 3rd side of triangle(in cm) "))
S = (side1 + side2 + side3)/2
area = math.sqrt(S*(S-side1)*(S-side2)*(S-side3))
print(area, "cm\u00b2 is the area of the given triangle.")
