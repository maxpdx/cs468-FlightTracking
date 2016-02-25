from IOgenerate import *

sourceAirports = "data/airports.dat"
sourceAirlines = "data/airlines.dat"
outputAirport = "sql/airport.sql"
outputAirline = "sql/airline.sql"
outputCountry = "sql/country.sql"

# Start values for IDs
airportId = 1
airlineId = 1
countryId = 1

airportSQL = []
airlineSQL = []
countrySQL = []

airports = get_contents(sourceAirports)
airlines = get_contents(sourceAirlines)

countries = {}

for airport in airports:
    country = airport[3]
    if country and country != " " and country not in countries:
        countries[country] = countryId
        countryId += 1

    airportSQL.append(
        "INSERT INTO Airports (AirportId, Name, City, CountryId, Alias, "
        "Latitude, Longitude, Altitude, TimeZone) VALUES (" +
        airport[0] + "," +          # AirportId
        airport[1] + "," +          # Name
        airport[2] + "," +          # City
        str(countries[country]) + "," +  # CountryId
        airport[4] + "," +          # Alias
        airport[5] + "," +          # Latitude
        airport[6] + "," +          # Longitude
        airport[7] + "," +          # Altitude
        airport[8] +                # TimeZone
        ");")

for airline in airlines:
    country = airline[6]
    if country and country != " " and country not in countries:
        countries[country] = countryId
        countryId += 1

    airlineSQL.append(
        "INSERT INTO Airline (AirlineId, Name, Alias, CountryId) VALUES (" +
        airline[0] + "," +          # AirlineId
        airline[1] + "," +          # Name
        airline[2] + "," +          # Alias
        str(countries[country]) +   # CountryId
        ");")

for country in countries:
    countrySQL.append(
        "INSERT INTO Country (CountryId, Name) VALUES (" +
        str(countries[country]) + ", " +
        country +
        ");")


print(outputAirport + " [" + str(len(airportSQL)) + "]")
print(outputAirline + " [" + str(len(airlineSQL)) + "]")
print(outputCountry + " [" + str(len(countrySQL)) + "]")

write_contents(airportSQL, outputAirport)
write_contents(airlineSQL, outputAirline)
write_contents(countrySQL, outputCountry)
