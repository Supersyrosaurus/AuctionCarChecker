import requests
from bs4 import BeautifulSoup
#URL = get('https://autotrader.co.uk')
URL = requests.get('https://www.salvagemarket.co.uk')
print(URL.status_code)
#print(URL.content)
soup = BeautifulSoup(URL.content, 'html5lib')
print(soup.prettify())
