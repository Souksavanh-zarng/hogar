from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

dbConnection = "dbname='hogar' user='postgres' host='localhost' password='sml' port=5433"

    # pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    con.autocommit = True
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)
