import requests
from bs4 import BeautifulSoup

url = "https://insanelygoodrecipes.com/nigerian-foods/"

siteContent = requests.get(url).text
soup = BeautifulSoup(siteContent, 'lxml')
recipies = soup.find_all('h2', class_ = 'wp-block-heading')

rec = ''

for recipie in recipies:
    title = recipie.a.text
    link = recipie.a['href']

    rec += f"Meal: {title}, Link: {link} \n"

myfile = open('RECIPIES.txt', 'a')
myfile.write(rec)
myfile.close()
print('DONE')
