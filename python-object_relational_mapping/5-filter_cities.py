#!/usr/bin/python3

"""
== Safe version / prevents SQL Injection ==
Script to list all states
from database hbtn_0e_0usa
where name of states matches an argument of command line

"""

import MySQLdb
import sys

if "__main__" == __name__:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                INNER JOIN states WHERE states.id=cities.state_id AND states.name= %s \
                ORDER BY cities.id ASC", (sys.argv[4], )
                )
    rows = cur.fetchall()
    display = (' ,'.join(row[0] for row in rows))
    cur.close()
    db.close()
