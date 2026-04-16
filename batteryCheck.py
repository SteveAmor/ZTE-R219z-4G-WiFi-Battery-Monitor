import requests
from datetime import datetime

time = str(int(datetime.now().timestamp()))
url = 'http://192.168.0.254/goform/goform_get_cmd_process?multi_data=1&isTest=false&cmd=battery_value,battery_charging&_=' + time
response = requests.get(url, headers=({'referer':'http://192.168.0.254/index.html'}))
print(response.json())
response_dict = response.json()
print(response_dict['battery_value'])
print(response_dict['battery_charging'])
