#!/usr/bin/python3
""" Lists all states with a name starting with N. """

import MySQLdb
import sys


def sql_connect(usr, pw, db_name):
    """Connect to a MySQL database and print all states starting with 'N'."""

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])