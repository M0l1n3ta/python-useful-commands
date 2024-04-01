import json 
from playwright.sync_api import sync_playwright 
 
with sync_playwright() as p: 
	for browser_type in [p.chromium, p.firefox, p.webkit]: 
		browser = browser_type.launch() 
		page = browser.new_page() 
		page.goto('https://httpbin.org/headers') 
		jsonContent = json.loads(page.inner_text('pre')) 
		print(jsonContent['headers']['User-Agent']) 
		browser.close()   