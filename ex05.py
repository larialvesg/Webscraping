import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

categorias = soup.find_all('div', class_='tags')
citacoes = soup.find_all('span', class_='text')
print(categorias)

for citacao, categoria in zip(citacoes, categorias):
    tags = categoria.find_all("a")
    print(f"A sua citação é", citacao.text, end='\ncategorias: ')
    for tag in (tags):
        print(f"{tag.text}",end='; ')
    print('\n')
