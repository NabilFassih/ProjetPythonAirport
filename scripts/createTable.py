import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='projet_python_airport')

cur = conn.cursor()

def createTableAirlines():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `airlines` (
            `carrier` varchar(255) NOT NULL,
            `name` varchar(255) NOT NULL,
            PRIMARY KEY (`carrier`)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    ''')

    print('Create Table Airlines')


def createTableAirports():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `airports` (
            `faa` varchar(255) NOT NULL,
            `name` varchar(255) NOT NULL,
            `lat` varchar(255) NOT NULL,
            `lon` varchar(255) NOT NULL,
            `alt` varchar(255) NOT NULL,
            `tz` varchar(255) NOT NULL,
            `dst` varchar(255) NOT NULL,
            `tzone` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`faa`)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    ''')

    print('Create Table Airports')


def createTablePlanes():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `planes` (
            `tailnum` varchar(255) NOT NULL,
            `year` varchar(4) NOT NULL,
            `type` varchar(255) NOT NULL,
            `manufacturer` varchar(255) NOT NULL,
            `model` varchar(255) NOT NULL,
            `engines` varchar(255) NOT NULL,
            `seats` varchar(30) NOT NULL,
            `speed` varchar(50) NOT NULL,
            `engine` varchar(255) NOT NULL,
            PRIMARY KEY (`tailnum`)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    ''')

    print('Create Table Planes')


def createTableWeathers():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `weathers` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `year` varchar(4) NOT NULL,
            `month` varchar(10) NOT NULL,
            `day` varchar(10) NOT NULL,
            `hour` int(11) NOT NULL,
            `temp` varchar(255) NOT NULL,
            `dewp` varchar(255) NOT NULL,
            `humid` varchar(255) NOT NULL,
            `wind_dir` varchar(255) NOT NULL,
            `wind_speed` varchar(255) NOT NULL,
            `wind_gust` varchar(255) NOT NULL,
            `precip` varchar(255) DEFAULT NULL,
            `visib` int(11) NOT NULL,
            `time_hour` varchar(255) NOT NULL,
            `origin` varchar(255) NOT NULL,
            `pressure` varchar(255) NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    ''')

    print('Create Table Weathers')


def createTableFlights():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `flights` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `year` varchar(100) NOT NULL,
            `month` varchar(100) NOT NULL,
            `day` varchar(100) NOT NULL,
            `dep_time` varchar(100) NOT NULL,
            `sched_dep_time` varchar(100) NOT NULL,
            `dep_delay` varchar(100) NOT NULL,
            `arr_time` varchar(100) NOT NULL,
            `sched_arr_time` varchar(100) NOT NULL,
            `arr_delay` varchar(100) NOT NULL,
            `carrier` varchar(100) NOT NULL,
            `flight` varchar(100) NOT NULL,
            `tailnum` varchar(100) NOT NULL,
            `origin` varchar(100) NOT NULL,
            `dest` varchar(100) NOT NULL,
            `air_time` varchar(100) NOT NULL,
            `distance` varchar(100) NOT NULL,
            `hour` varchar(100) NOT NULL,
            `minute` varchar(100) NOT NULL,
            `time_hour` varchar(100) NOT NULL,
            PRIMARY KEY (`id`),
            FOREIGN KEY `carrier` (`carrier`) REFERENCES airlines(carrier),
            FOREIGN KEY `tailnum` (`tailnum`) REFERENCES planes(tailnum)
        ) ENGINE=MyISAM DEFAULT CHARSET=latin1;
    ''')

    print('Create Table Flights')


createTableAirlines()
createTableAirports()
createTablePlanes()
createTableWeathers()
createTableFlights()