# How to query table using mysql.connector and then using then using the queried data in script
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='*****',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees") # query the employees table
        rows = cursor.fetchall() # fetch all the rows from the result
        print(type(rows)) # print the type of the result
        print("Employee details:")
        for row in rows:
            print(f"Employee ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}") # print the employee details   
except mysql.connector.Error as err:    
    print(f"Error: {err}")
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")