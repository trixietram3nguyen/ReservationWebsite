query = tables.count({"book_status.date":"11/29/2021"})
# print(query)
if query != 0:
    # If yes -> check the time picked has been reserved
    print("There are table(s) reserved with this date")
    query = tables.find({"book_status.date":"11/29/2021"},{"table_number":1,"table_size":1,"_id":0})
    
    for result in query:
        table_num.append(result['table_number'])
        table_size.append(result['table_size'])
    
    print(table_num)
    print(table_size)
    print(len(table_num))