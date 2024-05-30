import pandas

# Initiating a Pandas Object with a methods to read .csv files. 
# The dtype means that we're sending a String rather than an Integer for the ID of the Hotel and a 
# STR as part of the entire record for every one of those Hotels.
df = pandas.read_csv("hotels.csv", dtype= {"id" : str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records") # Init the Object into a Dictionary to compare values.


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, 
                     "holder": holder, "cvc": cvc}
        # Compare whether a specific Card is present as part of the cards.csv file.
        if card_data in df_cards:
            return True
        else:
            return False


'''MAIN PROGRAM'''
print(df)
hotel_ID = input("Enter the id of the Hotel: ")

# Init the Object
hotel = Hotel(hotel_ID)

if (hotel.available):
    # Asks Users for a specific Credit Card Number
    credit_card = CreditCard(number="123456") # Adding a harcoding one which corresponds with a record in the cards.csv file
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        # Providing the Hotel ID and the Name of the person who reserves the Ticket
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print("Goes here or not?")
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your payment. Please, try again!")
else:
    print("Hotel is not free.")

'''
Hotels.csv FILE
id                     name        city         capacity   available
0  134  Tourist Sunny Apartment   Anchorage         4       yes
1  188              Snow Palace   New Delhi         5        no
2  655           City Break Inn  Porto-Novo         3        no
s'''