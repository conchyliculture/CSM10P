"""
Alec Glavey
temperatureConverter.py
8-27-19
Ver 1.3
A program that converts Celsius temperatures to Fahrenheit temperatures.
Ask the user to enter a temperature in Celsius, 
and then display the temperature converted to Fahrenheit.
"""
# Get celcius from the user
celcius = int(input('Input a temperature in Celcius: '))

# Convert celcius into fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32

# Discard any input that's greater or equal to 200, and equal to or less than -60
if celcius >= 200 or celcius <= -60:
    print('Please choose another number less than 200°C and greater than -60°C')

# Print converted temperature
else:
    print(fahrenheit)