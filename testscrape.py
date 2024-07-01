import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://cellbuddy.in/buddy/store/page/'
detail_data = []
pages = []
# page = 0
for y in range(1,13)  :
    pages.append(url + str(y))

link_product = []

for link_page in pages:
    req = requests.get(link_page)
    soup_link_product = BeautifulSoup(req.content, 'html.parser')
    element = ','.join([a.get('href') for a in soup_link_product.find_all('a',{'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})])
    link_product.extend(element.split(','))
    # print(link_product)

del link_product[-1]

for prod in link_product:
    req = requests.get(prod)
    soup_product = BeautifulSoup(req.content, 'html.parser')
    data_script = soup_product.find('script', {'type' : "application/ld+json"})
    data_prod = data_script.text.strip()
    data_prod = re.sub(r'[\\/@]|(\b u?2\d{3}\b)', '', data_prod)
    print(data_prod)
    data_prod = json.loads(data_prod.encode().decode('unicode-escape'))
    results = detail_data.extend({
        'brand': 'Apple',
        'name' : data_prod['name'],
        # 'price' : d['offers'][0]['']
    })
    print('inserting.. ')
    print(data_prod['name'])
            
        
    # print(array)

print(detail_data)
# print(link_product)


