class Animal:
    def __init__(self, specie, sound):
        # Init variables that are gonna be invoked by the object.
        self.specie = specie
        self.sound = sound
    
    def get_specie(self):
        return self.specie  # returns the value that is part of the init method and the object
    
    def make_sound(self):
        return self.sound  # returns the value that is part of the init method and the object

# Init Variables
animal = Animal("Bird", "Pio-pio")
#(f"The {animal.get_specie()}") Proper way of include method properties in the Print statement
print(f"The {animal.get_specie()} says {animal.make_sound()}!")
animal2 = Animal("mammal", "Auhhhhhhhh")
print(animal2.get_specie(), animal2.make_sound())

