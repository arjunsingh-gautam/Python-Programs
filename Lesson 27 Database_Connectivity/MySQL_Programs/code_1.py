# Connecting to MySQL database using mysql.connector
import mysql.connector
import os
# Establishing a connection to the database 
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='arjun1052003')
    if connection.is_connected():
        print("Connected to MySQL database")
except mysql.connector.Error as err:
    print(f"Error: {err}")# Writing a python object to json string using the json module

# close the connection
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")