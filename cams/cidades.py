import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get('http://www.insecam.org/en/mapcity/', headers=headers).content

'''
url = 'URL_DA_PÁGINA_AQUI'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Resto do código igual ao exemplo anterior...


from bs4 import BeautifulSoup

html = 
<a href="/en/bycity/Arezzo/"> Arezzo / ( 1)</a> <br>
<a href="/en/bycity/Armenis/"> Armenis / ( 2)</a> <br>
<a href="/en/bycity/Arnold/"> Arnold / ( 1)</a> <br>
... (seu HTML completo aqui) ...
<a href="/en/bycity/Balti/"> Balti / ( 1)</a> <br>

'''
soup = BeautifulSoup(html, 'html.parser')
cities = []

for link in soup.find_all('a', href=lambda href: href and '/en/bycity/' in href):
    city_full = link.text.strip()
    # Extrai apenas o nome da cidade antes da barra
    city_name = city_full.split('/')[0].strip()
    cities.append(city_name)

# Remover duplicatas (opcional)
unique_cities = list(dict.fromkeys(cities))  # Mantém a ordem original

print("Lista de cidades:")
for city in unique_cities:
    print(city)



soup = BeautifulSoup(html, 'html.parser')
cidades_links = []

# Iterar por todas as tags <a>
for link in soup.find_all('a'):
    url = link.get('href')
    nome_cidade = link.text.split('/')[0].strip()
    cidades_links.append({"Cidade": nome_cidade, "Link": url})

# Exibir resultados
for item in cidades_links:
    print(f"Cidade: {item['Cidade']}, Link: {item['Link']}")
