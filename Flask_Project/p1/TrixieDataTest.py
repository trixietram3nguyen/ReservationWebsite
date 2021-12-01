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
def tableInsert(tb_num, tb_size, party_sz,pairs):
    # print("Length")
    # print(len(tb_size))
    #array of table, table[0] is the insert table, table[1] is combine table
    tb_insert = [0,0]
    available = []
    
    if party_sz >= 8:
        print("Need table for 8-12")
        # tb_insert[0] = 0
        # tb_insert[1] = 1
        print(pairs)

        # loop to find what tables are available to combine
        for p in pairs:
            if (p[0] in tb_num and p[1] in tb_num):
                print("Adding to available")
                print(p[0])
                print(p[1])
                available.append([p[0],p[1],p[2]])
        print(available)

        if len(available) == 0:
            # If there is nothing added in available, meaning no table are able to combine
            print("No tables can be combine at this time")
            print("There are no available for party size you choose")
            tb_insert[0] = 0
            tb_insert[1] = 0
        else:
            # There are tables available to combine
            # loop through the pairs list to find the pair of tables that can accommondate the desired size
            index = 0
            print(available[index][2])
            print(party_sz)
            while (party_sz > available[index][2]):
                index += 1
                print("INDEX2")
                print(index)
                if (index == len(available)):
                    break
            
            # then take in that index
            # check to see if there is table still available
            if index >= len(available):
                # index out of range no more table for that party size
                print("There are no available for party size you choose")
                tb_insert[0] = 0
            else:
                # table still available for that party size
                # use that index to get the insert table number and combine table number
                print("INDEX")
                print(index)
                tb_insert[0] = available[index][0]
                tb_insert[1] = available[index][1]
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
time = ["5:30pm","5:45pm","6:00pm","6:15pm"]
date = "11/28/2021"
name = "TT"
email = "TW"
combined_tb = 0
# pairs to store the tables that can be combine and the size of it [0],[1] tables number, [2] combined size
pairs = [[3,5,8],[4,6,8],[1,2,12],[7,8,12]]

# Test addReservation function
# addReservation(table,date,time,confirmation,name,party_sz,email,combined_tb)

# New algorithm
# Check if date picked has been reserve
query = tables.count({"book_status.date":date})
# print(query)
if query != 0:
    # Yes -> Check if time picked has been reserve
    print("There are some reservations booked with this date. Check for time!")
    time_booked = 0
    for t in time:
        #print(t)
        query = tables.count({"book_status.time":t})
        #print(query)
        time_booked += query
    print(time_booked)

    if (time_booked != 0):
        print("Check for available tables during this time!")
        # Yes -> Check if there still tables available
        # Check if there are still tables that does not have that date reserve
        # query = tables.count({"book_status.date":{"$ne":date}})
        # if query != 0:
        #     # Yes -> Find the table(s) that don't have that date reserve
        #     print("There are still available table on " + date)
        #     query = tables.find({"book_status.date":{"$ne":date}},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
        #     for result in query:
        #     #print(result)
        #         table_num.append(result['table_number'])
        #         table_size.append(result['table_size'])
            
        #     print("Print out the list of tables")
        #     print(table_num)
        #     print(table_size)
        # else:
        # No -> Retrieve all the table info and check with date and time so see if anything available
        all_tb = []
        tb_info = []
        print("All tables have reservations on " + date + " and " + time[0])
        query = tables.find({},{"table_number":1,"table_size":1,"book_status.date":1,"book_status.time":1,"_id":0}).sort("table_size")
        for result in query:
            #print(result)
            #print(type(result))
            all_tb.append(result)
        
        # #print(type(all_tb))
        # tb_info = all_tb[0]
        # #print(tb_info)
        # #print(type(tb_info))
        # status = tb_info['book_status']
        # #print(type(status))
        # #print(type(status[0]))
        # reserved = status[0]
        # #print(type(reserved))
        # print(type(reserved['date']))

        # Get the list of available tables
        for table_info in all_tb:
            table_number = table_info['table_number']
            table_sz = table_info['table_size']
            status = table_info['book_status']
            # print(tb_info)
            # print("I'M HERE!!!!!\n")
            # status = tb_info['book_status']
            print(table_number)
            print(table_sz)
            print(status)
            date_available = True
            time_available = True
            for s in status:
                reserved_time = s['time']
                reserved_date = s['date']
                print(reserved_date)
                print(reserved_time)
                
                if date == reserved_date:
                    # That table has the same date reserve so check the time
                    for t in time:
                        if t in reserved_time:
                            time_available = False
                            date_available = False
                            break
                
            if time_available or date_available:
                # That table is available to reserve
                # Add to table_num and table_size list
                if table_number not in table_num:
                    table_num.append(table_number)
                    table_size.append(table_sz)
                    #     print("Print out the list of tables")
                    #     print(table_num)
                    #     print(table_size)
                    #     print("I'M HERE^^^^^^^^^\n")
                    # else:
                    #     print("No more availability. Pick another time/date.")
                    # That table is available to reserve
                    # Add to table_num and table_size list
                    # if table_number not in table_num:
                    #     table_num.append(table_number)
                    #     table_size.append(table_sz)
                    # print("Print out the list of tables")
                    # print(table_num)
                    # print(table_size)
                    # print("I'M HERE********\n")
        print("Print out the list of tables")
        print(table_num)
        print(table_size)
        print("I'M HERE^^^^^^^^^\n")
    else:
        # No -> Make the reservations, insert into database
        print("This time is available to book!")
        print("Making reservation...")
        # No time in the array were book at all, so we can choose anytime from the array to retrieve the available tables
        query = tables.find({"book_status.date":{"$ne":time[0]}},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
        for result in query:
        #print(result)
            table_num.append(result['table_number'])
            table_size.append(result['table_size'])
        
        print("Print out the list of tables")
        print(table_num)
        print(table_size)
else:
    # No -> Find the available tables
    print("This reservation can be book")
    query = tables.find({"book_status.date":{"$ne":date}},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
    for result in query:
        #print(result)
        table_num.append(result['table_number'])
        table_size.append(result['table_size'])
        
    print("Print out the list of tables")
    print(table_num)
    print(table_size)

if len(table_num) == 0:
    print("No more availability. Pick another time/date.")
else:
    # Find out what table best fit for the party size
    best_table = tableInsert(table_num, table_size, party_size, pairs)
    print("The table will be reserve is")
    print(best_table)

    # If best_table[1] is 0 -> table will need to be combine or non of the table can be reserve
    if (best_table[1] == 0):
        # Yes -> Check if best_table[0] is 0
        if (best_table[0] == 0):
            # Yes -> No more table to reserve
            print("Please pick another time/date.")
        else:
            # No -> There are table to reserve
            # Call the addReservation function once
            print("Add reservation for table " + str(best_table[0]))
            # Reserving the table
            addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
    else:
        # No -> Table need to be combine
        # Call the addReservation function twice, flip the table insert and table combine for the second call
        print("Add reservation for table " + str(best_table[0]))
        # Reserving the table
        addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
        # Reserving the table
        print("Add reservation for table " + str(best_table[1]))
        addReservation(best_table[1], date, time, confirmation, name, party_size, email, best_table[0])





# New algorithm
# query = tables.find({"book_status.date":"11/29/2021"},{"book_status.date":1,"book_status.time":1,"_id":0})
# for i in query:
#     print("PRINT...........")
#     print(i)
#     checking.append(i)

# print("CHECKING CHECKING")
# print(checking[0])
# checking2 = checking[0]
# book_status = checking2['book_status']
# print("CHECKING 22222")
# print(book_status)
# date = book_status[0]
# print("CHECKING 3333333")
# print(date['time'])
# # Find if the date picked has been reserved
# # Count the tables that don't have picked date and time reserved
# query = tables.count({"$or":[{"book_status.date":{"$ne":"11/29/2021"}},{"book_status.time":{"$ne":"6:00pm"}}]})

# if query == 0:
#     # 0 -> no more available table to book reservation -> customer has to pick another time and date
#     print("No more available tables, please pick another date/time!")
# else:
#     # > 0 -> find out what table(s) available
#     print("There are some table(s) available to book now.")
#     query = tables.find({"$or":[{"book_status.date":{"$ne":"11/29/2021"}},{"book_status.time":{"$ne":"6:00pm"}}]},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
#     # print(query)
#     for result in query:
#         #print(result)
#         table_num.append(result['table_number'])
#         table_size.append(result['table_size'])
        
#     print("Print out the list of tables")
#     print(table_num)
#     print(table_size)
#     # Find out what table best fit for the party size
#     best_table = tableInsert(table_num, table_size, party_size)
#     print("The table will be reserve is")
#     print(best_table)
#     # Check to see if table still available to reserve for the particular party size
#     if(best_table[0] == 0):
#         # No more availabilty for the chosen party size
#         print("NO MORE TABLE! Pick another size/time/date.")
#     else:
#         # Make reservation -> Insert reserve info into database
#         # insert table is best_table[0], combined table is best_table[1]
#         addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
#         print("The confirmation code: " + confirmation)











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


