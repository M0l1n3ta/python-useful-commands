import requests 
 
proxies = {'http': 'http://80.228.235.6:80'} 
response = requests.get('http://httpbin.org/ip', proxies=proxies) 
print(response.json()['origin']) # 190.64.18.162


response = requests.get('https://www.paddypower.com/inplay?tab=football', proxies=proxies)
print(response.json())