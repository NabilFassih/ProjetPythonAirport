import pymysql
import os
from more_itertools import unique_everseen

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='projet_python_airport')

cur = conn.cursor()

def importAirlines():
    query = "LOAD DATA INFILE 'C:/Users/suley/Documents/Projet/ProjetPythonAirport/csv/airlines.csv' INTO TABLE airlines fields terminated BY ',' IGNORE 1 LINES;"
    cur.execute(query)
    conn.commit()


def importAirports():
    query = "LOAD DATA INFILE 'C:/Users/suley/Documents/Projet/ProjetPythonAirport/csv/airports.csv' INTO TABLE airports fields terminated BY ',' IGNORE 1 LINES;"
    cur.execute(query)
    conn.commit()


def importPlanes():
    query = "LOAD DATA INFILE 'C:/Users/suley/Documents/Projet/ProjetPythonAirport/csv/planes.csv' INTO TABLE planes fields terminated BY ',' IGNORE 1 LINES;"
    cur.execute(query)
    conn.commit()


def importWeathers():
    query = "LOAD DATA INFILE 'C:/Users/suley/Documents/Projet/ProjetPythonAirport/csv/weather.csv' INTO TABLE weathers fields terminated BY ',' IGNORE 1 LINES (origin,year,month,day,hour,temp,dewp,humid,wind_dir,wind_speed,wind_gust,precip,pressure,visib,time_hour);"
    cur.execute(query)
    conn.commit()


def importFlights():
    query = "LOAD DATA INFILE 'C:/Users/suley/Documents/Projet/ProjetPythonAirport/csv/flights.csv' INTO TABLE flights fields terminated BY ',' IGNORE 1 LINES (year,month,day,dep_time,sched_dep_time,dep_delay,arr_time,sched_arr_time,arr_delay,carrier,flight,tailnum,origin,dest,air_time,distance,hour,minute,time_hour);"
    cur.execute(query)
    conn.commit()


# importAirlines()
# importAirports()
# importPlanes()
# importWeathers()
# importFlights()