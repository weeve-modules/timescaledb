"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import psycopg2 as pg
from psycopg2 import sql
from logging import getLogger
from .connect import createTimescaleConnection
from .params import PARAMS

log = getLogger("module")

# connect to TimescaleDB
CURSOR, CONN = createTimescaleConnection()

query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values});").format(
    table=sql.Identifier(PARAMS['TABLE_NAME']),
    columns=sql.SQL(", ").join(
        [sql.Identifier(column) for column in PARAMS['COLUMNS']]
    ),
    values=sql.SQL(", ").join(sql.Placeholder() * len(PARAMS['LABELS'])),
)


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        if not CURSOR:
            raise Exception("Cannot connect to TimescaleDB, check provided API details and authentication credentials.")

        if type(received_data) == dict:
            return insert_data(received_data)
        else:
            for data in received_data:
                resp_error = insert_data(data)
                if resp_error:
                    return resp_error
            return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"

def insert_data(data):
    # build values
    values = []
    for label in PARAMS['LABELS']:
        values.append(data[label])

    try:
        log.info("Writing data...")
        CURSOR.execute(query, values)
    except (Exception, pg.Error) as error:
        return error.pgerror

    CONN.commit()

    return None
