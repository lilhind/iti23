class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

class QueueOutOfRangeException(Exception):
    pass

class Queue2(Queue):

    queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.queue = []
        Queue2.queues[name] = self

    def insert(self, item):
        if len(self.queue) == self.size:
            raise QueueOutOfRangeException("Queue is full")
        else:
            self.queue.append(item)



    
###################################################################


import requests
from geopy import geocoders

class WeatherAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_temperature(self, city):
        latitiude, longitude = self.get_lat_and_long("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitiude}&lon={longitude}&appid={self.api_key}"
        response = requests.get(url)
        tp = ""
        if response.status_code == 200:
            print("code 200")
            data = response.json()
            dt = data["main"]["temp"]    
            return str(dt)
        else:
            print("error")
        
        return None

    def get_lat_and_long(self, city):
        gn = geocoders.GeoNames(username="zzbdjgi")
        place, (latitiude, longitude) = gn.geocode(city)
        return latitiude, longitude
    




# create weather api client

weather = WeatherAPIClient("152808cf5497c163ad774bf65018f6f5")

# get current temperature

tp = weather.get_current_temperature("cairo")

print(tp)
