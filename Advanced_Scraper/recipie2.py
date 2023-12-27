import requests
from bs4 import BeautifulSoup

url = "https://www.food.com/ideas/all-time-best-dinner-recipes-6009#c-636919"
htmlText = requests.get(url).text
soup = BeautifulSoup(htmlText, 'lxml')

recipies = soup.find_all('div', class_ = "smart-card container-sm recipe")

rec = ""

for recipe in recipies:
    title = recipe.h2.text
    link = recipe.h2.a['href']
    rec += f"Meal: {title}, Link: {link} \n"

myfile = open('RECIPIES.txt', 'a')
myfile.write(rec)
myfile.close()
print('DONE')