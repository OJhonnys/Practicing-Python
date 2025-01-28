# Write a program that takes a temperature entered in degrees Celsius and converts it to degrees Fahrenheit.

print('--------------Exercise 014--------------')

# Resquest user to enter the temperature in celcius.
celcius = float(input('Please enter your temperature in degrees Celcius: '))

# Converting celcius to fahrenheit.
fahrenheit = (celcius * 9/5) + 32

# Display the result
print('Your temperature is {0} degrees Celsius, which is equivalent to {1} degrees Fahrenheit.'.format(celcius, fahrenheit))