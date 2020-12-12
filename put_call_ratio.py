#!pip3 install requests
#!pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = 'https://markets.cboe.com/us/options/market_statistics/daily/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='daily-market-stats-data')
date = soup.find(id='stats-date-header')

from prettytable import from_html

x = from_html(str(results))

print(date.text.strip())
print(x[0])