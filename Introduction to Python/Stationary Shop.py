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

item1 = "A4sheet"
item2 = "pen"
item3 = "pencil"
item4 = "eraser"

price1 = float(input("Cost of {}: ".format(item1)))
if price1 < 0:
    print("Invalid input")
else:
    price2 = float(input("Cost of {}: ".format(item2)))
    if price2 < 0:
        print("Invalid input")
    else:
        price3 = float(input("Cost of {}: ".format(item3)))
        if price3 < 0:
            print("Invalid input")
        else:
            price4 = float(input("Cost of {}: ".format(item4)))
            if price4 < 0:
                print("Invalid input")
            else:
                print("\nItems Details\n")
                print("{}: {:.2f}".format(item1, price1))
                print("{}: {:.2f}".format(item2, price2))
                print("{}: {:.2f}".format(item3, price3))
                print("{}: {:.2f}".format(item4, price4))
