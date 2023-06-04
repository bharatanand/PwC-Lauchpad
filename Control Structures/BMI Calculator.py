# Objective:
# To work with Control structures
# Scenario:
# Program in Python to compute the BMI of a person and display the risk associated with it by
# entering the height in 'm' and
# weight in' kg'.  

# Note:
#     To calculate the BMI apply the formula:  BMI = weight(kg)/( height(m)*height(m) ).
#     The result must be adjusted to one decimal place.
#     When the height or weight is entered as a negative number or zero, then display the message
#     "Provide a valid input" and stop the program.

# Get the weight from the user and convert it to an integer
weight = int(input("Enter the weight of the person(kg):").strip())

# Get the height from the user and convert it to a float
height = float(input("Enter the height of the person(m):").strip())

# Check if both height and weight are greater than 0
if weight > 0 and height > 0:
    # Calculate the BMI using the formula and round it to 1 decimal place
    bmi = weight / (height * height)
    BMI = round(bmi, 1)

    # Check the BMI range and display the corresponding risk message
    if BMI >= 27.5:
        print("Your BMI is", BMI, "(High Risk).")
    elif 23 <= BMI <= 27.4:
        print("Your BMI is", BMI, "(Moderate Risk).")
    elif 18.5 <= BMI <= 22.9:
        print("Your BMI is", BMI, "(Low Risk).")
    elif BMI < 18.5:
        print("Your BMI is", BMI, "(Risk of nutritional deficiency diseases).")
else:
    # Display an error message for invalid input
    print("Provide a valid input.")
