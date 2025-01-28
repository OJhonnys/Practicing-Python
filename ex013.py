# Create an algorithm that reads an employee's salary and shows their new salary with a 15% raise.

print('--------------Exercise 013--------------')

# Request the employee's salary
salary = float(input('Please enter the salary: '))

# Calculation of the new salary.
newsalary = salary + (salary * 0.15)

# Display the new salary.
print("The employee's salary was ${0:.2f}. After the 15% of increase, the new salary is ${1:.2f}".format(salary, newsalary))
