import psycopg2
from psycopg2 import sql
import pandas as pd
import tempconf as config

tb_name = "emps"

def connect_to_db():
    """Establish connection to PostgreSQL database"""
    try:
        connection = psycopg2.connect(
            host=config.host,          
            database=config.dbname,
            user=config.username,
            password=config.password,
            port=config.port
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def read_data_basic():
    """Basic example of reading data"""
    connection = connect_to_db()
    
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        
        cursor.execute(f"SELECT * FROM {tb_name} LIMIT 10;")
        
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
            
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def read_data_with_column_names():
    """Read data with column names"""
    connection = connect_to_db()
    
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM emps LIMIT 10;")
        
        column_names = [desc[0] for desc in cursor.description]
        
        rows = cursor.fetchall()
        
        print("Columns:", column_names)
        for row in rows:
            print(dict(zip(column_names, row)))
            
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def read_data_into_dataframe():
    """Read data into pandas DataFrame"""
    connection = connect_to_db()
    
    if connection is None:
        return None
    
    try:
        query = f"SELECT * FROM {tb_name};"
        df = pd.read_sql_query(query, connection)
        
        print(f"Retrieved {len(df)} rows")
        print(df.head())
        
        return df
        
    except Exception as e:
        print(f"Error reading data: {e}")
        return None
    finally:
        connection.close()

def read_with_parameters(table_name, limit=10):
    """Read data with parameters (safe from SQL injection)"""
    connection = connect_to_db()
    
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        
        query = sql.SQL("SELECT * FROM {} LIMIT %s").format(
            sql.Identifier(table_name)
        )
        
        cursor.execute(query, (limit,))
        
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        
        result = []
        for row in rows:
            result.append(dict(zip(column_names, row)))
        
        return result
        
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    print("=== Basic Reading ===")
    read_data_basic()
    
    print("\n=== With Column Names ===")
    read_data_with_column_names()
    
    print("\n=== Into DataFrame ===")
    df = read_data_into_dataframe()
    
    print("\n=== With Parameters ===")
    results = read_with_parameters(f"{tb_name}", 5)
    if results:
        for row in results:
            print(row)
