CREATE SCHEMA IF NOT EXISTS "AirlineTrackingSystem";

CREATE TABLE IF NOT EXISTS Country
(
  CountryId INT NOT NULL,
  CountryName VARCHAR(100),
  PRIMARY KEY(CountryId)
);

CREATE TABLE IF NOT EXISTS Airport
(
  AirportId INT NOT NULL,
  AirportName VARCHAR(255),
  City VARCHAR(100),
  CountryId INT,
  Alias VARCHAR(10),
  Latitude NUMERIC,
  Longitude NUMERIC,
  Altitude NUMERIC,
  TimeZone SMALLINT NOT NULL,
  PRIMARY KEY(AirportId),
  FOREIGN KEY (CountryId) REFERENCES Country(CountryId)
);

CREATE TABLE IF NOT EXISTS Airline
(
  AirlineId INT NOT NULL,
  AirlineName VARCHAR(255),
  Alias VARCHAR(50),
  CountryId INT,
  PRIMARY KEY(AirlineId),
  FOREIGN KEY (CountryId) REFERENCES Country(CountryId)
);

CREATE TABLE IF NOT EXISTS Flight
(
  FlightId INT NOT NULL,
  FlightNo INT NOT NULL,
  AirlineId INT NOT NULL,
  FromAirportId INT NOT NULL,
  ToAirportId INT NOT NULL,
  NumOfStops SMALLINT,
  WeekDays VARCHAR(15),
  DepartureTime TIME,
  ArrivalTime TIME,
  Distance SMALLINT,
  Duration TIME,
  PRIMARY KEY(FlightId),
  FOREIGN KEY(AirlineId) REFERENCES Airline(AirlineId),
  FOREIGN KEY(FromAirportId) REFERENCES Airport(AirportId),
  FOREIGN KEY(ToAirportId) REFERENCES Airport(AirportId)
);

CREATE TABLE IF NOT EXISTS AirVehicle
(
  PlaneId INT NOT NULL UNIQUE,
  TypeNum VARCHAR (50)
);

CREATE TABLE IF NOT EXISTS FliesOn
(
  FlightAirVehicleId INT NOT NULL,
  FlightId INT NOT NULL,
  PlaneId INT NOT NULL,
  FOREIGN KEY(FlightId) REFERENCES Flight(FlightId),
  FOREIGN KEY(PlaneId) REFERENCES Airvehicle(PlaneId)
);

CREATE TABLE IF NOT EXISTS Status
(
  StatusId INT NOT NULL,
  StatusName VARCHAR(100),
  PRIMARY KEY(StatusId)
);

CREATE TABLE IF NOT EXISTS FlightStatus
(
  FlightStatusId INT NOT NULL UNIQUE,
  FlightId INT NOT NULL,
  StatusId INT NOT NULL,
  OptionalNote VARCHAR(255),
  DepartureDateTime TIMESTAMP,
  ArrivingDateTime TIMESTAMP,
  InsertTime TIME,
  FOREIGN KEY(FlightId) REFERENCES Flight(FlightId),
  FOREIGN KEY(StatusId) REFERENCES Status(StatusId)
);
