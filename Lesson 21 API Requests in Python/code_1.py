# Handling http requests in Python using the requests library
import requests
import os
os.chdir(r"d:\Desktop\Python_Programs\Lesson 21 API Requests in Python")
response = requests.get("https://xkcd.com/353/")
print(response) # Output:<Response [200]>  200 means a successful response
print(response.status_code) # Output:200
print(response.headers) # Output:{'Date': 'Sat, 15 Jul 2023 12:00:00 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Content-Length': '12345', ...}
with open("response_1.html", "w", encoding="utf-8") as file:
    file.write(response.text) # Writing the response content to a file
