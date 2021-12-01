from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
import pymongo
#import json
from pymongo import MongoClient
#from bson import Binary, Code
#from bson.json_util import loads


app = Flask(__name__)


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
        size = request.form.get("psize")
        time = request.form.get("appt-time")
        print(date)
        print(size)
        print(time)
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
