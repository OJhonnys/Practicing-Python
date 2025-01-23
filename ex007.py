# Create a program that reads a student's two grades, calculates, and displays their average.

print('--------------Exercise 007--------------')

# Read the grade from the user
grade1 = int(input('Please enter the first grade: '))
grade2 = int(input('Please enter the second grade: '))

# Calculate the average
average = (grade1 + grade2) / 2

# Display the result
print('The average of the grades {0} and {1} is {2:.2f}.'.format(grade1, grade2, average))

