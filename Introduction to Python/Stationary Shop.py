# Objective:
# To work with Operators

# Scenario:
# A new stationary shop has been opened in the city.
# The owner asks his accountant to take the list of items sold in the store.
# The list should contain the details of the items and their costs. Help the accountant to
# generate the prince list by writing a Python program.  Generate list with just 4 products -
# A4sheets, pen, pencil and eraser and get the price of the items from the user.
# Please refer the sample input and output statements for more clarifications.

# Guidelines:
#     The amount must be displayed with 2 decimal places.
#     On entering the product price to be a negative number,
#     the program should display the message " Invalid input" and stop the program.

item1 = "A4sheet"  # Name of item 1
item2 = "pen"  # Name of item 2
item3 = "pencil"  # Name of item 3
item4 = "eraser"  # Name of item 4

price1 = float(input("Cost of {}: ".format(item1)))  # Input price for item 1
price2 = float(input("Cost of {}: ".format(item2)))  # Input price for item 2
price3 = float(input("Cost of {}: ".format(item3)))  # Input price for item 3
price4 = float(input("Cost of {}: ".format(item4)))  # Input price for item 4

valid_input = True  # Flag to track if inputs are valid

if price1 < 0:  # Check if price for item 1 is negative
    # Print "Invalid input" message for item 1
    print("Invalid input for", item1)
    valid_input = False  # Set flag to indicate invalid input

if price2 < 0:  # Check if price for item 2 is negative
    # Print "Invalid input" message for item 2
    print("Invalid input for", item2)
    valid_input = False  # Set flag to indicate invalid input

if price3 < 0:  # Check if price for item 3 is negative
    # Print "Invalid input" message for item 3
    print("Invalid input for", item3)
    valid_input = False  # Set flag to indicate invalid input

if price4 < 0:  # Check if price for item 4 is negative
    # Print "Invalid input" message for item 4
    print("Invalid input for", item4)
    valid_input = False  # Set flag to indicate invalid input

if valid_input:  # Check if all inputs are valid
    print("\nItems Details\n")
    print("{}: {:.2f}".format(item1, price1))  # Print item 1 details
    print("{}: {:.2f}".format(item2, price2))  # Print item 2 details
    print("{}: {:.2f}".format(item3, price3))  # Print item 3 details
    print("{}: {:.2f}".format(item4, price4))  # Print item 4 details
