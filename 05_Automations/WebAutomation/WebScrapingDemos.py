# Import the necessary libraries
## pip install beautifulsoup4 requests tabulate
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

elements = []

#proxy = '165.225.202.44:443'
#proxies = {'http': proxy, 'https': proxy}
response = requests.get("https://www.meneame.net/queue", headers=headers)

# Parse the HTML or XML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Extract the desired data using Beautiful Soup's methods and attributes
#data = soup.find("div", {"id": "data"})


data = soup.select('div.center-content')
# Print the data to the console
# take content and store in variable
for x in data:
    new_element = {
        "title": x.find("a").text.strip(),
        "url": x.find("a").get("href")
    }
    #elements.append({f'"title": "{x.text.strip()}", "url": "{x.find("a").get("href")}"'})
    elements.append(new_element)
    print(f"elemento añadido: {x.text.strip()}")  


# Función para truncar texto
def truncate(text, max_length):
    return text if len(text) <= max_length else text[:max_length - 3] + '...'

# Limitar tamaño de columnas
max_title_len = 80
max_url_len = 50

# Convert to list of lists for tabulate

table = [[truncate(el['title'], max_title_len), truncate(el['url'], max_url_len)] for el in elements]


# Print the table
print(tabulate(table, headers=["Title", "URL"], tablefmt="grid"))


# Define the CSV file name
csv_file = "elements.csv"

# Write the list to a CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(elements)

print(f"The table has been successfully stored in '{csv_file}'.")
