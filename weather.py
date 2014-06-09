"""
Written by: Anand Reddy Pandikunta
e-mail: anand21nanda@gmail.com

Forked Author: Akshay Verma
"""

import urllib.request
import json

def get_ip():
    '''
    get ip across LAN from api
    '''
    url = 'http://ip-api.com/json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'})
    json_html = urllib.request.urlopen(req).read()
    json_reply = json.loads(json_html.decode('UTF-8'))
    addr = json_reply['query']
    return addr

def get_weather(addr):
    '''
    get weather based on ip
    '''
    end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?"
    query = "key=a37fae643df77aa83d88abbc9e8e96194ab242d4&q=" + str(addr) + "&num_of_days=0&format=json"
    url = end_point +  query
    json_data = urllib.request.urlopen(url).read()
    weather_data = json.loads(json_data.decode('UTF-8'))
    current_weather = weather_data['data']['current_condition'][0]
    return current_weather

def print_weather(weather_data):
    '''
    parse and print weather
    '''
    print("""
    Weather : %s 
    Temperatue : %s Celsius
    Wind : %s Kmph %s 
    Humidity : %s 
    Precipitation : %s MM
    """ % (weather_data['weatherDesc'][0]['value'], weather_data['temp_C'], weather_data['windspeedKmph'], weather_data['winddir16Point'], weather_data['humidity'], weather_data['precipMM']))


if __name__ == "__main__":
    print("\nGetting weather information for your location...")
    addr = get_ip()
    weather_data = get_weather(addr)
    print_weather(weather_data)
