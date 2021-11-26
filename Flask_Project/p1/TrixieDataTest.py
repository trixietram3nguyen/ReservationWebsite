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

# Add new customer
# Check if the email customer enter for sign up already existed
result = customers.find({"email":"rtq.nguyen12@gmail.com"})
print(result)
# If yes -> print error and ask to enter new email
# Else no -> insert new customer info into the database
# result = customers.update({"email":"lungrob10@yahoomail.com"},{"$set":{"first_name":"Robber", "last_name":"Lunge", "email":"lungrob10@yahoomail.com", "pass":"Lungigi!"}},upsert=True)

#print(result)