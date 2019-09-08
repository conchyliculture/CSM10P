
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
    
    
"   
Pennies for Pay

Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days.

Display a table showing what the salary was for each day, and then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

Input Validation: Don’t accept less than equal zero or more than 64 (accept 1-64).
"
