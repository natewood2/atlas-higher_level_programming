#!/usr/bin/python3
"""
Script that displays all values in the states
table where name matches the argument.
"""

import MySQLdb
import sys


def sql_connect(usr, pw, db_name, state_name):
    """
    Connect to a MySQL database and display
    all states matching a specific name.
    """

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'\
        ORDER BY id ASC;".format(state_name)
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        if row[1] == state_name:
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
