import ipinfo
import requests #http://docs.python-requests.org/en/latest/
from requests import get
import json
# get external ip using http request from ipify
external_ip = get('https://api.ipify.org').content.decode('utf8')

# get city & country according to external ip using ipinfo library
ipinfo_token = 'd5a13af3bebba0'
handler = ipinfo.getHandler(ipinfo_token) # create object handler 
ipinfo_details = handler.getDetails(external_ip) # use getDetails property
city = ipinfo_details.city
country = ipinfo_details.country
# get temp with respect to city & country 
weatherReq = requests.get('http://api.openweathermap.org/data/2.5/weather?units=metric&q='+city+','+country+'&APPID=0a1e14ce198f208c5665f1b1a6bb4879').text
# parse response using json
data = json.loads(weatherReq)
temp=data['main']['temp']
# format response as json 
value = {
        "city": city,
        "country": country,
        "temp": temp,
        }
jsonString = json.dumps(value)
print(jsonString)