# Fetching image data from http url using requests library and saving it to a file
import requests
import os
os.chdir(r"d:\Desktop\Python_Programs\Lesson 21 API Requests in Python")
image_url = "https://imgs.xkcd.com/comics/python.png"
response = requests.get(image_url)
if response.status_code==200:
    with open("demo.png",'wb') as f:
        f.write(response.content)

