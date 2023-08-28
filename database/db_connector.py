import os
import mysql.connector

def get_database_connection():
    try:
        # Retrieve database credentials from environment variables
        db_config = {
            'host': os.environ['DB_HOST'],
            'user': os.environ['DB_USER'],
            'password': os.environ['DB_PASSWORD'],
            'database': os.environ['DB_NAME'],
        }

        # Establish a connection
        connection = mysql.connector.connect(**db_config)

        return connection

    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None
