#!/usr/bin/python3

"""A simple script that connects to database and executes a query"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password, db=db_name
    )

    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE states.name \
            LIKE BINARY "N%" ESCAPE "/" ORDER BY states.id'
    )
    results = cur.fetchall()
    for result in results:
        print(result)
