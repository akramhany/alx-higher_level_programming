#!/usr/bin/python3

"""A simple script that connects to database and executes a query"""

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
db_name = argv[3]

db = MySQLdb.connect(
    host='localhost', port=3306, user=username, passwd=password, db=db_name
)

cur = db.cursor()

if __name__ == '__main__':
    cur.execute('SELECT * FROM states ORDER BY states.id')
    results = cur.fetchall()
    for result in results:
        print(result)
