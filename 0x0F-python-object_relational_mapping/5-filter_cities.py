#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    rows = cur.fetchall()
    cities = []
    for row in rows:
        if row[4] == check[0]:
            cities.append(row[2])
    print(', '.join(cities))
    cur.close()
    db.close()
