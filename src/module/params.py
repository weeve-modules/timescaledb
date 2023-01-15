from os import getenv

PARAMS = {
    "USERNAME": getenv("USERNAME", ""),
    "PASSWORD": getenv("PASSWORD", ""),
    "HOST_URL": getenv("HOST_URL", ""),
    "PORT": getenv("PORT", ""),
    "DATABASE_NAME": getenv("DATABASE_NAME", ""),
    "SSL_MODE": True if getenv("SSL_MODE", "True") == 'True' else False,
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": [column.strip() for column in getenv("COLUMNS", "").split(',')],
    "LABELS": [label.strip() for label in getenv("LABELS", "").split(',')]
}
