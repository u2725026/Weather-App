import requests
import string
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Token to get location  for ip info
token = "81ebde365bc0dd"

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "thisisasecret"
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


# public ip function
def public_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    return response.json()["ip"]


# function to retrieve location from ip
def get_location(ip):
    url = f"https://ipinfo.io/{ip}/json?token={token}"
    response = requests.get(url)
    data = response.json()
    return data


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=a67dc9788b42ec743f9ea12b1a6f8bcc"
    r = requests.get(url).json()
    return r


@app.route("/")
def index_get():
    user_ip = public_ip()
    location = get_location(user_ip)

    cities = City.query.all()

    weather_data = []

    geo_data = get_weather_data(location["city"])

    for city in cities:
        r = get_weather_data(city.name)
        weather = {
            "city": city.name,
            "temperature": r["main"]["temp"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"],
        }
        weather_data.append(weather)

    return render_template("weather.html", weather_data=weather_data, location=geo_data)


@app.route("/", methods=["POST"])
def index_post():
    err_msg = ""
    new_city = request.form.get("city")
    new_city = new_city.lower()
    new_city = string.capwords(new_city)
    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()

        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data["cod"] == 200:
                new_city_obj = City(name=new_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = "That is not a valid city!"
        else:
            err_msg = "City already exists in the database!"

    if err_msg:
        flash(err_msg, "error")
    else:
        flash("City added successfully!", "success")

    return redirect(url_for("index_get"))


@app.route("/delete/<name>")
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f"Successfully deleted { city.name }!", "success")
    return redirect(url_for("index_get"))
