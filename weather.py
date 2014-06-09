"""
Written by: Anand Reddy Pandikunta
e-mail: anand21nanda@gmail.com

Forked Author: Akshay Verma
"""

import re
import urllib.request
import json

def get_ip():
    '''
    get ip across LAN from api
    '''
    #~ url = 'https://www.whatismyip.com/'
    url = 'http://ip-api.com/json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'})
    json_html = urllib.request.urlopen(req).read()
    jsonReply = json.loads(json_html.decode('UTF-8'))
    ip_address = jsonReply['query']
    return ip_address

def get_weather(ip_address):
    end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?" 
    query = "key=a37fae643df77aa83d88abbc9e8e96194ab242d4&q=" + str(ip_address) + "&num_of_days=0&format=json"
    url = end_point +  query
    json_data = urllib.request.urlopen(url).read()
    data = json.loads(json_data.decode('UTF-8'))
    current_weather = data['data']['current_condition'][0]
    return current_weather

def print_weather(data):
    print ("""
    Weather : %s 
    Temperatue : %s Celsius
    Wind : %s Kmph %s 
    Humidity : %s 
    Precipitation : %s MM
    """ % (data['weatherDesc'][0]['value'], data['temp_C'], data['windspeedKmph'], data['winddir16Point'], data['humidity'], data['precipMM']))


def main():
    print ("\nGetting weather information for your location...")
    ip_address = get_ip()
    data = get_weather(ip_address)
    print_weather(data)


if __name__ == "__main__":
    main()
