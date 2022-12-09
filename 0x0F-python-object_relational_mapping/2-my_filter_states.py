#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(sql_cmd)
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
