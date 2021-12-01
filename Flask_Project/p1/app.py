from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
import pymongo
#import json
from pymongo import MongoClient
#from bson import Binary, Code
#from bson.json_util import loads


app = Flask(__name__)
current_user = ""

@app.route("/home")
def home():
    return render_template("1st_Page.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       print(first_name + " " + last_name)
       return "Your name is "+first_name + last_name
    return render_template("test.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pname")
        #query database does username exist if it does go
        print(username + " " + password)
        # Check Sign-In
        # check if email is valid (meaning available in the system)
        query = customers.count({"email":username})  #count the info in the database
        if query != 0:
            # if yes -> check password
            query = customers.find({"email":username},{"pass":1,"_id":0})

            for result in query:
                db_password = result['pass']
            
            if password == db_password:
                # if password match -> proceed to log in
                print("...Logging in")
                global current_user
                current_user=username
                print(current_user)
                return redirect("/register", code=302)
            else:
                # else promt incorrect password
                print("Incorrect password!")
                return redirect("/loginpass", code=302)
        else:
            # else no -> promt user not valid
            print("Incorrect email!")
            return redirect("/loginemail", code=302)
        
    return render_template("LOGGIN_PAGE.html")

@app.route("/loginpass", methods=["GET", "POST"])
def loginpass():
    if request.method == "POST":
        username = request.form.get("uname")
        
        password = request.form.get("pname")
        #query database does username exist if it does go
        print(username + " " + password)
        # Check Sign-In
        # check if email is valid (meaning available in the system)
        query = customers.count({"email":username})  #count the info in the database
        if query != 0:
            # if yes -> check password
            query = customers.find({"email":username},{"pass":1,"_id":0})

            for result in query:
                db_password = result['pass']
            
            if password == db_password:
                # if password match -> proceed to log in
                print("...Logging in")
                global current_user
                current_user=username
                print(current_user)
                return redirect("/register", code=302)
            else:
                # else promt incorrect password
                print("Incorrect password!")
                return redirect("/loginpass", code=302)
        else:
            # else no -> promt user not valid
            print("Incorrect email!")
            return redirect("/loginemail", code=302)
        
    return render_template("LOGGIN_PAGE_PASSWORD.html")

@app.route("/loginemail", methods=["GET", "POST"])
def loginemail():
    if request.method == "POST":
        username = request.form.get("uname")
        
        password = request.form.get("pname")
        #query database does username exist if it does go
        print(username + " " + password)
        # Check Sign-In
        # check if email is valid (meaning available in the system)
        query = customers.count({"email":username})  #count the info in the database
        if query != 0:
            # if yes -> check password
            query = customers.find({"email":username},{"pass":1,"_id":0})

            for result in query:
                db_password = result['pass']
            
            if password == db_password:
                # if password match -> proceed to log in
                print("...Logging in")
                global current_user
                current_user=username
                print(current_user)
                return redirect("/register", code=302)
            else:
                # else promt incorrect password
                print("Incorrect password!")
                return redirect("/loginpass", code=302)
        else:
            # else no -> promt user not valid
            print("Incorrect email!")
            return redirect("/loginemail", code=302)
        
    return render_template("LOGGIN_PAGE_EMAIL.html")



@app.route("/confirm1")
def confirm1():
    return render_template("CONFIRM_RESERVE_REGISTER.html")


@app.route("/confirm2")
def confirm2():
    return render_template("CONFIRM_RESERVE_UNREGISTER_PAGE_2.html")


@app.route("/confirm3")
def confirm3():
    return render_template("CONFIRM_RESERVE_UNREGISTER.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        date = request.form.get("rdate")
        print(date)
        date_year= date[0:4]
        date_month= date[5:7]
        date_day= date[8:10]
        date=date_month+"/"+date_day+"/"+date_year
        print(date)
        size = int(request.form.get("psize"))
        print(type(size))
        time_input = request.form.get("appt-time")
        print(time_input)
        time_hour = int(time_input[0:2]) - 12
        time_minute = time_input[3:5]
        time_input = str(time_hour)+":"+time_minute+"pm"
        print(time_input)
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
            # print("Reservation inserted!")

        # Function to find out the table number to add the reservation, return the table will be insert and combine
        def tableInsert(tb_num, tb_size, party_sz,pairs):
            #table[0] is the insert table, table[1] is combine table
            tb_insert = [0,0]
            #list to store which table can be combine
            available = []
            
            # Check the party size to see if table will need to be combine
            if party_sz >= 8:
                # table of 8 or up -> need to be combine
                print("\nNeed table for 8-12")

                # loop to find what tables are available to combine
                for p in pairs:
                    if (p[0] in tb_num and p[1] in tb_num):
                        available.append([p[0],p[1],p[2]])
                print("\nTables that available to combine are: ")
                print(available)

                # Check to see if length of available list is equal to 0
                if len(available) == 0:
                    # Yes -> No table are able to combine
                    print("\nNo tables can be combine at this time. No available for party size you choose")
                    tb_insert[0] = 0
                    tb_insert[1] = 0
                else:
                    # There are tables available to combine
                    # loop through the pairs list to find the pair of tables that can accommondate the desired size
                    index = 0
                    # Go through the list as if party size are bigger than the size of the one inside the list
                    # Keep going until find one or until reach the end of the list
                    while (party_sz > available[index][2]):
                        index += 1
                        # if index is equal to the length of the list -> the end of the list -> break out the loop
                        if (index == len(available)):
                            break
                    
                    # then take in that index
                    # check to see if there is table still available
                    if index < len(available):
                        # table still available for that party size
                        # use that index to get the insert table number and combine table number
                        tb_insert[0] = available[index][0]
                        tb_insert[1] = available[index][1]
            else:
                # party size less than 8, no table need to be combine, so tb_insert[1] will be 0 always
                tb_insert[1] = 0
                
                # loop through the table size array until find a table size that is >= party size
                index = 0
                while (party_sz > tb_size[index]):
                    index += 1
                    # if index is equal to the length of the list -> the end of the list -> break out the loop
                    if (index == len(tb_size)):
                        break
                    
                
                # then take in that index
                # check to see if there is table still available
                if index < len(tb_size):
                    # table still available for that party size
                    # use that index to get the table number, then store in tb_insert[0]
                    tb_insert[0] = tb_num[index]
            
            return tb_insert



        # info to book reservation
        table_num = []     #store the available table(s) to reserve
        table_size = []    #store the side of the table(s) accordingly
        party_size = size
        time = [] #list of time that need to be reserve
        start = time_list.index(time_input)    
        print(start)
        if  party_size < 5:
            for i in range(4):
                if start+i < len(time_list):
                    time.append(time_list[start+i]) 
        elif party_size < 8:
            for i in range(5):
                if start+i < len(time_list):
                    time.append(time_list[start+i]) 
        else:
            for i in range(6):
               if start+i < len(time_list):
                    time.append(time_list[start+i])
        print(time)

        confirmation = id_generator()    #random confirmation generated
        global current_user
        email = current_user
        print(email)
        name = "TT" #Add database query Trixie

        # pairs to store the tables that can be combine and the size of it [0],[1] tables number, [2] combined size
        pairs = [[3,5,8],[4,6,8],[1,2,12],[7,8,12]]

        # First, find out the list of table(s) that is available
        # Check if date picked has been reserved
        query = tables.count({"book_status.date":date})
        if query != 0:
            # Yes -> Check if time picked has been reserve
            # print("\nThere are some reservations booked with this date. Check for time!")
            time_booked = 0
            for t in time:
                query = tables.count({"book_status.time":t})
                time_booked += query
            print(time_booked)

            # check if time picked is reserved in the system
            if (time_booked != 0):
                # time_booked not equal 0 -> the picked time is already in the system
                # print("\nCheck for available tables during this time!")
                all_tb = []
                tb_info = []
                query = tables.find({},{"table_number":1,"table_size":1,"book_status.date":1,"book_status.time":1,"_id":0}).sort("table_size")
                for result in query:
                    all_tb.append(result)

                # Get the list of available tables
                for table_info in all_tb:
                    table_number = table_info['table_number']
                    table_sz = table_info['table_size']
                    status = table_info['book_status']
                    date_available = True
                    time_available = True
                    for s in status:
                        reserved_time = s['time']
                        reserved_date = s['date']
                        
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
                        
                print("\nPrint out the list of tables")
                print(table_num)
            else:
                # No -> Make the reservations, insert into database
                # print("\nThis time is available to book!")
                # No time in the array were book at all, so we can choose anytime from the array to retrieve the available tables
                query = tables.find({"book_status.date":{"$ne":time[0]}},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
                for result in query:
                    table_num.append(result['table_number'])
                    table_size.append(result['table_size'])
                
                print("\nPrint out the list of tables")
                print(table_num)
        else:
            # No -> Find the available tables
            # print("\nThis date is available to book")
            query = tables.find({"book_status.date":{"$ne":date}},{"table_number":1,"table_size":1,"_id":0}).sort("table_size")
            for result in query:
                table_num.append(result['table_number'])
                table_size.append(result['table_size'])
                
            print("\nPrint out the list of available table(s)")
            print(table_num)
            # print(table_size)

        # Then start making the reservation
        # If there is nothing in table_num list -> no table available
        if len(table_num) == 0:
            print("\nNo more availability. Pick another time/date.")
            #add confirmation redirect page here
            return redirect("/register", code=302)
        else:
            # Find out what table best fit for the party size
            best_table = tableInsert(table_num, table_size, party_size, pairs)
            print("\nThe table will be reserve is " + str(best_table[0]) + " and " + str(best_table[1]))

            # Make the reservation
            # If best_table[1] is 0 -> table will need to be combine or non of the table can be reserve
            if (best_table[1] == 0):
                # Yes -> No table need to be combine
                # Check if best_table[0] is 0
                if (best_table[0] == 0):
                    # Yes -> No more table to reserve
                    print("\nNo more table is available to reserve. Please pick another time/date.")
                else:
                    # No -> There are table to reserve
                    # Call the addReservation function once
                    print("\nAdd reservation for table " + str(best_table[0]))
                    # Reserving the table
                    addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
            else:
                # No -> Table need to be combine
                # Call the addReservation function twice, flip the table insert and table combine for the second call
                print("\nAdd reservation for table " + str(best_table[0]))
                # Reserving the table
                addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
                # Reserving the table
                print("\nAdd reservation for table " + str(best_table[1]))
                addReservation(best_table[1], date, time, confirmation, name, party_size, email, best_table[0])
        return redirect("/TIMEregister", code=302)





        
    return render_template("Register_Page.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        pass1 = request.form.get("pword1")
        query = customers.count({"email":email})  #count the info in the database
        if query != 0:
            # If yes (meaning there is 0 number of that info in the database) -> print error and ask to enter new email
             # print("There is " + str(query) + " result found. ")
            print("Enter another email")
            return redirect("/signup1", code=302)
        else:
            # Else no -> insert new customer info into the database
            # result = customers.update({"email":"lungrob10@yahoomail.com"},{"$set":{"first_name":"Robber", "last_name":"Lunge", "email":"lungrob10@yahoomail.com", "pass":"Lungigi!"}},upsert=True)
            result = customers.insert({"first_name":fname, "last_name":lname, "email":email, "pass":pass1})
            print("New customer inserted")
            return redirect("/signup_conf", code=302)
    return render_template("SIGN_UP.html")

@app.route("/signup_conf", methods=["GET", "POST"])
def signup_conf():
    

    return render_template("SIGN_UP_CONFIRM.html"), {"Refresh": "5; /login"}

@app.route("/signup1", methods=["GET", "POST"])
def signup1():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        pass1 = request.form.get("pword1")
        query = customers.count({"email":email})  #count the info in the database
        if query != 0:
            # If yes (meaning there is 0 number of that info in the database) -> print error and ask to enter new email
             # print("There is " + str(query) + " result found. ")
            print("Enter another email")
            return redirect("/signup1", code=302)
        else:
            # Else no -> insert new customer info into the database
            # result = customers.update({"email":"lungrob10@yahoomail.com"},{"$set":{"first_name":"Robber", "last_name":"Lunge", "email":"lungrob10@yahoomail.com", "pass":"Lungigi!"}},upsert=True)
            result = customers.insert({"first_name":fname, "last_name":lname, "email":email, "pass":pass1})
            print("New customer inserted")
            return redirect("/signup_conf", code=302)
    return render_template("SIGN_UP_NEW_PASSWORD.html")

@app.route("/unregister", methods=["GET", "POST"])
def unregister():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        date = request.form.get("date")
        size = request.form.get("size")
        time = request.form.get("appt-time")
        print(fname)
        print(lname)
        print(email)
        print(date)
        print(size)
        print(time)

        return redirect("/TIMEunregister", code=302)
    return render_template("Unregister_Reserve_page.html")

@app.route("/TIMEregister", methods=["GET", "POST"])
def TIMEregister():
    if request.method == "POST":
        hour = request.form.get("rhour")
        minutes = request.form.get("rminutes")
        print(hour + " " + minutes)
        return redirect("/confirm1", code=302)
    return render_template("TIME (REGISTER).html")

@app.route("/TIMEunregister", methods=["GET", "POST"])
def TIMEunregister():
    if request.method == "POST":
        hour = request.form.get("rhour")
        minutes = request.form.get("rminutes")
        print(hour + " " + minutes)
        return redirect("/confirm3", code=302)
    return render_template("TIME(UNREGISTER).html")


@app.route("/ACCOUNT")
def ACCOUNT():
    return render_template("ACCOUNT INFO.html")

#------------------------------------------Time Logics------------------------------------------------
time_list = ["5:00pm", "5:15pm", "5:30pm", "5:45pm", "6:00pm", "6:15pm", "6:30pm", "6:45pm", "7:00pm", "7:15pm", "7:30pm", "7:45pm", "8:00pm", "8:15pm", "8:30pm", "8:45pm", "9:00pm", "9:15pm", "9:30pm", "9:45pm", "10:00pm", "10:15pm", "10:30pm", "10:45pm", "11:00pm" ]
#------------------------------------------This part from here to------------------------------------------------
 
# To connect with the database
client = MongoClient("mongodb+srv://rtqnguyen12:Trixie1237@cluster0.jqrjj.mongodb.net/customers?retryWrites=true&w=majority")
# To use reservations database
db = client.reservations
# To use the tables collections
tables = db.tables
customers = db.customers


#-------------------------------------------here is my connection database stuff, so don't delete it------------


if __name__ == '__main__':
    app.run()
