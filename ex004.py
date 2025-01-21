#Create a program that reads something from the keyboard and displays its primitive type and all possible information about it.

print('--------------Exercise 004--------------')

#request for something

n = input('Type something: ')

#return the checks
print('The primitive type for this value is ', type(n))
print('Only has spaces? ', n.isspace())
print('Is a number? ', n.isnumeric())
print('Is alphabetical? ', n.isalpha())
print('Is alphanumeric? ', n.isalnum())
print('Is in Upper? ', n.isupper())
print('Is in lower? ', n.islower())
print('Is capitalized? ',n.istitle())