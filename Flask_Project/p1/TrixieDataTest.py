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
table = []
# print("THE FIRST TABLE LENGTH\n")
# print(len(table))
confirmation = id_generator()
print("The confirmation code: " + confirmation)

# Find if the date picked has been reserved
query = tables.count({"book_status.date":"11/20/2021"})
# print(query)
if query != 0:
    # If yes -> check the time picked has been reserved
    print("There are table(s) reserved with this date")
    query = tables.find({"book_status.date":"11/20/2021"},{"table_number":1,"_id":0})
    
    for result in query:
        table.append(result['table_number'])
    
    print(table)
    print(len(table))
        # If yes -> check what table(s) that reserved for chosen date and time
            # If all tables reserved with the chosen time and date
                # Promt choose different reservation time or date or both
            # If not all tables reserved with the chosen time and date
                # Book the reservation with available tables -> Insert the reservation into the database
                # Reservation successfully booked, email the confirmation
        # If no -> book the reservation -> insert the reservation into the data
        # Reservation successfully booked, email the confirmation
else:
    # If no -> book the reservations -> insert the reservation into the database
    print("This date can be reserve now")
    # Check the table size before booking
    # 5 cases to book
    # case 1: if party size is 4 or less use table any table but all available so automatically use 3
    # case 2: if party size is 5 or less use table 1/2/7/8 but all available so automatically use 2
    # case 3: if party size is 7 or less use table 1/7 but both available so automatically use 1
    # case 4: if party size is 8 or less use table 3+5/4+6 but both available so automatically use 3+5
    # case 5: if party size is 12 or less use table 1+2/7+8 but both available so automatically use 1+2
    # Reservation successfully booked, email the confirmation
