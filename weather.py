import requests

city='London'

url = 'http://api.weatherapi.com/v1/current.json?key=b9523f89f0774b9484825404251102&q='+ city +'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')

print("Today's weahter in " , city ," is", description, 'and', temp, 'degrees')