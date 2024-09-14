from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://pt.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #Encontramos uma página nova
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')

#http://en.wikipedia.org{}'

'''
Um aviso quanto à recursão
Este é um aviso raramente visto em livros de software, mas achei que você deveria saber: se
deixar o programa anterior executando por tempo suficiente, é quase certo que ele
apresentará uma falha.
Python tem um limite default para recursão (o número de vezes que um programa pode
chamar a si mesmo recursivamente) igual a 1.000. Como a rede de links da Wikipédia é
extremamente grande, em algum momento esse programa atingirá esse limite de recursão e
será interrompido, a menos que você coloque um contador de recursão ou algo para impedir
que isso aconteça.
Para sites “planos”, com menos de 1.000 links de profundidade, esse método em geral
funciona bem, com algumas exceções incomuns. Por exemplo, uma vez, encontrei um bug em
um URL gerado dinamicamente, que dependia do endereço da página atual para escrever o
link nessa página. Isso resultava em paths se repetindo infinitamente, por exemplo,
/blogs/blogs.../blogs/blog-post.php.
Na maioria das ocasiões, porém, essa técnica recursiva não deverá apresentar problemas
para qualquer site típico que você possa encontrar.
'''
