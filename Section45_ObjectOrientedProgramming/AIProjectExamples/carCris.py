

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year    

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
# Init objects for the Cars car

car1 = Car("Ford", "Maverick", "2023")
print(f"The Maker of the vehicle is: {car1.get_make()}.")
print(f"The Model of the vehicle is: {car1.get_model()}.")
print(f"The Year of the vehicle is: {car1.get_year()}.")
