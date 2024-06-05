import pandas

# REVISIT THIS SCRIPT WHICH IS NOT RETURNING PROPER VALUES 

# Initiating a Pandas Object with a methods to read .csv files. 
# The dtype means that we're sending a String rather than an Integer for the ID of the Hotel and a 
# STR as part of the entire record for every one of those Hotels.
df = pandas.read_csv("hotels.csv", dtype= {"id" : str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records") # Init the Object into a Dictionary to compare values
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


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
        return content

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

# Inheritance from the CreditCard Class which is the Parent class. The SecureCreditCard class is the child
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        # Sending the Number of the credit card (in the card_security.csv file) which needs to be consistent with the number of the cards.csv file.
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

'''MAIN PROGRAM'''
print(df)
hotel_ID = input("Enter the id of the Hotel: ")

# Init the Object
hotel = Hotel(hotel_ID)

if (hotel.available):
    # Asks Users for a specific Credit Card Number 1234567890123456
    credit_card = SecureCreditCard(number="1234567890123456") # Adding a harcoding one which corresponds with a record in the card_security.csv file
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            # Providing the Hotel ID and the Name of the person who reserves the Ticket
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print("Goes here or not?")
            print(reservation_ticket.generate())
        else: 
            print("Credit Card authentication failed. Please, try again later")
    else:
        print("There was a problem with your payment. Please, try again!")
else:
    print("Hotel is not free")

'''
Hotels.csv FILE
id                     name        city         capacity   available
0  134  Tourist Sunny Apartment   Anchorage         4       yes
1  188              Snow Palace   New Delhi         5        no
2  655           City Break Inn  Porto-Novo         3        no
s'''