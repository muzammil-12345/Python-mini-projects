'''
  Day 19 : Weather app using API (API Basics)
  Topics Covered:
  1. What is an API?
  2. How APIs works
  3. Using API keys
  4. Fetching data from APIs using requests
  5. Mini-project: Weather App using API 
'''
# What is an API?
'''An API (Aplication programming interface) is a set of
rules adn tools that allows diffrent software applications
to communicate with eachother. APIs enables deveopers to
fetch data, send data and interact with external services
(e.g: Weather data, financia market information).'''

# How APIs work
'''You send a request to an API endpoint, th API processes 
your request, the API send bakc response oftn in JSON format
containing the requested data.
'''
# Example of API call
# https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY

# Using API keys (Generate your own API key in the openweathermap website)
# Fetching Data from APIs using requests

# import requests


# API_KEY = '33605e314c7ac75763b4a7016bd457c0'
# city = 'Islamabad'
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# response = requests.get(url)
# if response.status_code == 200:
#     weather_data = response.json()
#     print(weather_data)
# else: 
#     print("An error ocured. Status code: ", response.status_code)


# --- Mini-project: Weather App using Openweathermap API ---

import requests

# Step 1: API Setup
API_KEY = '33605e314c7ac75763b4a7016bd457c0'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 2: Get Weather Data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
           data = response.json()
           weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}C",
            "Weather": data['weather'][0]['description'].title(),
            "Humidity": f"{data['main']['humidity']}%",
            "wind Speed": f"{data['wind']['speed']}m/s"
            }
           return weather
        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occured. Status code: ", response.status_code)
    except Exception as e:
        print("An Error occurred: ",e)
    return None

# Step 3: Display the weather information
def display_weather(weather):
    print("\n--- Weather Information ---")
    for key,value in weather.items():
        print(f'{key}:{value}')

# Step 4: Main program loop
while True:
    print("\n--- Weather App ---")
    city = input("Entr a city name (or q to quit): ")
    if city.lower() == 'q':
        break
    weather = get_weather(city)
    if weather:
        display_weather(weather)

            