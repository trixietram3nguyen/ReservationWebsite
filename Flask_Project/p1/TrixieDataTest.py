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

# Get customer name from email
query = customers.find({"email":"rtq.nguyen12@gmail.com"},{"first_name":1,"last_name":1,"_id":0})
for result in query:
    print(result)

name = result['first_name'] + " " + result['last_name']
print(name)
