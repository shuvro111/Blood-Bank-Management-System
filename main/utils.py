#import models
from .models import *

# geolocation
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# geo ip
from django.contrib.gis.geoip2 import GeoIP2
import socket
import requests

# helper functions
geolocator = Nominatim(user_agent="main")


def get_location(ip_address):
    g = GeoIP2()
    country = g.country(ip_address)
    city = g.city(ip_address)
    location = g.lat_lon(ip_address)

    return location


def get_destination(city):
    des = geolocator.geocode(city)
    address = des.address
    destination = (des.latitude, des.longitude)

    return destination


def sort_nearest():
    distance_list = []

    # get donors
    donors = Donor.objects.all()
    # get ip from socket module
    hostname = socket.gethostname()
    #ip_address = socket.gethostbyname(hostname)
    my_ip_address = '103.54.150.241'

    # get user location by ip_address
    location = get_location(my_ip_address)

    for donor in donors:
        # get donors location by city
        city = donor.city
        destination = get_destination(city)
        distance, duration = get_distance_data(location, destination)

        distance_obj = {
            'donor': donor,
            'distance': distance,
            'duration': duration
        }

        distance_list.append(distance_obj)

    sorted_distance = sorted(distance_list, key=lambda x: x['distance'])

    return sorted_distance


def get_distance_data(location, destination):
    distance_dict = {}
    url = f'https://api.distancematrix.ai/maps/api/distancematrix/json?origins={location}&destinations={destination}&key=bFMS21YWgeULK0I61v4pOwGFj9SpY'
    response_data = requests.get(url)
    response = response_data.json()
    distance = int(response['rows'][0]['elements']
                   [0]['distance']['value']) / 1000
    duration = response['rows'][0]['elements'][0]['duration']['text']

    distance_list = [distance, duration]
    return distance_list
