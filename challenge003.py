#create a program that reads two numbers and displays the sum between them.

#request value a value
value1 = int(input('Type a number: '))
value2 = int(input('Type another number: '))

#logic
sum = value1 + value2

#return
print('The total between {0} and {1} is: {2}'.format(value1, value2, sum))