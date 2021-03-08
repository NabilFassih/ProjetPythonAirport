import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='projet_python_airport')

cur = conn.cursor()

def getAllAirports():
    return pd.read_sql('SELECT name, lat, lon FROM airports', conn).to_dict(orient='records')


def getAllFightsByMonth():
    return pd.read_sql('SELECT month, COUNT(month) as nb FROM flights GROUP BY month ORDER BY cast(month as unsigned) ASC', conn).to_dict(orient='records')


def getAirlinesDepDelay():
    return pd.read_sql('SELECT f.carrier, a.name, COUNT(f.dep_delay) as nb FROM flights f INNER JOIN airlines a ON a.carrier = f.carrier WHERE f.dep_delay > 0 GROUP BY f.carrier', conn).to_dict(orient='records')


def getAirlinesArrDelay():
    return pd.read_sql('SELECT f.carrier, a.name, COUNT(f.arr_delay) as nb FROM flights f INNER JOIN airlines a ON a.carrier = f.carrier WHERE f.arr_delay > 0 GROUP BY f.carrier', conn).to_dict(orient='records')


def dataAirports():
    nbAeroports = pd.read_sql('SELECT count(*) as nbAeroports FROM airports', conn).to_dict(orient='records')
    nbCompagnies = pd.read_sql('SELECT count(*) as nbCompagnies FROM airlines', conn).to_dict(orient='records')
    nbDestinations = pd.read_sql('SELECT count(*) as nbDestinations FROM flights', conn).to_dict(orient='records')
    nbAvions = pd.read_sql('SELECT count(*) as nbAvions FROM planes', conn).to_dict(orient='records')
    nbFuseauxHoraires = pd.read_sql('SELECT COUNT(DISTINCT tz) as nbFuseauxHoraires from airports', conn).to_dict(orient='records')
    nbZone =pd.read_sql('SELECT COUNT(*) as nbZone from airports WHERE dst = "N" AND tzone LIKE "%America/%"', conn).to_dict(orient='records')

    return nbAeroports, nbCompagnies, nbDestinations, nbAvions, nbFuseauxHoraires, nbZone


def lowAndTopDestination():
    topAeroportDepart = pd.read_sql('SELECT origin, a.name, MAX(mycount) as nb FROM ( SELECT origin, COUNT(origin) mycount FROM flights GROUP BY origin ) AS T INNER JOIN airports a ON a.faa = origin', conn).to_dict(orient='records')
    topDestination = pd.read_sql('SELECT dest, name, nombre FROM ( SELECT COUNT(*) AS NOMBRE, dest FROM flights GROUP BY dest ) AS T INNER JOIN airports ON dest = faa GROUP BY nombre DESC LIMIT 10', conn).to_dict(orient='records')
    lowDestination = pd.read_sql('SELECT dest, name, nombre FROM ( SELECT COUNT(*) AS NOMBRE, dest FROM flights GROUP BY dest ) AS T INNER JOIN airports ON dest = faa GROUP BY nombre ASC LIMIT 10', conn).to_dict(orient='records')

    return topAeroportDepart, topDestination, lowDestination

def nbDestinationsByCompagnie():
    nbDestinationsByCompagnie = pd.read_sql('SELECT a.name, COUNT(f.carrier) as nbDestination FROM flights f INNER JOIN airlines a ON f.carrier = a.carrier GROUP BY f.carrier HAVING COUNT(f.carrier)', conn).to_dict(orient='records')

    return nbDestinationsByCompagnie