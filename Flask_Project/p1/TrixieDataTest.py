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

# Update profile info
# update customer info base on their email since there is only 1 email for each profile
email = "tx3rry@hotmail.com"
points = 0
preferred_diner = "2"
card_num = "1234567890987654"
exp_date = "09/24"
cvv = "945"
preferred_card = "yes"
mail_street = "19678 Magnolia Ln"
mail_city = "Houston"
mail_state = "texas"
mail_zip = "77088"
billing = True          #default billing to be same as mailling address

# check if billing address is the same as mailing address
if billing:
    print("Same, use mailing address")
else:
    print("Set new billing address")

