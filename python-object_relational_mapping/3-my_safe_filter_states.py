#!/usr/bin/python3
""" Script that displays all values in the states table. """

import MySQLdb
import sys


def sql_connect(usr, pw, db_name, state_name):
    """ SQL injections. """

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        sql_connect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
