# cs468-FlightTracking
Some helper python scripts to parse CSV data from http://openflights.org/data.html to generate SQLs for them. 

Also generating some 'random data' to satisfy our database requirement.

3 main scripts that create 'sql' queries based on 'data':
# airlinesAirports.py
Generates sql queries for:
  1. sql/country.sql [318]
  2. sql/airport.sql [8107]
  3. sql/airline.sql [6048]

# flightsPlanes.py
Generates sql queries for:
  1. sql/flight.sql [66548]
  2. sql/airVehicle.sql [167]
  3. sql/fliesOn.sql [92021]
  4. sql/status.sql [7]
  5. sql/flightStatus.sql [34967]
  
# db.py
Connects to CS dept. postgress db and excecutes queries from sql files above + "sql/_CREATE_TABLE.sql"

----------

dist.py - script where I tested different statistical distributions.
