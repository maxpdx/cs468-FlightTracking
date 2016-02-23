from IOgenerate import *

sourceFlight = "data/routes2.dat"
outputFlight = "sql/flight.sql"
outputAirVehicle = "sql/airVehicle.sql"
outputFliesOn = "sql/fliesOn.sql"

flightId = 1    # Start value and increment from there
airVehicleId = 1
fliesOnId = 1

flightSQL = []
airVehicleSQL = []
fliesOnSQL = []

routes = get_contents(sourceFlight)

# first row
flightSQL.append(
    "INSERT INTO Flight (FlightId, FlightNo, AirlineId, FromAirportId, " +
    "ToAirportId, NumOfStops, WeekDays, DepartureTime, ArrivalTime, " +
    "Distance, Duration) VALUES")

airVehicleSQL.append("INSERT INTO AirVehicle (PlaneId, TypeNum) VALUES")

fliesOnSQL.append("INSERT INTO " +
                  "FliesOn(FlightAirVehicleId, FlightId, PlaneId) VALUES")

flightNOs = {}
planes = {}
for route in routes:

    # Skipping some routes that have \N in their rows.
    skip = False
    for el in route:
        if el == "\\N":
            skip = True
    if skip:
        continue

    # Making sure there are no duplicates in flight numbers
    flightNO = ""
    while flightNO == "" or flightNO in flightNOs:
        flightNO = route[0] + "-" + random_(randint(3, 5), string.digits)

    flightNOs[flightNO] = flightNO

    flightSQL.append("(" +
        str(flightId) + ", " +                          # FlightId
        flightNO + ", " +                               # FlightNo
        route[1] + ", " +                               # AirlineId
        route[3] + ", " +                               # FromAirportId
        route[5] + ", " +                               # ToAirportId
        route[7] + ", " +                               # NumOfStops
        random_week_days(randint(1, 4)) + ", " +        # WeekDays
        random_time() + ", " +                          # DepartureTime
        random_time() + ", " +                          # ArrivalTime
        random_(randint(2, 4), string.digits) + ", " +  # Distance
        random_time() +                                 # Duration
        "),")

    planesList = route[8].split(" ")
    for plane in planesList:
        if plane not in planes:
            planes[plane] = airVehicleId
            airVehicleId += 1

        fliesOnSQL.append("(" +
            str(fliesOnId) + ", " +
            str(flightId) + ", " +
            str(planes[plane]) +
            "),")
        fliesOnId += 1
    flightId += 1


for plane in planes:
    airVehicleSQL.append("(" +
        str(planes[plane]) + ", " +
        plane +
        "),")

print(outputFlight + " [" + str(len(flightSQL) - 1) + "]")
print(outputFliesOn + " [" + str(len(fliesOnSQL) - 1) + "]")
print(outputAirVehicle + " [" + str(len(airVehicleSQL) - 1) + "]")

# Making sure I'm ending with ';' (semicolon)
flightSQL[-1] = flightSQL[-1][:-1] + ";"
fliesOnSQL[-1] = fliesOnSQL[-1][:-1] + ";"
airVehicleSQL[-1] = airVehicleSQL[-1][:-1] + ";"

write_contents(flightSQL, outputFlight)
write_contents(fliesOnSQL, outputFliesOn)
write_contents(airVehicleSQL, outputAirVehicle)
