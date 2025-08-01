import requests
from bs4 import BeautifulSoup

# initialize the list of discovered urls
# with the first page to visit
urls = ["https://scrapeme.live/shop/"]
url_list = []
# until all pages have been visited
while len(urls) != 0:
    # get the page to visit from the list
    current_url = urls.pop()
    url_list.append(current_url)
    # crawling logic
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element['href']
        if ("https://scrapeme.live/shop" in url) and (url not in urls) and (url not in url_list):
            urls.append(url)

print(url_list)
