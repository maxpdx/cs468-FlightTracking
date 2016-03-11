import pg8000

"""
To use this file please do:
1. make a copy of it to 'dbConnect.py'
2. change contents of db_connect() method bellow
3. use 'from dbConnect import *' whenever you need db_connect()
"""

def db_connect():
    return pg8000.connect(
        host="host",
        user="user",
        password="password",
        database="database"
    )
