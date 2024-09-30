import requests
import json
import os

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=7ed4ba4501904c57b0184745242408&q={city}"
    r = requests.get(url)
    dic = json.loads(r.text)
    
    # Extracting different weather details
    temp_c = dic["current"]["temp_c"]
    condition = dic["current"]["condition"]["text"]
    humidity = dic["current"]["humidity"]
    wind_kph = dic["current"]["wind_kph"]
    
    return temp_c, condition, humidity, wind_kph

def speak_weather(city, temp_c, condition, humidity, wind_kph):
    # Formulating the weather report
    weather_report = (
        f"The current weather in {city} is as follows: "
        f"The temperature is {temp_c} degrees Celsius with {condition}. "
        f"The humidity level is {humidity} percent, and the wind speed is {wind_kph} kilometers per hour."
    )
    
    # Using text-to-speech to announce the weather
    os.system(f"say '{weather_report}'")
    print(weather_report)

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    temp_c, condition, humidity, wind_kph = get_weather(city)
    speak_weather(city, temp_c, condition, humidity, wind_kph)
