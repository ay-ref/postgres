import psycopg2
from psycopg2 import sql
import tempconf as config

db_config = {
    'dbname': config.dbname,
    'user': config.username,
    'password': config.password,
    'host': config.host,  
    'port': config.port          
}

data_to_insert = [
    ('John Doe', 'Software Engineer', 75000),
    ('Jane Smith', 'Data Scientist', 85000),
    ('Alice Johnson', 'Product Manager', 90000)
]

insert_query = sql.SQL("""
    INSERT INTO emps (name, position, salary)
    VALUES (%s, %s, %s);
""")

try:
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    for row in data_to_insert:
        cursor.execute(insert_query, row)

    connection.commit()
    print("Data inserted successfully!")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
