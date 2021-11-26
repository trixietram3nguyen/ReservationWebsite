import pymongo
from pymongo import MongoClient

# To connect with the database
client = MongoClient("mongodb+srv://rtqnguyen12:Trixie1237@cluster0.jqrjj.mongodb.net/customers?retryWrites=true&w=majority")
# To use reservations database
db = client.reservations
# To use the tables collections
tables = db.tables
# To use the customers collections
customers = db.customers

# Making a reservations
# Need to generate random string with letters and numbers for the confirmation code
import string
import random

# function to generate confirmation code
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# info to book reservation
confirmation = id_generator()

# Find if the date picked has been reserved
    # If yes -> check the time picked has been reserved
        # If yes -> check what table(s) that reserved for chosen date and time
            # If all tables reserved with the chosen time and date
                # Promt choose different reservation time or date or both
            # If not all tables reserved with the chosen time and date
                # Book the reservation with available tables -> Insert the reservation into the database
                # Reservation successfully booked, email the confirmation
        # If no -> book the reservation -> insert the reservation into the data
        # Reservation successfully booked, email the confirmation
    # If no -> book the reservations -> insert the reservation into the database
    # Reservation successfully booked, email the confirmation
