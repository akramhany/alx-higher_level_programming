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
        'SELECT cities.name FROM cities INNER JOIN \
        states ON cities.state_id = states.id WHERE BINARY states.name = %s \
        ORDER BY cities.id;',
        (state_name,),
    )
    results = cur.fetchall()
    endT = ''
    for result in results:
        print(endT, end='')
        print(result[0], end='')
        endT = ', '
    print()

    db.close()
