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

# Function to add reservation into database
def addReservation(insert_tb, date, time, confirmation, name, size, email, combine_tb):
    tables.update({"table_number":insert_tb},{"$push":{"book_status":{"date":date,"time":time,"confirmation":confirmation,"name":name,"party_size":size,"email":email,"combined_table":combine_tb}}})
    print("Reservation inserted!")

# info to book reservation
table = []
party_sz = 5
# print("THE FIRST TABLE LENGTH\n")
# print(len(table))
confirmation = id_generator()
print("The confirmation code: " + confirmation)
time = ["5:00pm","5:15pm","5:30pm","5:45pm"]
table = 2
date = "11/29/2021"
name = "TT"
email = "TW"
combined_tb = 0

# Test addReservation function
addReservation(table,date,time,confirmation,name,party_sz,email,combined_tb)

# Find if the date picked has been reserved
query = tables.count({"book_status.date":"11/19/2021"})
# print(query)
if query != 0:
    # If yes -> check the time picked has been reserved
    print("There are table(s) reserved with this date")
    query = tables.find({"book_status.date":"11/19/2021"},{"table_number":1,"table_size":1,"_id":0})
    
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
    # Find out what table should the reservation add into
    
# Function to find out the table number to add the reservation, return the table will be insert and combine
def tableInsert(size):
    print("This table will be reserve")
    table = [1,0]
    return table

result = tableInsert(7)
print("Insert table")
print(result[0])
print("Combine table")
print(result[1])



# 5 cases to book
if party_sz <= 4:
    print("table for 4 or less")
    print("can reserve any table")
elif party_sz <= 5:
    print("table for 5 or less")
    print("reserve table for 5 and up. table 1/2/7/8")
elif party_sz <= 7:
    print("table for 7 or less")
    print("reserve table for 7 and up. table 1/7")
else:
    print("Big party -> combine table")
    if party_sz > 8:
        print("table for 12 or less")
        print("reserve table for 12 people only 1+2/7+8")
    else:
        print("table for 8")
        print("reserve table for 8 and up. table 3+5/4+6/1+2/7+8")
# case 1: if party size is 4 or less use table any table but all available so automatically use 3
# case 2: if party size is 5 or less use table 1/2/7/8 but all available so automatically use 2
# case 3: if party size is 7 or less use table 1/7 but both available so automatically use 1
# case 4: if party size is 8 or less use table 3+5/4+6 but both available so automatically use 3+5
# case 5: if party size is 12 or less use table 1+2/7+8 but both available so automatically use 1+2
# Reservation successfully booked, email the confirmation


# Check table size to see which case we deal with
# 5 cases to book
# case 1: if party size is 4 or less use table any table but prioritize table for 4 first
# case 2: if party size is 5 or less use table 1/2/7/8 but all available so automatically use 2
# case 3: if party size is 7 or less use table 1/7 but both available so automatically use 1
# case 4: if party size is 8 or less use table 3+5/4+6 but both available so automatically use 3+5
# case 5: if party size is 12 or less use table 1+2/7+8 but both available so automatically use 1+2


