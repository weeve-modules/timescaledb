from os import getenv

PARAMS = {
    "USERNAME": getenv("USERNAME", ""),
    "PASSWORD": getenv("PASSWORD", ""),
    "HOST_URL": getenv("HOST_URL", ""),
    "PORT": getenv("PORT", ""),
    "DATABASE_NAME": getenv("DATABASE_NAME", ""),
    "SSL_MODE": bool(getenv("SSL_MODE", "True")),
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": getenv("COLUMNS", ""),
    "LABELS": getenv("LABELS", "")
}

# parse columns and labels
if PARAMS['COLUMNS']:
    # build columns artefact
    columns = ""
    for c in [header.strip() for header in PARAMS['COLUMNS'].split(',')]:
        columns += f"{c},"
    PARAMS['COLUMNS'] = "(" + columns[:-1] + ")"
else:
    PARAMS['COLUMNS'] = None

if PARAMS['LABELS']:
    PARAMS['LABELS'] = [header.strip() for header in PARAMS['LABELS'].split(',')]
else:
    PARAMS['LABELS'] = None
