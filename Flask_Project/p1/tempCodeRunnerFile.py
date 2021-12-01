if (best_table[1] == 0):
    #     # Yes -> Check if best_table[0] is 0
    #     if (best_table[0] == 0):
    #         # Yes -> No more table to reserve
    #         print("Please pick another time/date.")
    #     else:
    #         # No -> There are table to reserve
    #         # Call the addReservation function once
    #         print("Add reservation for table " + str(best_table[0]))
    #         # Reserving the table
    #         addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
    # else:
    #     # No -> Table need to be combine
    #     # Call the addReservation function twice, flip the table insert and table combine for the second call
    #     print("Add reservation for table " + str(best_table[0]))
    #     # Reserving the table
    #     addReservation(best_table[0], date, time, confirmation, name, party_size, email, best_table[1])
    #     # Reserving the table
    #     print("Add reservation for table " + str(best_table[1]))
    #     addReservation(best_table[1], date, time, confirmation, name, party_size, email, best_table[0])