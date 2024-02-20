#!/usr/bin/python3
""" Script that lists all states from the database. """

import MySQLdb
import sys


def sql_connect(usr, pw, db_name):
    """Connect to a MySQL database and print all states."""

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
