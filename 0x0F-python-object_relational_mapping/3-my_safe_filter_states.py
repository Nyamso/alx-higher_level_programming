#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (argv[4],))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
