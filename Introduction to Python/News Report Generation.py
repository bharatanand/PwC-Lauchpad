# Objective:
# To work with Operators

# Scenario:
# Japan was hit by a huge Tsunami. Lives and properties were lost. 
# Many were injured too. A news reporter has arrived to the spot to analyse and generate report  on the number of people alive , 
# dead and injured. His report also has a statement 
# seeking public to help the people in need. Can you help him to generate the report by writing a Python program ? 

# Guidelines:  
# If the dead count or injured count or safe count entered by the user is a negative number, then display the message 
# "Invalid input" and stop the program.
# The statement for seeking help should be "Please help the people who are suffering!!!".  
# Please refer the sample input and output for more clarifications

print("TSUNAMI REPORT OF JAPAN\n")

dead_count = int(input("Dead Count: \n"))
if dead_count < 0:
    print("Invalid input")
    exit()

injured_count = int(input("Injured Count: \n"))
if injured_count < 0:
    print("Invalid input")
    exit()

safe_count = int(input("Safe Count: \n"))
if safe_count < 0:
    print("Invalid input")
    exit()

print("\nThe number of people\n")
print("Dead:\n", dead_count)
print("Injured:\n", injured_count)
print("Safe:\n", safe_count)

print("\nPlease help the people who are suffering!!!")
