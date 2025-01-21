#Create a program that asks for 3 numbers, adds them together, and returns the result.

print('--------------Exercise 003--------------')

#request the numbers
n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
n3 = int(input('Type the third number: '))

#logic
sum = n1 + n2 + n3

#return
print('The balance for {0} + {1} + {2} is {3}'.format(n1, n2, n3, sum))