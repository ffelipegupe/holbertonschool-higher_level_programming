#!/usr/bin/python3
""" Filter states module """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
