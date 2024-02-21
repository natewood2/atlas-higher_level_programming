#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities.
"""

import MySQLdb
import sys


def list_cities_of_state(usr, pw, db_name, state_name):
    """List all cities of a specified state from the database."""

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    query = ("SELECT cities.id, cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC;")
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    cities = []
    for row in rows:
        cities.append(row[1])
    print(", ".join(cities))

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_of_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
