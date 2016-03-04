from IOgenerate import *

sourceFlight = "data/routes.dat"
outputFlight = "sql/flight.sql"
outputAirVehicle = "sql/airVehicle.sql"
outputFliesOn = "sql/fliesOn.sql"
outputStatus = "sql/status.sql"
outputFlightStatus = "sql/flightStatus.sql"

# Start values for IDs
flightId = 1
airVehicleId = 1
fliesOnId = 1
statusId = 1
flightStatusId = 1

flightSQL = []
airVehicleSQL = []
fliesOnSQL = []
statusSQL = []
flightStatusSQL = []

statuses = ['On Time',
            'Arrived',
            'Arriving',
            'Delayed',
            'Departed',
            'Departing',
            'Cancelled']

flightNOs = {}
planes = {}

routes = get_contents(sourceFlight)

for route in routes:

    # Skipping some routes that have \N in their rows.
    skip = False
    for el in route:
        if el == "\\N":
            skip = True
    # Ignoring empty AirlineId, FromAirportId, ToAirportId or other '\N's
    if skip or not route[3] or not route[5] or not route[1]:
        continue

    # Making sure there are no duplicates in flight numbers
    flightNO = ""
    while flightNO == "" or flightNO in flightNOs:
        flightNO = random_(randint(3, 5), string.digits)

    flightNOs[flightNO] = flightNO

    flightSQL.append(
        "INSERT INTO Flight (FlightId, FlightNo, AirlineId, " +
        "FromAirportId, ToAirportId, NumOfStops, WeekDays, " +
        "DepartureTime, ArrivalTime, Distance, Duration) VALUES (" +
        str(flightId) + ", " +                          # FlightId
        "'" + flightNO + "'" + ", " +                   # FlightNo
        route[1] + ", " +                               # AirlineId
        route[3] + ", " +                               # FromAirportId
        route[5] + ", " +                               # ToAirportId
        route[7] + ", " +                               # NumOfStops
        "'" + random_week_days(randint(1, 4)) + "', " + # WeekDays
        "'" + random_time() + "'" + ", " +              # DepartureTime
        "'" + random_time() + "'" + ", " +              # ArrivalTime
        random_(randint(2, 4), string.digits) + ", " +  # Distance
        "'" + random_time() + "'" +                     # Duration
        ");")

    planesList = route[8].split(" ")
    for plane in planesList:
        if not plane or plane == " ":
            continue

        if plane not in planes:
            planes[plane] = airVehicleId
            airVehicleId += 1

        fliesOnSQL.append(
            "INSERT INTO FliesOn(FlightAirVehicleId, FlightId, PlaneId) " +
            "VALUES (" +
            str(fliesOnId) + ", " +
            str(flightId) + ", " +
            str(planes[plane]) +
            ");")
        fliesOnId += 1

    # Making sure we don't generate statuses for every flight
    # rep = randint(0, 2)
    # rep = round(normalvariate(-1, 4))
    # rep = round(expovariate(7)*10)
    rep = round(normalvariate(-3, 4))
    if rep < 0:
        rep = 0
    i = 0
    while i < rep:
        flightStatusSQL.append(
            "INSERT INTO FlightStatus (FlightStatusId, FlightId, StatusId, " +
            "OptionalNote, DepartureDateTime, ArrivingDateTime, InsertTime) " +
            "VALUES (" +
            str(flightStatusId) + ", " +                # FlightStatusId
            str(flightId) + ", " +                      # FlightId
            str(randint(1, len(statuses))) + ", " +     # StatusId
            "''" + ", " +                               # OptionalNote
            "'" + random_datetime() + "'" + ", " +      # DepartureDateTime
            "'" + random_datetime() + "'" + ", " +      # ArrivingDateTime
            "'" + random_time() + "'" +                 # InsertTime
            ");")

        flightStatusId += 1
        i += 1

    flightId += 1

for plane in planes:
    airVehicleSQL.append(
        "INSERT INTO AirVehicle (PlaneId, TypeNum) VALUES (" +
        str(planes[plane]) + ", " +
        "'" + plane + "'" +
        ");")

for status in statuses:
    statusSQL.append("INSERT INTO Status(StatusId, StatusName) VALUES (" +
        str(statusId) + ", " +
        "'" + status + "'" +
        ");")
    statusId += 1

print(outputFlight + " [" + str(len(flightSQL)) + "]")
print(outputFliesOn + " [" + str(len(fliesOnSQL)) + "]")
print(outputAirVehicle + " [" + str(len(airVehicleSQL)) + "]")
print(outputStatus + " [" + str(len(statusSQL)) + "]")
print(outputFlightStatus + " [" + str(len(flightStatusSQL)) + "]")

write_contents(flightSQL, outputFlight)
write_contents(fliesOnSQL, outputFliesOn)
write_contents(airVehicleSQL, outputAirVehicle)
write_contents(statusSQL, outputStatus)
write_contents(flightStatusSQL, outputFlightStatus)
