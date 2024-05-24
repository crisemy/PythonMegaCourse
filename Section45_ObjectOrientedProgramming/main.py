import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "app8flask@gmail.com"
        password = "qyciukmocfaiarse"

        receiver = "app8flask@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")


class Database:
    # A special method to be invoked by other methods. Self is a special variable and all the methods have access to self. We use self as the 'middle man' to access variables. The way of sending parameters to the init Class is by providing parameters after the self.
    # Init is a special method that needs to be invoked by the object of a Class. 
    # Self is a special argument. Is the variable that hold the instance that is being created. When creating an object, the method that is gonna be called with that object is gonna be the __init__ method and nothing else. If you need to call another method from that Class, you must specify the name of the method when using the object. For instance: object.method()
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path) # 
    
    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        # Invoking the init method to gain access to the DB
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        # Invoking the init method to gain access to the DB
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == "__main__":
    while True:
        event = Event() # Creat an Event Object
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            # Creating the DB Object and sending the database_path="data.db" parameter to the init class
            database = Database(database_path="data.db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send(message="Hey, new event was found!")
        time.sleep(2)