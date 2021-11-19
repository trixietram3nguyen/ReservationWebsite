from flask import Flask, render_template, request, jsonify, url_for, flash, redirect

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
        return redirect("/confirm1", code=302)
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
        return redirect("/confirm2", code=302)
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
        print(fname + " " + lname + " " + email +
              " " + date + " " + size + " " + time)
        return redirect("/confirm3", code=302)
    return render_template("Unregister_Reserve_page.html")


if __name__ == '__main__':
    app.run()
