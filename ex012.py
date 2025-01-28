# Create an algorithm that reads the price of a product and shows its new price with a 5% discount.

print('--------------Exercise 012--------------')

# Request to the user to enter the value.
value = int(input('Enter the product price: '))

# Calculation of 5% of the price.
newprice =  value - (value * 0.05)
discount = value * 0.05

# Display the final price.
print(' The new price with the 5% of discount is ${0:.2f} and the total in discount is ${1:.2f}.'.format(newprice, discount))