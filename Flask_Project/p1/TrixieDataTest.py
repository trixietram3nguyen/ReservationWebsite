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

# Getting information of the customer for the profile page
first_name = "TTY"
last_name = "QQN"
email = "ttyqqn@gmail.com"
password = "ttnew!"
street = "12345 Miller House Dr"
city = "Houston"
state = "Texas"
zip = "73491"
phone = "2346956109"
payment = "credit"
points = 0

result = customers.insert({"first_name":first_name, "last_name":last_name, "email":email, "pass":password,
                            "mailing_address":{"street":street,"city":city,"state":state,"zip":zip},
                            "billing_address":{"street":street,"city":city,"state":state,"zip":zip},
                            "phone":phone,"preferred_pmt":payment,"points":0})