#!/usr/bin/python3
"""filters printed states that start w cpital N"""
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    my_states = c.fetchall()
    for state in my_states:
        if state[1][0] == 'N':
            print(state)
