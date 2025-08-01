import requests 
from bs4 import BeautifulSoup 
 
response = requests.get('https://scrapeme.live/shop/') 
soup = BeautifulSoup(response.content, 'html.parser') 
pages = soup.select('.woocommerce-pagination a.page-numbers:not(.next)') 
print(pages[0].get('href')) # https://scrapeme.live/shop/page/2/ 
print(pages[-1].get('href')) # https://scrapeme.live/shop/page/48/