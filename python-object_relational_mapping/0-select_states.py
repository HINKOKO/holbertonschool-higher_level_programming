#!/usr/bin/python3

"""
Script to list all states
from database hbtn_0e_0usa
"""

import MySQLdb
import sys

if "__main__" == __name__:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db='hbtn_0e_0_usa',
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
