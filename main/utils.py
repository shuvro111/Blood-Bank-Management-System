#import models
from .models import *

#geolocation
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

#geo ip
from django.contrib.gis.geoip2 import GeoIP2

#helper functions
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


def get_distance(location, destination):
    distance = round(geodesic(location, destination).km, 2)

    return distance
