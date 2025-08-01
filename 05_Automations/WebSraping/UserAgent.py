import requests 
 
response = requests.get('http://httpbin.org/headers') 
print(response.json()['headers']['User-Agent']) 
# python-requests/2.25.1

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
response = requests.get('http://httpbin.org/headers', headers=headers) 
print(response.json()['headers']['User-Agent'])