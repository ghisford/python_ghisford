# from unittest import result
import requests

def get_data(city):
    api_key = '02332cebe46b0b980cd24a7cdaa6ef11'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    r =  requests.get(url)

    json_object = r.json()
    return json_object

# get_data('london')
def print_data(data):
    weather = 'the weather in {} is {} '.format(data['name'],data['weather'][0]['main'])
    return weather
# print_data(get_data('london'))

def save_data():
    with open('weather.txt','w') as fin:
        fin.write(print_data(get_data('london')))

def read_data():
    with open('weather.txt') as out:
        out.readlines()

save_data()