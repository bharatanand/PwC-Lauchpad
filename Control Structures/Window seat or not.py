# Objective:
# To work with Control structures


# Scenario:
# Renn plans a trip to Goa, this weekend. He decides to go by bus and book his 
# ticket through a website. Code logic in Python so that he gets to know if he has booked a window seat or not.  

# Assume the bus to have 11 rows.  Seat number begins with 1 which will be a window seat.  If the no. of seats per row is a 
# factor of the seat number you have entered, then it is a window seat, else it is not a window seat.   Refer to the sample 
# input and output statements for more clarifications.

# Note:
# 1. For any invalid seat number specified as a negative number, zero or the seat number is greater than the total no. of seats, 
#   then display - "Invalid Seat Number" and stop the program.

# 2. If the no. of seats per row specified is less than or equal to zero, then display - "Invalid Input" and stop the program.

 
# Prompt the user to enter the number of seats per row
print("Enter the number of seats per row: \n")
seats_per_row = int(input())

# Check if the number of seats per row is invalid (less than or equal to zero)
if seats_per_row <= 0:
    print("Invalid Input")
    exit()

# Prompt the user to enter the seat number
print("Enter the seat number: \n")
seat_number = int(input())

# Check if the seat number is invalid (negative, zero, or greater than the total number of seats)
if seat_number <= 0 or seat_number > 11 * seats_per_row:
    print("Invalid Seat Number")
    exit()

# Check if the seat is a window seat based on the logic: seat_number % seats_per_row == 1
if seat_number % seats_per_row == 0:
    print("Window Seat")
else:
    print("Not a Window Seat")
