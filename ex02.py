import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")

autores = soup.find_all('small', class_='author')
for autor in autores:
    print(autor.text)


