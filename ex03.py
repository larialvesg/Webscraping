import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")

categorias = soup.find_all('a', class_='tag')

print("As categorias são: ")
for categoria in categorias:
    print(categoria.text.title())









