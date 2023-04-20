# Import the necessary libraries
## pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests


proxy = '165.225.202.44:443'
proxies = {'http': proxy, 'https': proxy}
response = requests.get("https://www.meneame.net/queue", proxies=proxies, verify=False)

# Parse the HTML or XML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Extract the desired data using Beautiful Soup's methods and attributes
#data = soup.find("div", {"id": "data"})


data = soup.select('div.link')
# Print the data to the console
# take content and store in variable
content = data[0].text.strip()

# print content
print(content)