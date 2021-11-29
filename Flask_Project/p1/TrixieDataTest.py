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

# Function to find out the table number to add the reservation, return the table will be insert and combine
def tableInsert(tb_num, tb_size, party_sz):
    print("Length")
    print(len(tb_size))
    #array of table, table[0] is the insert table, table[1] is combine table
    tb_insert = [0,0]
    
    if party_sz >= 8:
        tb_insert[0] = 1
        tb_insert[1] = 0
        print(tb_insert[1])
    else:
        # party size less than 8, no table need to be combine, so tb_insert[1] will be 0 always
        tb_insert[1] = 0
        
        # loop through the table size array until find a table size that is >= party size
        index = 0
        while (party_sz > tb_size[index]):
            index += 1
            print("INDEX2")
            print(index)
            if (index == len(tb_size)):
                break
            
        
        # then take in that index
        # check to see if there is table still available
        if index >= len(tb_size):
            # index out of range no more table for that party size
            print("There are no available for party size you choose")
            tb_insert[0] = 0
        else:
            # table still available for that party size
            # use that index to get the table number, then store in tb_insert[0]
            tb_insert[0] = tb_num[index]
    
    print("This table will be reserve")
    print(tb_insert)
    return tb_insert

# result = tableInsert(7)
# print("Insert table")
# print(result[0])
# print("Combine table")
# print(result[1])

# info to book reservation
table_num = []
table_size = []
party_size = 5
# print("THE FIRST TABLE LENGTH\n")
# print(len(table))
confirmation = id_generator()
time = ["5:00pm","5:15pm","5:30pm","5:45pm"]
date = "11/29/2021"
name = "TT"
email = "TW"
combined_tb = 0

# Test addReservation function
# addReservation(table,date,time,confirmation,name,party_sz,email,combined_tb)

# New algorithm
# Find if the date picked has been reserved
# Count the tables that don't have picked date and time reserved
query = tables.count({"$or":[{"book_status.date":{"$ne":"11/29/2021"}},{"book_status.time":{"$ne":"6:00pm"}}]})

if query == 0:
    # 0 -> no more available table to book reservation -> customer has to pick another time and date
    print("No more available tables, please pick another date/time!")
else:
    # > 0 -> find out what table(s) available
    print("There are some table(s) available to book now.")
    query = tables.find({"$or":[{"book_status.date":{"$ne":"11/29/2021"}},{"book_status.time":{"$ne":"6:00pm"}}]},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
    # print(query)
    for result in query:
        #print(result)
        table_num.append(result['table_number'])
        table_size.append(result['table_size'])
        
    print("Print out the list of tables")
    print(table_num)
    print(table_size)
    # Find out what table best fit for the party size
    best_table = tableInsert(table_num, table_size, party_size)
    print("The table will be reserve is")
    print(best_table)
    # Check to see if table still available to reserve for the particular party size
    if(best_table[0] == 0):
        # No more availabilty for the chosen party size
        print("NO MORE TABLE! Pick another size/time/date.")
    else:
        # Make reservation -> Insert reserve info into database
        # insert table is best_table[0], combined table is best_table[1]
        addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
        print("The confirmation code: " + confirmation)











# # Find if the date picked has been reserved
# # Count the tables that don't have the picked date reserve
# query = tables.count({"book_status.date":"11/28/2021"})
# # print(query)
# # If count == 0 then there is no tables to reserve, pick another day
# if query != 0:
#     # If yes -> check the time picked has been reserved
#     print("There are table(s) reserved with this date")
#     query = tables.find({"book_status.date":{"$ne":"11/28/2021"}},{"table_number":1,"table_size":1,"_id":0})
    
#     for result in query:
#         table_num.append(result['table_number'])
#         table_size.append(result['table_size'])
    
#     print(table_num)
#     print(table_size)
#     print(len(table_num))
#         # If yes -> check what table(s) that reserved for chosen date and time
#             # If all tables reserved with the chosen time and date
#                 # Promt choose different reservation time or date or both
#             # If not all tables reserved with the chosen time and date
#                 # Book the reservation with available tables -> Insert the reservation into the database
#                 # Reservation successfully booked, email the confirmation
#         # If no -> book the reservation -> insert the reservation into the data
#         # Reservation successfully booked, email the confirmation
# else:
#     # If no -> book the reservations -> insert the reservation into the database
#     print("This date can be reserve now")
#     # Find out what table should the reservation add into



# 5 cases to book
# if party_sz <= 4:
#     print("table for 4 or less")
#     print("can reserve any table")
# elif party_sz <= 5:
#     print("table for 5 or less")
#     print("reserve table for 5 and up. table 1/2/7/8")
# elif party_sz <= 7:
#     print("table for 7 or less")
#     print("reserve table for 7 and up. table 1/7")
# else:
#     print("Big party -> combine table")
#     if party_sz > 8:
#         print("table for 12 or less")
#         print("reserve table for 12 people only 1+2/7+8")
#     else:
#         print("table for 8")
#         print("reserve table for 8 and up. table 3+5/4+6/1+2/7+8")
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


