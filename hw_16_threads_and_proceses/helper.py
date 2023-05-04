import requests


def find_and_add_city_coordinates(city, city_list_with_data):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city}

    res_ = requests.get(url=url, params=params).json()

    latitude = round(res_["results"][0]["latitude"], 2)
    longitude = round(res_["results"][0]["longitude"], 2)

    coordinates = {
        "city": city,
        "latitude": latitude,
        "longitude": longitude

    }

    city_list_with_data.append(coordinates)


def get_average_temperature_by_city(city):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": city["latitude"],
              "longitude": city["longitude"],
              "hourly": "temperature_2m"}

    res_ = requests.get(url=url, params=params)

    temperature = res_.json()["hourly"]["temperature_2m"]
    average_temperature = sum(temperature) / len(temperature)
    city["average_temperature"] = round(average_temperature, 2)
