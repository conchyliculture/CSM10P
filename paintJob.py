wallSpace = 115 ** 2
paint = 1
hoursLabor = 8
laborCost = 20.00

wallUserInput = float(input('How many square feet was painted? '))
paintCost = float(input('How much does a gallon of paint cost? '))

paintUsed = wallUserInput / wallSpace * paint
hoursUsed = wallUserInput / wallSpace * hoursLabor
totalPaintCost = paintUsed * paintCost
laborCostPerHour = hoursUsed * laborCost
overallCost = totalPaintCost + laborCostPerHour

print('The number of callons of paint required is/are ', format(paintUsed,',.2f'), 'cans of paint.')
print('Hours of labor required are ', hoursUsed, 'hours')
print('The cost of the paint is ', totalPaintCost, 'dollars.')
print('Cost per hour of the opperation is ', laborCostPerHour, 'dollars.')
print('The total cost of the operation is, ', overallCost, 'dollars.')
