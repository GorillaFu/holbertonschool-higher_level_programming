#!/usr/bin/python3
"""accepts state as argument + lists cities of state"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    db = db.cursor()
    db.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state,))

    r = db.fetchall()
    print(", ".join([row[0] for row in r]))
