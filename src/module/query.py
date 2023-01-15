import psycopg2
from psycopg2 import sql
from .params import PARAMS

# build SQL query
QUERY = sql.SQL(f"INSERT INTO {PARAMS['TABLE_NAME']}" + " ({columns}) VALUES ({values});").format(
    columns=sql.SQL(', ').join(map(sql.Identifier, PARAMS["COLUMNS"])),
    values=sql.SQL(', ').join(sql.Placeholder() * len(PARAMS["LABELS"]))
)
