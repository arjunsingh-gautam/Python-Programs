# HTTP get method
import requests
payload={"page":2,"count":25}
response=requests.get("https://httpbin.org/get",params=payload)
print(response.headers)
print(response.url)
print(response.json())