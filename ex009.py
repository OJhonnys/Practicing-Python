# Write a program that reads any integer and displays its multiplication table on the screen.

print('--------------Exercise 009--------------')

# Resquest a number from the user.
num = int(input('Please enter a number: '))

# Calculate the multiplication table.

multi1 = num * 1
multi2 = num * 2
multi3 = num * 3
multi4 = num * 4
multi5 = num * 5
multi6 = num * 6
multi7 = num * 7
multi8 = num * 8
multi9 = num * 9
multi10 = num * 10

# Display the result
print('THE TABLE OF {0:.0f} \n {0:.0f} x 1 = {1:.0f} \n {0:.0f} x 2 = {2:.0f} \n {0:.0f} x 3 = {3:.0f} \n {0:.0f} x 4 = {4:.0f} \n {0:.0f} x 5 = {5:.0f} \n {0:.0f} x 6 = {6:.0f} \n {0:.0f} x 7 = {7:.0f} \n {0:.0f} x 8 = {8:.0f} \n {0:.0f} x 9 = {9:.0f} \n {0:.0f} x 10 = {10:.0f}'.format(num, multi1, multi2, multi3, multi4, multi5, multi6, multi7, multi8, multi9, multi10))