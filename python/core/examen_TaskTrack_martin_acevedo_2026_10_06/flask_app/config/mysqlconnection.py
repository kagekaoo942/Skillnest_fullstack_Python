import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"

if not ENV_FILE.is_file():
    raise RuntimeError(
        f"No se encontró {ENV_FILE}. Copia .env.example como .env "
        "y completa las credenciales."
    )

load_dotenv(ENV_FILE)

REQUIRED_SETTINGS = ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "SECRET_KEY")
missing_settings = [name for name in REQUIRED_SETTINGS if os.getenv(name) is None]
if missing_settings:
    raise RuntimeError(
        "Faltan estas variables en .env: " + ", ".join(missing_settings)
    )


DB_CONFIG = {
    "host": os.environ["DB_HOST"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "database": os.environ["DB_NAME"],
}


def connect_to_mysql():
    return pymysql.connect(
        **DB_CONFIG,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def query_db(query, params=None, fetch="all"):
    connection = connect_to_mysql()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params or {})
            if fetch == "one":
                return cursor.fetchone()
            if fetch == "none":
                return cursor.lastrowid
            return cursor.fetchall()
    finally:
        connection.close()
