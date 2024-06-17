#TriangeTypechecker
# Prompt the user to enter the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the given sides can form a triangle using the triangle inequality theorem
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # If the sides can form a triangle, determine the type of triangle
    if side1 == side2 == side3:
        # All sides are equal
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        # Exactly two sides are equal
        print("The triangle is isosceles.")
    else:
        # No sides are equal
        print("The triangle is scalene.")
else:
    # If the sides cannot form a triangle, print an appropriate message
    print("The given lengths cannot form a triangle.")
