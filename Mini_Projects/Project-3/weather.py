# This project we are going to retrieve weather data from OpenWeathermap.org
""" Modules: """
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

class City:
    def __init__(self, name: str):
        self.name = name
        self.temperature = None
        self.description = None
        self.humidity = None

    def fetch_weather_data(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    def set_values(self):
        data = self.fetch_weather_data()
        if data:
            self.temperature = data["main"]["temp"]
            self.humidity = data["main"]["humidity"]
            self.description = data["weather"][0]["description"]

    def get_weather_data(self):
        self.set_values()
        if self.temperature is not None:
            print(f"Weather of {self.name} is:")
            print(f"\033[31m🌡️  Temperature: {self.temperature}°C\033[0m")
            print(f"\033[31m💧  Humidity: {self.humidity}%\033[0m")
            print(f"\033[31m☁️  Description: {self.description}\033[0m")


i = 0
while i < 10:
    print(50 * "*")
    c = City(input("Enter city name for which you want weather_data: ").capitalize())
    c.get_weather_data()
    print(50 * "*")
    option = int(input("If you want to search weather for another city, enter 1; else to exit enter 0: "))
    if option == 1:
        i += 1
        continue
    else:
        break