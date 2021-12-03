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
email = "rtq.nguyen12@gmail.com"

query = customers.find({"email":"rtq.nguyen12@gmail.com"})
for result in query:
    profile = result

pf_firstName = profile['first_name']
pf_lastName = profile['last_name']
pf_email = profile['email']
pf_pass = profile['pass']
pf_mailingAdd = profile['mailing_address']
pf_billingAdd = profile['billing_address']
pf_card = profile['card']
pf_points = profile['points']
pf_diner = profile['preferred_diner']

print(pf_firstName + "\n")
print(pf_lastName + "\n")
print(pf_email + "\n")
print(pf_pass + "\n")
print(pf_mailingAdd + "\n")
print(pf_billingAdd + "\n")
print(pf_card + "\n")
print(pf_points + "\n")
print(pf_diner + "\n")