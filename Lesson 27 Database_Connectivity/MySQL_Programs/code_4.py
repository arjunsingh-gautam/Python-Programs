# Inserting rows into a table using the execute() method
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='***',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO employees (name, age, department) 
                        VALUES ('John Doe', 30, 'HR'),('Jane Smith', 25, 'IT'),('Alice Johnson', 28, 'Finance')
                        ''') # insert a row into the employees table
         # insert row into the employees table
        connection.commit() # commit the changes to the database
        print("Rows inserted successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")  
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")