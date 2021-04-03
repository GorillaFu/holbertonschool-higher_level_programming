#!/usr/bin/python3
"""accepts state as argument + lists cities of state"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    db = db.cursor()
    db.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
    states ON cities.state_id=states.id")

    r = db.fetchall()
    print(", ".join([row[0] for row in r]))
