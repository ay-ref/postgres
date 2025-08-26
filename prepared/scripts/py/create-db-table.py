import psycopg2
from psycopg2 import sql
import tempconf as config

host = config.host
user = config.username
password = config.password
db_name = config.dbname
port = config.port

print("port", port)
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database="postgres",
        user=user,
        password=password
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    print(f"Database '{db_name}' created.")

except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{db_name}' already exists.")
finally:
    cur.close()
    conn.close()

try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db_name,
        user=user,
        password=password
    )
    cur = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS emps (
        name TEXT,
        position TEXT,
        salary INTEGER
    );
    '''

    cur.execute(create_table_query)
    conn.commit()
    print("Table 'emps' created.")

except Exception as e:
    print("Error:", e)
    conn.rollback()
finally:
    cur.close()
    conn.close()
