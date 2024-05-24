'''Task 4: Let us suppose the current year is 2023.
1. Create a User instance for John, whose birth year is 1999.
2. Call the age method for that instance and print out the output.

Solution: You should get 24 as output.'''


class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        pass
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age
    

# Creating the Object
user = User("John", 1999)
user2 = User("Cris", 1977)

# Calling the Method to calculate John's age
currentYear = 2024
print("John's age is:", user.age(currentYear))
print("My age is:", user2.age(currentYear))
