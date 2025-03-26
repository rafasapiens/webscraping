from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get('http://www.insecam.org/en/view/1010803', headers=headers).content #'http://www.insecam.org'
#print(html)

soup = BeautifulSoup(html, 'html.parser')
cameras = []

# Encontrar todos os elementos de câmera
for cam in soup.select('div.col-xs-12.col-sm-6.col-md-4.col-lg-4'):
    link = cam.find('a')
    if link:
        camera_data = {
            'title': link.get('title', '').strip(),
            'url': link.get('href', '').strip(),
            'image': link.find('img').get('src', '').strip() if link.find('img') else '',
            'location': link.get_text(strip=True).split('\n')[-1]  # Pega o texto após a quebra de linha
        }
        cameras.append(camera_data)

# Exibir resultados
for idx, cam in enumerate(cameras, 1):
    print(f'Câmera {idx}:')
    print(f'Título: {cam["title"]}')
    print(f'URL: {cam["url"]}')
    print(f'Imagem: {cam["image"]}')
    print(f'Localização: {cam["location"]}\n')





'''
from bs4 import BeautifulSoup
import requests
import csv

#Cria o arquivo .csv
arquivo_csv = open('Cams.csv', 'w')
escritor = csv.writer(arquivo_csv)
#Primeira linha do arquivo csv
escritor.writerow(['Id','Title','Link','Nascimento','Obito'])

#Inicio do scrap
# Número do id a ser buscado do site
id= 29377
while id<29728:
    id=id+1
    print(' ')
    print(id)

    #arquivo_csv = open('obituario.csv', 'w')
    escritor = csv.writer(arquivo_csv)


    #site do scrap
    site = requests.get(f'https://lformolo.com.br/obituario/post.php?id_atendimento={id}').content                         #'https://www.lformolo.com.br/obituario.php?id_atendimento={id}').content
    soup = BeautifulSoup(site, 'html.parser')


    # filtra nome
    busca_nome = soup.find('h2', class_='nome').get_text()
    print(busca_nome)

    # filtra sobrenome
    busca_sobrenome = soup.find('h2', class_='sobrenome').get_text()
    print(busca_sobrenome)

    #filtra nascimento
    nasc=soup.find('div', class_='data nascimento').get_text()
    print(nasc)

    #filtra obito
    obito=soup.find('div', class_='data falecimento').get_text()
    print(obito)

    escritor.writerow([id,busca_nome,busca_sobrenome,nasc,obito])

    #arquivo_csv.close()                                        
    print(' ')
    print('Adicionado ao banco de dados')

arquivo_csv.close()
'''
