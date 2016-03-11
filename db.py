from dbConnect import *
import time

start_time = time.time()

SCHEMA = "AirlineTrackingSystem"

filesToRead = [
    "sql/_CREATE_TABLE.sql",

    "sql/country.sql",
    "sql/airport.sql",
    "sql/airline.sql",

    "sql/flight.sql",
    "sql/airVehicle.sql",
    "sql/fliesOn.sql",
    "sql/status.sql",
    "sql/flightStatus.sql",
]

connection = db_connect()

# Dropping the whole schema for testing purposes
# cursor = connection.cursor()
# cursor.execute("DROP SCHEMA IF EXISTS \"" + SCHEMA + "\" CASCADE")
# connection.commit()
# cursor.close()

total_text = ""
total_counter = 0
for file in filesToRead:
    cursor = connection.cursor()
    counter = 0

    cursor.execute("SET search_path = \"" + SCHEMA + "\", pg_catalog;")
    connection.commit()

    query = ""
    for row in open(file, "r", encoding='utf8'):
        row = row.replace("\n", "")
        if row == "" or row.startswith("# ") or row.startswith("--"):
            continue

        query += row

        if row.endswith(";"):
            query = query.replace("\n", " ")
            print("%s: %s" % (counter, query))
            cursor.execute(query)
            query = ""
            counter += 1

    connection.commit()
    cursor.close()

    total_counter += counter
    text = "Operations in '" + str(file) + "': " + str(counter) + "\n"
    total_text += text
    print(text)
    counter = 0

connection.close()

print("==========================")
print(total_text)
print("Total operations: " + str(total_counter))
end_time = time.time()
print("Total time: %.2f mins" % ((end_time - start_time)/60))
