from bs4 import BeautifulSoup
import requests

url = "https://www.allnigerianrecipes.com/"

siteText = requests.get(url).text

soup = BeautifulSoup(siteText, 'lxml')

recipies = soup.find_all('div', class_ = 'listing-item')

rec = ""

for recipie in recipies:
    title = recipie.find('a', class_ = 'title').text
    link = recipie.a['href']
    rec += f"Meal: {title}, Link: {link} \n"

myfile = open('RECIPIES.txt', 'w')
myfile.write(rec)
myfile.close()
print('DONE')