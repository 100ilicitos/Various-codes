# Get address detail
# by Busyman.Inc

# pip install geopy

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geopi")
a = input("Enter the zipcode: ")
zipcode = a

location = geolocator.geocode(zipcode)

print("Zipcode:", zipcode)
print("Details of Zipcode: ")
print(location)
