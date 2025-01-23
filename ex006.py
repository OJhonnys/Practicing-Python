# Create an algorithm that reads a number and displays its double, triple, and square root.

print('--------------Exercise 006--------------')

# Read the number from the user
number = int(input('Please type a number: '))

# Calculate the double, triple and square root
double = number * 2
triple = number * 3
squareroot = number **(1/2)

# Displays in the screen
print(' The double of {0} is {1}. \nThe triple of {0} is {2}. \nThe square root of {0} is {3:.2f}.'.format(number, double, triple, squareroot))
