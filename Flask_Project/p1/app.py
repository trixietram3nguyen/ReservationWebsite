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
        return redirect("/register", code=302)
    return render_template("LOGGIN_PAGE.html")


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
        pass2 = request.form.get("pword2")
        print(fname + " " + lname + " " + email + " " + pass1 + " " + pass2)
        return redirect("/login", code=302)
    return render_template("SIGN_UP.html")


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

# client = MongoClient("mongodb+srv://rtqnguyen12:Trixie1237@cluster0.jqrjj.mongodb.net/customers?retryWrites=true&w=majority")
# db=client.reservations
# table_collection = db.tables

# # test = {"_id":12312312312, "name": "Tuan"}
# # collection.insert_one(test)
# result = table_collection.find({"book_status.date" : "11/18/2021"})
# all = table_collection.find({"table_number":1})
# # print(result.next()["table_number"])
# # print(result[0].book_status[0].time_booked[0].name)
# #print(loads(json(result.next())))
# # print(json.loads(bson.json_util.dumps(data)))

# for info in all:
#     table = info
    
# date = table['book_status']
# print(type(date))
# print(date[0])

# print("hello")
# print(type(date[0]))

# print("more")
# status = date[0]
# print(type(status))
# print(status['time_booked'])

# time_booked = status['time_booked']
# print("blah blah blah")
# print(type(time_booked[0]))
# print(time_booked[0])

# name = time_booked[0]['name']
# print("the name")
# print(name)

# #print(type(all))

# # if (table['table_position'] == "inside"):
# #     print(table['table_position'])
# # else:
# #     print("Error")

#-------------------------------------------here is my connection database stuff, so don't delete it------------


if __name__ == '__main__':
    app.run()
