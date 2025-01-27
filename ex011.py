# Create a program that reads the width and height of a wall in meters, calculates its area, and determines the amount of paint needed to paint it, knowing that each liter of paint covers an area of 2m².

print('--------------Exercise 011--------------')

# Request the width and height from the user.
width = float(input('Please enter the width in meters: '))
height = float(input('Please enter the height in meters: '))

# Calculation of the area.
area = height * width
paint = area / 2

# Display the amount of paint.
print('For a wall of {0:.0f} H by {1:.0f} W, with an area of {2:.0f} m², {3:.0f} liters of paint will be needed.'.format(width, height, area, paint))


