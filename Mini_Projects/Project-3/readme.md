

# **🌤 Weather App using OpenWeatherMap API**

## Project Overview

This Python project retrieves and displays real-time weather data for any city using the **OpenWeatherMap API**. It demonstrates key concepts like API interaction, JSON parsing, environment variable management, object-oriented programming, and user interaction via the terminal.

---

## Objective

The main goal of this project is to **fetch and display accurate weather information** for a user-specified city, including:

* Temperature (in Celsius)
* Humidity (percentage)
* Weather description (e.g., clear sky, haze, rain)

It also provides a reusable, class-based structure that can be extended into larger applications, like a GUI app or a web dashboard.

---

## Design & Architecture

The project uses **object-oriented programming (OOP)** for better structure and reusability:

### 1. City Class

* **Attributes**:

  * `name`: Name of the city
  * `temperature`: Current temperature
  * `humidity`: Current humidity
  * `description`: Weather description
* **Methods**:

  * `fetch_weather_data()`: Sends an API request to OpenWeatherMap and returns the JSON response as a Python dictionary. Handles HTTP errors.
  * `set_values()`: Extracts temperature, humidity, and description from the JSON response and stores them in the object.
  * `get_weather_data()`: Calls `set_values()` and prints the weather information in a formatted style.

### 2. User Interaction

* Terminal-based input allows the user to search multiple cities in a loop.
* Option to exit or continue searching for additional cities.

---

## Implementation Details

### 1. Environment Variables

* The **API key** is stored in a `.env` file to keep it secure and prevent exposing it in the code.
* `.env` format:

  ```
  WEATHER_API_KEY=your_real_api_key_here
  ```
* Python code loads the key using `python-dotenv`:

  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()
  api_key = os.getenv("WEATHER_API_KEY")
  ```
* This approach prevents accidental exposure on GitHub or other shared environments.

---

### 2. Sending HTTP Requests

* Uses the `requests` module to send **GET requests** to the OpenWeatherMap API:

  ```python
  import requests
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
  response = requests.get(url)
  ```
* `response` is a **Response object** that contains:

  * `response.status_code` → HTTP status code (200 means OK)
  * `response.text` → raw response as string
  * `response.json()` → parsed JSON as a Python dictionary

---

### 3. Parsing the JSON Response

* OpenWeatherMap returns JSON data, which is converted to a Python dictionary using:

  ```python
  data = response.json()
  ```
* Relevant fields are extracted:

  ```python
  temperature = data["main"]["temp"]
  humidity = data["main"]["humidity"]
  description = data["weather"][0]["description"]
  ```

---

### 4. OpenWeatherMap API Guidelines

* Sign up at [OpenWeatherMap](https://openweathermap.org/) to get a free API key.
* Use the **Current Weather Data API** endpoint:

  ```
  http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric
  ```
* Free tier allows multiple requests per minute; handle errors gracefully.
* API returns data in **JSON format**, containing keys like `main`, `weather`, `wind`, etc.

---

## Additional Features

* Formatted terminal output with emojis for better readability:

  ```
  🌡️ Temperature: 30°C
  💧 Humidity: 78%
  ☁️ Description: haze
  ```
* Error handling for invalid cities or API errors.
* Reusable `City` class can be extended for:

  * Logging weather history to CSV
  * Displaying additional metrics (wind speed, sunrise/sunset)
  * GUI or web-based applications

---

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:

   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project folder with your API key.
4. Run the script:

   ```bash
   python weather_app.py
   ```
5. Enter the city name when prompted. Optionally, search multiple cities.

---

## Learning Outcomes

* Understanding **APIs and HTTP requests**
* Parsing **JSON data** into Python dictionaries
* Using **environment variables** for secure key storage
* Building **OOP-based Python projects**
* Handling user input and error cases in terminal applications

---

This README makes your project **professional, clear, and portfolio-ready**.

---


