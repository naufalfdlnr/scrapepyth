import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://cellbuddy.in/buddy/store/apple-iphone-7-no-touch-id/'


data = []
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
script = soup.find('script', type='application/ld+json')
str = script.text.strip()
str = re.sub(r'[\\/@]', '', str)
str = re.sub(r'\b u?2\d{3}\b', '', str)
array = json.loads(str.encode().decode('unicode-escape'))
src = data.append(array)

print(data)


