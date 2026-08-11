# Selecting a database and creating a table using mysql.connector
import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',user='root',password='***',database='my_database')
    if connection.is_connected():   
        print("Connected to MySQL database")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            age INT NOT NULL,
                            department VARCHAR(255) NOT NULL
                        )''') # create a table named employees with id, name, age and department columns
        print("Table created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
# close the connection
finally:    
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")