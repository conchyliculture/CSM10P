"""
Alec
geometryCalculator.py
8-31-19
Ver 1.8
Display a menu with four options. Find the area of a circle, rectangle, triangle.
Option number four quits program. Disregard numbers that aren't 1-4.
Don't accept negative numbers for the area calculations.
"""

from os import sys

# Restart program after a succesful or unsuccesful calculation
while True:
    # Menu
    print("""Geometry Calculator
    1. Calculate the Area of a Circle
    2. Calculate the Area of a Rectangle
    3. Calculate the Area of a Triangle
    4. Quit
    """)

    # Get user number
    choice = int(input('Enter your choice (1-4): '))

    # Circle block
    if choice == 1:
        print(' Circle ')
        # Get input from user
        radius = float(input(' Enter the radius for the circle: '))
        area = 3.14159 * (radius ** 2)
        # Check for invalid numbers
        if radius < 0:
            print('Invalid number')
        else:
            # Print area
            print(format(area,',.2f'))

    # Rectangle block
    elif choice == 2:
        print('Rectangle')
        # Get lenght from user
        length = float(input('Enter the length of the rectangle: '))
        # Check for invalid numbers
        if length < 0:
            print('Invalid number')
        # Get width from user
        else:
            width = float(input('Enter the width of the rectangle: '))
            # Check for invalid numbers
            if width < 0:
                print('Invalid number')

            # Print area
            else:
                area = length * width
                print(format(area,',.2f'))

    # Triangle block
    elif choice == 3:
        print('Triangle')
        # Get base from user
        base = float(input('Enter the base of your triangle: '))
        # Check for invalid numbers
        if base < 0:
            print('Invalid number')
        # Get height from user
        else:
            height = float(input('Enter the height of the triangle: '))
            # Check for invalid numbers
            if height < 0:
                print('Invalid number')
            # Print area
            else:
                area = base * height * 0.5
                print(format(area,',.2f'))

    # Exit program
    elif choice == 4:
        print('Exiting...')
        sys.exit(0)

    # Discard invalid menu options
    else:
        print("Please choose a valid option")
