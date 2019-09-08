"""
Alec Glavey
paintJob.py
8-25-19
Ver 1.17
Get wall space to be painted and the cost of paint from the user. Print out the gallons of paint required,
the hours of labor, cost of the paint, the cost of the operation, and the total cost
"""

# Define variables
wallSpace = 115
gallonsPaint = 1
hoursLabor = 8
laborCost = 20.00

# Get wallspace and paint cost from user
wallUserInput = float(input('How many square feet was painted? '))
paintCost = float(input('How much does a gallon of paint cost? '))

# Divide user input by wallspace (115) and multiply by gallonsPaint to find paint used
paintUsed = wallUserInput / wallSpace * gallonsPaint

# Divide user input by wallspace (115) and multiply by hoursLabor to find hours used
hoursUsed = wallUserInput / wallSpace * hoursLabor

# Multiply paintUsed by user input to find the total paint cost
totalPaintCost = paintUsed * paintCost

# Muultiply hoursUsed by laborCost to find the cost of total labor cost
totalLaborCost = hoursUsed * laborCost

# Add the paint cost to the labor cost for the overall cost
overallCost = totalPaintCost + totalLaborCost

# Print the results of the questions
print('The number of gallons of paint required is/are ', format(paintUsed,',.2f'), 'cans of paint.')
print('Hours of labor required are ', format(hoursUsed,',.2f'), 'hours')
print('The cost of the paint is ', format(totalPaintCost,',.2f'), 'dollars.')
print('Cost per hour of the opperation is ', format(totalLaborCost,',.2f'), 'dollars.')
print('The total cost of the operation is, ', format(overallCost,',.2f'), 'dollars.')
