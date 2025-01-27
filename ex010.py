# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.

print('--------------Exercise 010--------------')

# Resquest a number from the user.
money = float(input('Please enter the quanty of money you have: '))

# Calculation
dolar = money * 3.27

# Display the convertion from R$ to dolar.
print('You have U${0:.2f}, and this amount in Brasilian Real is equivalent to R${1:.2f}.'.format(money, dolar))