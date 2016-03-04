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

countries = {"UNKNOWN": 0}


def insert_country(c="", c_id=countryId, c_list=countries):
    c = c.strip()
    if not c:
        c = "UNKNOWN"

    if c not in c_list:
        c_list[c] = c_id
        c_id += 1

    return c_id, c, c_list


for airport in airports:
    country = airport[3]
    countryId, country, countries = insert_country(country, countryId,
                                                   countries)

    airportSQL.append(
        "INSERT INTO Airport ("
        "AirportId, AirportName, City, CountryId, Alias, "
        "Latitude, Longitude, Altitude, TimeZone) VALUES (" +
        airport[0] + "," +                  # AirportId
        "'" + airport[1] + "'" + "," +      # Name
        "'" + airport[2] + "'" + "," +      # City
        str(countries[country]) + "," +     # CountryId
        "'" + airport[4] + "'" + "," +      # Alias
        airport[6] + "," +          # Latitude
        airport[7] + "," +          # Longitude
        airport[8] + "," +          # Altitude
        str(airport[9]) +           # TimeZone
        ");")

for airline in airlines:
    country = airline[6]
    countryId, country, countries = insert_country(country, countryId,
                                                   countries)

    airlineSQL.append(
        "INSERT INTO Airline ("
        "AirlineId, AirlineName, Alias, CountryId) VALUES (" +
        airline[0] + "," +          # AirlineId
        "'" + airline[1] + "'," +   # Name
        "'" + airline[2] + "'," +   # Alias
        str(countries[country]) +   # CountryId
        ");")

for country in countries:
    countrySQL.append(
        "INSERT INTO Country ("
        "CountryId, CountryName) VALUES (" +
        str(countries[country]) + ", " +
        "'" + country + "'" +
        ");")


print(outputAirport + " [" + str(len(airportSQL)) + "]")
print(outputAirline + " [" + str(len(airlineSQL)) + "]")
print(outputCountry + " [" + str(len(countrySQL)) + "]")

write_contents(airportSQL, outputAirport)
write_contents(airlineSQL, outputAirline)
write_contents(countrySQL, outputCountry)
