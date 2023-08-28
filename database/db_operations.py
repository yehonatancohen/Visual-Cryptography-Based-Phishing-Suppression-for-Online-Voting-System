from .db_connector import get_database_connection

def execute_query(query, params=None):
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = cursor.fetchall()

            # Commit the transaction (if needed)
            connection.commit()

            return result

    except Exception as e:
        print(f"Database error: {str(e)}")
        return None
    finally:
        if connection:
            connection.close()
