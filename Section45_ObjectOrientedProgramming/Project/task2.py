'''Task 2: Add an __init__ method to the User class. The method should have:
1. three parameters, self, name, and birthyear.
2. name and birthyear should also be instance variables.'''


class User:
    def __init__(self, name, birthyear):
        # Instance variables
        self.name = name
        self.birthyear = birthyear
    def get_name(self):
        pass
    def age(self, current_year):
        pass

