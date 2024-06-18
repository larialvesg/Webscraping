import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")

autores = soup.find_all('small', class_='author')
citacoes = soup.find_all('span', class_='text')


for autor, citacao in zip(autores, citacoes):
    print(f"O autor é {autor.text} e a sua citação é {citacao.text}")





