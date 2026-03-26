# Deleting a record from the database using the DELETE statement
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='arjun1052003',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE name = 'John Doe'") # delete the record of the employee named John Doe
        connection.commit() # commit the changes to the database
        print("Record deleted successfully")        
except mysql.connector.Error as err:
    print(f"Error: {err}")  
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")