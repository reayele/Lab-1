"""
Program name: Geometry Calculator
Author: Rediet Ayele
Purpose: Contains functions: Import the Circle.py and Rectangle.py modules
Date: 06/20/26
"""
import circle as c
import rectangle as r

# The aliases are necessary because there are duplicate modules that have a function that have calc_area(),
#  so the aliases help differentiate where the different functions come from which modules.
while True:
    print("Geometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5):"))

    if choice == 1:
        radius = float(input("\nEnter the radius of the circle: "))
        area = c.calc_area(radius)
        area = round(area, 3)
        print("\nThe area of the circle is", area)
        input("Press Enter to Continue")

    elif choice == 2:
        radius = float(input("\nEnter the radius of the circle: "))
        circumference = c.calc_circumference(radius)
        circumference = round(circumference, 3)
        print("\nThe circumference of the circle is", circumference)
        input("Press Enter to Continue")

    elif choice == 3:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = r.calc_area(width, height)
        area = round(area, 3)
        print("\nThe area of the rectangle is", area)
        input("Press Enter to Continue")

    elif choice == 4:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        perimeter = r.calc_perimeter(width, height)
        perimeter = round(perimeter, 3)
        print("\nThe perimeter of the rectangle is", perimeter)
        input("Press Enter to Continue")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Please enter a valid number")
    