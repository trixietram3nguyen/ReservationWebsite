from flask import Flask, render_template, request, jsonify, url_for, flash, redirect

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("1st_Page.html")

@app.route("/test", methods = ["GET", "POST"])
def test():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       print(first_name + " " + last_name)
       return "Your name is "+first_name + last_name
    return render_template("test.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pname")
        #query database does username exist if it does go
        print(username + " " + password)
        return render_template("Register_Page.html")
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

@app.route("/register")
def register():
    return render_template("Register_Page.html")

@app.route("/signup")
def signup():
    return render_template("SIGN_UP.html")

@app.route("/unregister")
def unregister():
    return render_template("Unregister_Reserve_page.html")

if __name__ == '__main__':
    app.run()

