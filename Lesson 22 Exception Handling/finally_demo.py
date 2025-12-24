# In this we will implement finally block:
# Task:Open a file Read content close file using finally:
file = None

try:
    file = open("D:\Desktop\Python_Programs\Lesson 22 Exception Handling\sample.txt", "r")
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError as e:
    print("Error:", e)

finally:
    if file is not None:
        file.close()
        print("File closed successfully")
    else:
        print("File was never opened")
