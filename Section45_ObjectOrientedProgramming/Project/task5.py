''' Implement/code the User.get_name method, so the method returns the capitalized version of the user's 
name (e.g., JOHN). Note that the name is stored in the instance variable. Also, call the method for 
the instance you created in Task 4.'''


class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        return self.name.upper()
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age


# Creating the Object and passing object parameters to the init class
user = User("John", 1999) 
print(user.get_name(), user.age(2024))
    
    
    
    
    
    
    
    

'''
# Calling the Method to calculate John's age
currentYear = 2024
print("John's age is:", user.age(currentYear))
print("My age is:", user2.age(currentYear))


class User:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        return self.name.upper()
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age

user = User("john", 1999)
print(user.age(2023))
print(user.get_name())
'''
