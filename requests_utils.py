import requests
from keys import RAPID_API_KEY


def find_location(location_name):
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchLocation"
    params = {
        "query": location_name,
    }
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    geo_id = data["data"][0]["geoId"]
    return geo_id


def find_hotels(geo_id, checkin, checkout, sort, rating, adults, rooms, priceMin=0, priceMax=100000):
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotels"

    querystring = {"geoId": geo_id, "checkIn": checkin, "checkOut": checkout, "pageNumber": "1",
                   "currencyCode": "EUR", "sort": sort, "rating": rating, "adults": adults, "rooms": rooms, "priceMin": priceMin, "priceMax": priceMax}
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(url=url, headers=headers, params=querystring)
    data = response.json()
    return data["data"]["data"][0:10]


def request_hotels(location_name, checkin, checkout, sort, rating, adults, rooms, priceMin, priceMax):
    geo_id = find_location(location_name)
    hotels = find_hotels(geo_id, checkin, checkout, sort, rating, adults, rooms, priceMin, priceMax)
    return hotels
