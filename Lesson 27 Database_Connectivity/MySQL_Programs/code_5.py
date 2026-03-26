# More readable way to insert data into table using parameterized queries
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='arjun1052003',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        sql = '''INSERT INTO employees (name, age, department) 
                VALUES (%s, %s, %s)''' # parameterized query with placeholders
        values = [('Bob Brown', 35, 'Marketing'),('Amanda Smith',23,'HR')] # values to be inserted
        cursor.executemany(sql, values) # execute the query with the values
        connection.commit() # commit the changes to the database
        print("Row inserted successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")