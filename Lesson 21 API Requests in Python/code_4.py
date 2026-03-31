# HTTP post method
import requests
payload={'username':"Arjun","password":"testing"}
response=requests.post("https://httpbin.org/post",data=payload)
print(response.headers)
data=response.json()
print(data['form'])