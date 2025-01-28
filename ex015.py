# Write a program that asks for the number of kilometers driven by a rented car and the number of days it was rented. Calculate the total price to pay, knowing that the car costs $60 per day and $0.15 per kilometer driven.

print('--------------Exercise 015--------------')

# Request to the user the KM and the days.
kilo = float(input('Please enter how many kilometers were driven: '))
days = int(input('Please enter how many days you kept the car: '))

# Calculation
kilodriven = kilo * 0.15
dayskept = days * 60
total = kilodriven + dayskept

# Display the total for the user.
print('You kept the car for {1} days and drove {0:.0f} kilometers. Our rates are $60 per day and $0.15 per kilometer driven. Therefore, your total is ${3:.0f} (days kept) + ${2:.2f} (kilometers driven) = ${4:.2f}.'.format(kilo, days, kilodriven, dayskept, total))