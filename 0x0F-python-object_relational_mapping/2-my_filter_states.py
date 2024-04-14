#!/usr/bin/python3

"""A simple script that connects to database and executes a query"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password, db=db_name
    )

    query = 'SELECT * FROM states WHERE states.name = "{}" \
    ORDER BY states.id'.format(
        state_name
    )
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    for result in results:
        print(result)
