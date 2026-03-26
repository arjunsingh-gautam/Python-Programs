# Creating a database using mysql.connector
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='arjun1052003')
    if connection.is_connected():
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_database") # create a database named my_database
        print("Database created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")