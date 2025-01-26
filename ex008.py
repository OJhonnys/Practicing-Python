# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

print('--------------Exercise 008--------------')

# Request the value from the user.
meters = float(input('Please enter the value in meters: '))

# Convert meters in centimeters and millimeters.
centi = meters * 100
milli = meters * 1000

# Display the result
print('{0:.0f} meters converted to centimeters are {1:.0f} cm. And to millimeters, they are {2:.0f} mm.'.format(meters, centi, milli))