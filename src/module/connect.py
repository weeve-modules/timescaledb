import psycopg2
from .params import PARAMS


def createTimescaleConnection():
    # connect to TimescaleDB
    CONNECTION = f"postgres://{PARAMS['USERNAME']}:{PARAMS['PASSWORD']}@{PARAMS['HOST_URL']}:{PARAMS['PORT']}/{PARAMS['DATABASE_NAME']}"
    if PARAMS["SSL_MODE"]:
        CONNECTION = CONNECTION + "?sslmode=require"
    conn = psycopg2.connect(CONNECTION)
    if conn:
        # prepare a cursor object
        return conn.cursor(), conn
    else:
        return None, None
