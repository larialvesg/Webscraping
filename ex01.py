import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.title
print("O titulo da pagina html é",*titulo)
