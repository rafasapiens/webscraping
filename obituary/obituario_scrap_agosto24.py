from bs4 import BeautifulSoup
import requests
import csv

#Cria o arquivo .csv
arquivo_csv = open('obituario_agosto2024.csv', 'w')
escritor = csv.writer(arquivo_csv)
#Primeira linha do arquivo csv
escritor.writerow(['Id','Nome','Sobrenome','Nascimento','Obito'])

#Inicio do scrap
# Número do id a ser buscado do site
id=26215
while id<26795:
    id=id+1
    print(' ')
    print(id)

    #arquivo_csv = open('obituario.csv', 'w')
    escritor = csv.writer(arquivo_csv)


    #site do scrap
    site = requests.get(f'https://www.lformolo.com.br/obituario.php?id_atendimento={id}').content

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
#Salva os dados do scrap em arquivo .csv

import csv

arquivo_csv = open('obituario.csv', 'w')

escritor = csv.writer(arquivo_csv)

escritor.writerow(['Id','Nome','Sobrenome','Nascimento','Obito'])

escritor.writerow([id,busca_nome,busca_sobrenome,nasc,obito])

arquivo_csv.close()

'''


