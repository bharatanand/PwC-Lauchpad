# Scenario:
# Write a Pyhon program to calculate and display the income tax of an individual 
# by giving his/her age and annual income. Refer to the INCOME TAX SLAB given below and code accordingly. 

#  INCOME TAX SLAB:
# Age <=60 and income<= 2, 50,000/     :    0% tax
# Age <=60  and income>2,50,000  and income<=  5,00,000    :    10% tax
# Age <=60  and income>5,00,000  and income<=  10,00,000   :    20% tax
# Age <=60  and income    above 10, 00,000/-         :    30% tax
# Age >60 and age<=80  , income<= 3, 00,000/     :    0% tax
# Age >60 and age<=80 ,  income > 3,00,000 and income <=5,00,000 :10% tax
# Age >60 and age<=80 ,  income > 5,00,000 and income <=10,00,000 :    20% tax
# Age >60 and age<=80 ,  income>10,00,000 : 30% tax
# Age >80 and income<= 5, 00,000/     :    0% tax
# Age >80 ,  income > 5,00,000 and income <=10,00,000 : 20% tax
# Age >80  and age<=100,  income >10,00,000 : 30% tax.

# Note:
#     If the age entered by the user is below 18 and above 100, then, display the message "Invalid Age" and stop the program.
#     If the income entered by the user is a negative number, then, display the message " Invalid Income " and stop the program.
#     The tax amount should be displayed in 2 decimal places

def calculate_income_tax(age, income):
    # Check if age is invalid
    if age < 18 or age > 100:
        return "Invalid Age"

    # Check if income is invalid
    if income < 0:
        return "Invalid Income"

    # Calculate tax based on age and income
    if age <= 60:
        if income <= 250000:
            tax_amount = 0
        elif income <= 500000:
            tax_amount = 0.1 * income
        elif income <= 1000000:
            tax_amount = 0.2 * income
        else:
            tax_amount = 0.3 * income
    elif age <= 80:
        if income <= 300000:
            tax_amount = 0
        elif income <= 500000:
            tax_amount = 0.1 * income
        elif income <= 1000000:
            tax_amount = 0.2 * income
        else:
            tax_amount = 0.3 * income
    else:
        if income <= 500000:
            tax_amount = 0
        elif income <= 1000000:
            tax_amount = 0.2 * income
        else:
            tax_amount = 0.3 * income

    # Format tax amount to 2 decimal places and return the result
    return f"The Tax amount is: {tax_amount:.2f}"


def main():
    # Get user input for age
    age = int(input("Enter the age: "))

    # Check if age is invalid
    if age < 18 or age > 100:
        print("Invalid Age")
        return

    # Get user input for income
    income = int(input("Enter the income: "))

    # Check if income is invalid
    if income < 0:
        print("Invalid Income")
        return

    # Calculate tax amount
    tax_amount = calculate_income_tax(age, income)

    # Print the result
    print(tax_amount)


if __name__ == '__main__':
    main()
