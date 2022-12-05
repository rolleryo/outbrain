import ipinfo
# requests library:  http://docs.python-requests.org/en/latest/
from requests import get
import requests

#ip_address = get('https://api.ipify.org').content.decode('utf8')
#print('My public IP address is: {}'.format(ip))

ipinfo_token = 'd5a13af3bebba0'
handler = ipinfo.getHandler(ipinfo_token)
ip_address = ip = get('https://api.ipify.org').content.decode('utf8')
ipinfo_details = handler.getDetails(ip_address)
city = ipinfo_details.city
country = ipinfo_details.country
x = requests.get('http://api.openweathermap.org/data/2.5/weather?units=metric&q='+city+','+country+'&APPID=0a1e14ce198f208c5665f1b1a6bb4879')
print(x.text)