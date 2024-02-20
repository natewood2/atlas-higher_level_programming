#!/usr/bin/python3
"""
A script that lists all cities from database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities(usr, pw, db_name):
    """ List all cities from the database. """

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])