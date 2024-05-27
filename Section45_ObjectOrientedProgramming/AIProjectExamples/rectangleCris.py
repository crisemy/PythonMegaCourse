class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_area(self):
        # A=Length × Width
        return self.length * self.width
    
    def get_perimeter(self):
        # P=2×(Length + Width)
        return 2 * (self.length + self.width)

length = float(input("Insert the Lenght: "))
width = float(input("Insert the width: "))

# Initialize the object with the specific value
rec = Rectangle(length, width)
print("The area is: ", rec.get_area())
print("The perimeter is: ", rec.get_perimeter())