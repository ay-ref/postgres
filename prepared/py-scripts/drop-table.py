import psycopg2
from psycopg2 import sql
import config


def drop_all_tables(connection_params):
    """
    Drop all tables in the public schema of a PostgreSQL database.
    
    :param connection_params: dict with keys like host, database, user, password, port
    """
    conn = psycopg2.connect(**connection_params)
    conn.autocomcommit = True  # Required for DROP SCHEMA
    cur = conn.cursor()

    try:
        # Option 1: Drop and recreate the public schema (simplest and cleanest)
        cur.execute("DROP SCHEMA public CASCADE;")
        cur.execute("CREATE SCHEMA public;")
        print("All tables dropped successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def drop_all_tables_individual(connection_params):
    conn = psycopg2.connect(**connection_params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        # Get list of all table names in the 'public' schema
        cur.execute("""
            SELECT tablename FROM pg_tables
            WHERE schemaname = 'public';
        """)
        tables = cur.fetchall()

        # Drop each table with CASCADE to handle dependencies
        for table in tables:
            drop_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(
                sql.Identifier(table[0])
            )
            cur.execute(drop_query)
            print(f"Dropped table: {table[0]}")

        print("All tables dropped.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# Example usage
if __name__ == "__main__":
    params = {
        "host": config.host,
        "database": config.dbname,
        "user": config.username,
        "password": config.password,
        "port": config.port
    }
    drop_all_tables_individual(params)
