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

    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE BINARY states.name = %s \
    ORDER BY states.id',
        (state_name,),
    )
    results = cur.fetchall()
    for result in results:
        print(result)

    db.close()
