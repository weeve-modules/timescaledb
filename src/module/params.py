from os import getenv

PARAMS = {
    "USERNAME": getenv("USERNAME", ""),
    "PASSWORD": getenv("PASSWORD", ""),
    "HOST_URL": getenv("HOST_URL", ""),
    "PORT": getenv("PORT", ""),
    "DATABASE_NAME": getenv("DATABASE_NAME", ""),
    "SSL_MODE": True if getenv("SSL_MODE", "True") == 'True' else False,
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": getenv("COLUMNS", ""),
    "LABELS": getenv("LABELS", "")
}

# parse columns and labels
if PARAMS['COLUMNS']:
    PARAMS['COLUMNS'] = [column.strip() for column in PARAMS['COLUMNS'].split(',')]
else:
    PARAMS['COLUMNS'] = None

if PARAMS['LABELS']:
    PARAMS['LABELS'] = [header.strip() for header in PARAMS['LABELS'].split(',')]
else:
    PARAMS['LABELS'] = None
