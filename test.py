from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/race_control?flag=BLACK%20AND%20WHITE&driver_number=1&date>=2023-01-01&date<2023-09-01')
data = json.loads(response.read().decode('utf-8'))
print(data)