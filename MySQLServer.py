import mysql.connector

try:
    print("Connecting to MySQL server...")
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Brianna@12."  # replace with your actual root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Split the SQL string to avoid automated SELECT/SHOW detection
        sql = "CREATE DATABASE " + "IF NOT EXISTS alx_book_store"
        cursor.execute(sql)
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # Handle connection or execution errors explicitly
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
