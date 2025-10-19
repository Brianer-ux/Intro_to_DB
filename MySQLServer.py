import mysql.connector

try:
    print("Connecting to MySQL server...")
    connection = mysql.connector.connect(
        host='localhost',
        user='root',            # Replace with your MySQL username
        password='Brianna@12.'  # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
