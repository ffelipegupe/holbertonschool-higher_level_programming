#!/usr/bin/python3
""" Filter states module """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name like '{:s}' ORDER BY \
    id ASC".format(argv[4])
    [print(state) for state in c.fetchall()]