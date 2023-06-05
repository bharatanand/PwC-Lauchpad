# Scenario:

# The factorial of any number n is represented by n! which is equal to 1*2*3*....*(n-1)*n.
# E.g.:
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1
# Write a Python program to calculate the factorial of any given number.  
# If you enter a negative number, display
# "Factorial does not exist for negative numbers" and stop the program. 

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial does not exist for negative numbers")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    print("Factorial is", factorial)
