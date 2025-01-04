from dotenv import load_dotenv

import requests

from pprint import pprint


load_dotenv()

import os

def getWeather(city):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    
    data = requests.get(url).json()
    
    # data["main"]["feels_like"]
    #data["main"]["temp"]
    #data["weather"]["description"]
    #data["cod"]
    
    pprint(data)
    return data 
    

if __name__ == "__main__":
    
    city = input("Enter the city")
    
    data = getWeather(city)
    
    print(data)
    
    
    