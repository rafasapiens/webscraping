'''
O programa a seguir
usa urllib.request.urlretrieve para fazer download de imagens de um URL
remoto:
'''

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup

#código obtido no github https://github.com/REMitchell/python-scraping/blob/master/Chapter09_StoringData.ipynb

print('Iniciando Scrap Download....\n')
html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('img', {'alt': 'python-logo'})['src']
urlretrieve (imageLocation, 'logo.jpg')
print('Download concluído!')

'''
código do Livro com erros
html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
imageLocation = bs.find('a', {'id': 'logo'})#.find(('img')['src'])
urlretrieve (imageLocation, 'logo.jpg')


Esse código faz o download do logo de http://pythonscraping.com e o
armazena como logo.jpg no mesmo diretório em que o script está
executando.
O código funciona bem se for necessário fazer o download de apenas um
arquivo e você souber como ele se chama e qual a sua extensão.
'''
