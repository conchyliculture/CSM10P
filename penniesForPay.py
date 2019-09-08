
# Starting salary
salary = 0.01

totalSalary = 0.00

# Get number of days worked from user
daysWorked = int(input('Enter number of days worked: '))

# Discard input that is equal to or less than 0 and also not greater than 64
if daysWorked <= 0 or daysWorked >= 65:
    print('Please choose a number greater than 0 or less than 65')

else:
    for day in range ( 1, daysWorked + 1 ):
        print('Day ', day, ' salary: ', '$', format(salary, ',.2f'),  sep='')
        
        # Accumulator
        totalSalary = salary + totalSalary
        
        # Double salary every day
        salary = salary+salary

    # Print total salary and exit program
    print('Total salary by day ', day,  ' is $', format(totalSalary, ',.2f'), sep='' )
