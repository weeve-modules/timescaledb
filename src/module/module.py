"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import psycopg2 as pg
from logging import getLogger
from .connect import createTimescaleConnection
from .params import PARAMS
from .query import QUERY

log = getLogger("module")

# connect to TimescaleDB
CURSOR, CONN = createTimescaleConnection()

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
    values = tuple(data[label] for label in PARAMS['LABELS'])

    log.debug(f"Query: {QUERY.as_string(CURSOR)}")
    log.debug(f"Values: {values}")

    try:
        log.info("Writing data...")
        CURSOR.execute(QUERY, values)
    except (Exception, pg.Error) as error:
        return f"Exception when executing the query: {error}"

    CONN.commit()

    return None
