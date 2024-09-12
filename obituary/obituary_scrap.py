from bs4 import BeautifulSoup
import requests

id=12874
while id<25000:
    id=id+1
    print(' ')
    print(id)
    site = requests.get(f'https://www.lformolo.com.br/obituario.php?id_atendimento={id}').content  #input('Digite o URL para fazer o scrapy: ')).content   #('https://www.lformolo.com.br/obituario.php?id_atendimento=18785  https://www.climatempo.com.br/').content

    soup = BeautifulSoup(site, 'html.parser')
    '''
print(soup.prettify())

busca_span = soup.find('span') #, class_="-gray-dark-2 -font-base -bold")

print(busca_span.string)

print(soup.title)

print(soup.title.string)

print(soup.a)
print(soup.a.string)

#print(soup.h1.string)
    '''
    #busca_p = soup.find_all('h2')
    busca_nome = soup.find('h2', class_='nome').get_text()
    print(busca_nome)
    busca_sobrenome = soup.find('h2', class_='sobrenome').get_text()
    print(busca_sobrenome)
    #print(soup.h2.string)
    #print(soup.p.string)
    nasc=soup.find('div', class_='data nascimento').get_text()
    print(nasc)
    obito=soup.find('div', class_='data falecimento').get_text()
    print(obito)
