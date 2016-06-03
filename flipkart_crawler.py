import json
import requests
from bs4 import BeautifulSoup

# Seed URL to crawl
seed_url = 'http://www.flipkart.com/search?q=mobiles&as=off&as-show=on&otracker=start'

# Get source code of Seed URL
source_code = requests.get(seed_url)
html_doc = source_code.text

# Create object of `BeautifulSoup`
soup = BeautifulSoup(html_doc, 'lxml')
page_description = soup.find('meta', attrs={ "name": "Description" })

products_list = {
    "title": soup.title.string.strip(),
    "description": page_description.get('content'),
    "productDetails": []
}

products = soup.find_all('div', { "class": "product-unit" })
for product in products:
    product_image_tag = product.find('img')
    product_image = product_image_tag.get('data-src')
    product_title_wrapper = product.find('div', { "class": "pu-title" })
    product_title = product_title_wrapper.a.string.strip()
    products_list['productDetails'].append({
        "title": product_title,
        "link": product_title_wrapper.a.get('href'),
        "image_url": product_image
    })

# Display products dictionary
print json.dumps(products_list, sort_keys=True, indent=4)

# Write in a JSON file
file_handle = open('flipkart.json', 'w')
file_handle.write(json.dumps(products_list))
file_handle.close()

# Read from the JSON file
file_handle = open('flipkart.json', 'r')
file_data = json.loads(file_handle.read())
print file_data
