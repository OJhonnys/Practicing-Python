#Create a program that reads something from the keyboard and displays its primitive type and all possible information about it.
from curses.ascii import isalpha, islower, isupper

print('--------------Challenge 004--------------')

#request a value
n = input('Type something: ')

#return
print(type(n))
print(n.isupper(), n.isalpha(), n.islower(), n.isalnum(), n.isascii(), n.isdecimal())


