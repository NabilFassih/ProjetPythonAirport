import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost:3306/projet_python_airport?charset=utf8mb4')


def importAirlines():
    airlines = pd.read_csv('../csv/airlines.csv')
    airlines.to_sql('airlines', con=engine, if_exists='append', index=False, chunksize=1)


def importAirports():
    airports = pd.read_csv('../csv/airports.csv')
    airports.to_sql('airports', con=engine, if_exists='append', index=False, chunksize=1)


def importPlanes():
    planes = pd.read_csv('../csv/planes.csv')
    planes.to_sql('planes', con=engine, if_exists='append', index=False, chunksize=1)


def importWeathers():
    weathers = pd.read_csv('../csv/weather.csv')
    weathers.to_sql('weathers', con=engine, if_exists='append', index=False, chunksize=1)


def importFlights():
    flights = pd.read_csv('../csv/flights.csv')
    flights.to_sql('flights', con=engine, if_exists='append', index=False, chunksize=1)


importAirlines()
importAirports()
importPlanes()
importWeathers()
importFlights()

exit()