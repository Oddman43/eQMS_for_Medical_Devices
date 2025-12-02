import sqlite3
import os

db_path: str = "mediqms.db"
db_schema: str = "schema.sql"

os.remove(db_path)

with sqlite3.connect(db_path) as db:
    with open(db_schema, encoding="utf-8") as f:
        schema = f.read()
    db.executescript(schema)
