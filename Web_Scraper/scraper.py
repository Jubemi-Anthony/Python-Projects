import requests
from bs4 import BeautifulSoup

url = "https://www.wikihow.com/Catch-a-Bird"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find_all('h1', {'class':'title_lg'})

for t in title:
    print(t.getText())