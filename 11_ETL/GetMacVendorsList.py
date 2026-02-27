import requests 
from bs4 import BeautifulSoup 

url = 'https://standards-oui.ieee.org/oui/oui.txt'
user_agent = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url, allow_redirects=True, headers = user_agent) 

soup = BeautifulSoup(response.content, 'html.parser') 

print(f"Content: {soup.prettify()[:1000]}")