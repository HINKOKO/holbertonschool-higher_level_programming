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
    cur.execute(
        "SELECT * FROM states WHERE name = %s \
            ORDER BY states.id ASC", (sys.argv[4], )
    )
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
