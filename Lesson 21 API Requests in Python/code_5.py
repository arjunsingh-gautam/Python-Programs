# Implementing basic-auth
import requests
response=requests.get("https://httpbin.org/basic-auth/arjun/test",auth=('arjun','test'))

print(response.json())