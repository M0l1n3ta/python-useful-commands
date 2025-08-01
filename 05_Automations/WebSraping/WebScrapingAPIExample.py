import requests
import json
from jsonpath_ng import jsonpath, parse
import cloudscraper

# Replace 'your_endpoint_url' with the actual URL you want to call
endpoint_url = 'https://a.4cdn.org/boards.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

# Make a GET request
response = requests.get(endpoint_url, headers=headers)

json_formatted_str = json.dumps(response.json(), indent=4)
print(json_formatted_str)


scraper = cloudscraper.create_scraper() 
match_response = scraper.get(endpoint_url)
json_formatted_str = json.dumps(match_response.json(), indent=4)
print(json_formatted_str)

with open(f'./05_Automations/WebSraping/Data/4ChanBoardsData.json', 'w', encoding='utf-8') as f:
    json.dump(match_response.json(), f, ensure_ascii=False, indent=4)


jsonpath_expression = parse('boards[*].title')

for match in jsonpath_expression.find(match_response.json()):
    print(f'Board title: {match.value}')