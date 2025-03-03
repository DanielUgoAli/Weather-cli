import datetime as dt
import json


def temperature(city: str, data: json):
    country_name = data["sys"]["country"]
    temp_in_celsius = (data["main"]["temp"])
    temp_in_fahrenheit = temp_in_celsius * (9/5) + 32
    temp_feels_like = data["main"]["feels_like"]
    weather_description = data["weather"][0]["description"]
    degree_sign = chr(176) # degree symbol from the standard ascii i think in hex blah blah blah....

    say = (
        f"It's {temp_in_celsius:.1f}{degree_sign}C in {city}, {country_name}\n"
        f"That's {temp_in_fahrenheit:.1f}{degree_sign}F in fahrenheit or freedom units\n"
        f"It feels more like {temp_feels_like:.1f}{degree_sign}C\n"
        f"Weather description: {weather_description}"
    )
    
    return temp_in_celsius, temp_in_fahrenheit, temp_feels_like, weather_description, degree_sign, say


def check_city_humidity(data: json):
    humidity = data["main"]["humidity"]
    if humidity >= 70:
        return f"Expect a lot of moisture, around{humidity}%"
    elif humidity <= 69 and humidity >= 50:
        return f"It's moderately humid today, with humidity at {humidity}%"
    else:
        return f"Humidity is around {humidity}% today"


def sunset_sunrise(data: json):
    sunset = dt.datetime.fromtimestamp(data["sys"]["sunset"] + data["timezone"])
    sunrise = dt.datetime.fromtimestamp(data["sys"]["sunrise"] + data["timezone"])
    
    return sunset, sunrise
