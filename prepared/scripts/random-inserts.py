import psycopg2
from psycopg2 import sql

# Database connection parameters
db_config = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # or your database host
    'port': 5432          # default PostgreSQL port
}

# Data to insert
data_to_insert = [
    ('John Doe', 'Software Engineer', 75000),
    ('Jane Smith', 'Data Scientist', 85000),
    ('Alice Johnson', 'Product Manager', 90000)
]

# SQL query to insert data
insert_query = sql.SQL("""
    INSERT INTO employees (name, position, salary)
    VALUES (%s, %s, %s);
""")

try:
    # Connect to the database
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    # Insert each row of data
    for row in data_to_insert:
        cursor.execute(insert_query, row)

    # Commit the transaction
    connection.commit()
    print("Data inserted successfully!")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()