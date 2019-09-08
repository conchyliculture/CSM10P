"""
Alec Glavey
bmi.py
8-27-19
Ver 1.5
A Python program that calculates and displays a person’s body mass index (BMI).
Calculate and display a message indicating whether the person has optimal weight,
is underweight, or is overweight.
"""
# Get weight and height from user
weight = int(input("Input your weight: "))
height = int(input('Input your height: '))

#Calculate bmi
bmi = (weight * 703) / height ** 2

# Determine if they are in the healthy range of bmi and print bmi
if bmi > 18.5 and bmi < 25:
    print('Your body mass index of', format(bmi,',.1f'), 'shows you are in healthy range')

# Show bmi and that the user is underwieght
elif bmi < 18.5:
    print('Your body mass index of', format(bmi,',.1f'), 'shows you are underweight')

# Show bmi and that the user is overweight
elif bmi > 25:
    print('Your body mass index of', format(bmi,',.1f'), 'shows you are overweight.')

# Failsafe
else:
    print('Undefined')