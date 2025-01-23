# Make a program that reads an integer number and displays its successor and predecessor on the screen.

print('--------------Exercise 005--------------')

# Read the number from the user
number = int(input('Please enter a number: '))

# Calculate the successor and predecessor

successor = number + 1
predecessor = number - 1

# Display the results

print('The successor of {} is {}'.format(number, successor))
print('The predecessor of {} is {}'.format(number, predecessor))
