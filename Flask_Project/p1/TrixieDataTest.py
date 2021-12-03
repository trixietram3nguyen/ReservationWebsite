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
pf_phone = profile['phone']
pf_pmt = profile['preferred_pmt']
pf_points = profile['points']
pf_diner = profile['preferred_diner']

print(pf_firstName + "\n")
print(pf_lastName + "\n")
print(pf_email + "\n")
print(pf_pass + "\n")
print(pf_mailingAdd)
print(pf_mailingAdd['street'])
print(pf_mailingAdd['city'])
print(pf_mailingAdd['state'])
print(pf_mailingAdd['zip'])
print("\n")
print(pf_billingAdd)
print(pf_billingAdd['street'])
print(pf_billingAdd['city'])
print(pf_billingAdd['state'])
print(pf_billingAdd['zip'])
print("\n")
print(pf_phone)
print("\n")
print(pf_pmt)
print("\n")
print(pf_points)
print("\n")
print(pf_diner + "\n")