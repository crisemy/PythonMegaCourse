import pandas

# Initiating a Pandas Object with a method to read the .csv file. 
# The dtype means that we're sending a String rather than an Integer for the ID of the Hotel.
df = pandas.read_csv("hotels.csv", dtype= {"id" : str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    # What an User can do? User can Book a hotel
    def book(self):
        '''Books a hotel by changing its availability to NO'''
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False) # Updates the file itself. Pyton won't add another index.
    
    def available(self):
        '''Checks if the Hotel is available'''
        # Searchs for the ID that is being given as parameter and squeeze it. 
        # The squeeze method returns a String
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        
    # What an User can do? Get a reservation ticket
    def generate(self):
        content = f"""
        Thank you for our reservation:
        Here are your booking data:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name} 
        """

'''MAIN PROGRAM'''
print(df)
hotel_ID = input("Enter the id of the Hotel: ")

# Init the Object
hotel = Hotel(hotel_ID)

if (hotel.available):
    hotel.book()
    name = input("Enter your name: ")
    # Providing the Hotel ID and the Name of the person who reserves the Ticket
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")

'''
Hotels.csv FILE
id                     name        city         capacity   available
0  134  Tourist Sunny Apartment   Anchorage         4       yes
1  188              Snow Palace   New Delhi         5        no
2  655           City Break Inn  Porto-Novo         3        no'''