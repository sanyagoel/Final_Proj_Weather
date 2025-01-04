import os
from flask import Flask, render_template,request
from weather import getWeather


app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template("index.html")

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    data = getWeather(city)
    # data["main"]["feels_like"]
    #data["main"]["temp"]
    #data["weather"]["description"]
    #data["cod"]
    if not data["cod"]==200:
        return render_template("notFound.html")
    if not city.strip() :
        city = "Gurgaon"
    return render_template("result.html",feelsLike = data["main"]["feels_like"], temp = data["main"]["temp"] , description = data["weather"][0]["description"].capitalize(), city = city
)

    

app.run(host='0.0.0.0', port = 8000)

