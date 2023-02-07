from psycopg2 import sql
from .params import PARAMS

# build SQL query
QUERY = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values});").format(
    table=sql.Identifier(PARAMS["TABLE_NAME"]),
    columns=sql.SQL(", ").join(map(sql.Identifier, PARAMS["COLUMNS"])),
    values=sql.SQL(", ").join(sql.Placeholder() * len(PARAMS["LABELS"])),
)
