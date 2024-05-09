# Coding Exercise 2
# Create a program that prompts the user to input their name repeatedly. 
# Then, the program repeatedly prints out the name with the first letter capitalized.

user_prompt = "Enter a User Name: "
name = input(user_prompt)

while (name != "END"): # It will finish once the user enters 'END'
    print("Your name is: ", name.capitalize()) # It will capitalize the the name
    print("next...")
    name = input(user_prompt)
    
if name == "END":
    print("Thank you for using this program!")
