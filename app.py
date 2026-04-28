import requests
from dotenv import load_dotenv
import os


load_dotenv()

API = os.getenv("api_key")
place = input("city : ")
country = input("country code : ")


URL = f"https://api.openweathermap.org/data/2.5/weather?q={place},{country}&APPID={API}&units={'metric'}"

def get_weather():
    response = requests.get(URL)
    data = response.json()
    wind = data['wind']
    main_data= data['main']
    
    weather_data= {
        'temprature' : main_data['temp'],
        'pressure': main_data['pressure'],
        'feels like' : main_data['feels_like'],
        'wind': wind['speed']
    }
    return weather_data

x = get_weather()
print(f"Temprature outside is : {x['temprature']} degree celsius\nPresssure is : {x['pressure']}hpa\nIt Feels like : {x['feels like']} degree celsius\nWind Speed is : {x['wind']} knots")