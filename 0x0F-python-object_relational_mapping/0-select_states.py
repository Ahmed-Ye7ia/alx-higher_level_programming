#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
Results must be sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    data = MySQLdb.connect(host = "local host",
                         port = 3306,
                         user = argv[1],
                         passwd = argv[2],
                         db = argv[3])

    # creatint cursor
    cursor = data.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    data.close()
