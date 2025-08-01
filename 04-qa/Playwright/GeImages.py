from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor
import requests
from PIL import Image
import os
import io

def img_down(link):
    response  = requests.get(link) 
    image_file = io.BytesIO(response.content)
    image  = Image.open(image_file)
    filePath = os.path.join('D:/Datos/Output/images', link.split('/')[-1])
    print(filePath)
    with open(filePath , "wb") as f:
          image.save(f , "WEBP")
          print("Success!!!!")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        #base_url ='https://free-images.com/'
        base_url = 'https://rarehistoricalphotos.com/mesoamerica-south-america-expeditions-photos/'
        page.goto(base_url)
        print("Visiting Free Images.com....")
        img_lst = []
        all_links = page.query_selector_all('.wp-caption.aligncenter img')
        for link in all_links:
            img_lst.append(link.get_attribute('src'))

        print("Total Images Found: ", len(img_lst))
        print("Downloading Images....")
        return img_lst
    
if __name__ == '__main__':
     all_images = main()
     with ThreadPoolExecutor(max_workers=10) as executor:
          executor.map(img_down , all_images)
     print("All Images Downloaded Successfully")