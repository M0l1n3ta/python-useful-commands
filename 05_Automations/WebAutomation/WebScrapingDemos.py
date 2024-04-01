# Import the necessary libraries
## pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#proxy = '165.225.202.44:443'
#proxies = {'http': proxy, 'https': proxy}
response = requests.get("https://www.meneame.net/queue",headers=headers,  verify=False)

# Parse the HTML or XML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Extract the desired data using Beautiful Soup's methods and attributes
#data = soup.find("div", {"id": "data"})


data = soup.select('div.link h2')
# Print the data to the console
# take content and store in variable
for x in data:
    print(x.text.strip())  

