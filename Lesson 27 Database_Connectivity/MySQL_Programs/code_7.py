# Updating a record in the database using the UPDATE statement
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='arjun1052003',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute("UPDATE employees SET age = 33 WHERE name = 'John Doe'") # update the age of the employee named John Doe to 30
        connection.commit() # commit the changes to the database
        print("Record updated successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")