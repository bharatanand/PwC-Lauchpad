# Objective:
# To work with the print statement
# Scenario:
# Imagine yourself to be a scientist who has developed an intellectual system that converts text to speech.
# You are getting ready for its demo and want to feed the information that your system 
# has to convert to speech.
# Simulate this through python.
# Note: The information includes the name of the AI system, creator, purpose of creation, Memory, etc.
# Enter name of the AI system , enter creator name, enter purpose of creation, 
# enter memory of the system , enter speed of the system

Name = input("Enter the name of the AI system:\n")
Creator = input("Enter the name of the creator:")
Purpose = input("Enter the purpose of creation: ")
Memory = input("Enter the memory of the system: ")
Speed = input("Enter the speed of the system: ")

print("I am " + Name + ", created by " + Creator + " for the pupose of "
      + Purpose + ". Memory I consume is around " + Memory + " and my speed is " + Speed + " GHZ.")
