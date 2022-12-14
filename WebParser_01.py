import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://porno-island.site/games/"
r = requests.get(URL_TEMPLATE)
if (r.status_code == 200):
    soup = bs(r.text, "html.parser")
    ElemsArr = soup.find_all('h4', class_="short-link")
    max_count = 5
    index = 0
    for elem in ElemsArr:
        if index < max_count:
            index = index + 1
            print(elem.a['title'])
else:
    print(r.status_code)

