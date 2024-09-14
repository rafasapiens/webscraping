print(
'‐‐----------------------------------------------------------------------\n'
'Simbolos |     Significado                       | Exemplo   | Ex.Corresp.|\n'
'    *    | Faz a correspondência com o caractere,|  a*b*     | aaaaaaaa,  |\n'
'         | a subexpressão ou o caractere entre   |           | aaabbbbb,  |\n'
'         | colchetes anterior, 0 ou mais vezes.  |           | bbbbbb     |\n'
'------------------------------------------------------------------------- |\n'
'    +    |Faz a correspondência com o caractere, |  a+b+     | aaaaaaaab, |\n'
'         |a subexpressão ou ocaractere entre     |           | aaabbbbb,  |\n'
'         |colchetes anterior, 1 ou mais vezes.   |           | abbbbbb    |\n'
'------------------------------------------------------------------------- |\n'
'    []   |Faz a correspondência com qualquer     |  [A-Z]*   | APPLE,     |\n'
'         |caractere entre os colchetes (isto é,  |           | CAPITALS,  |\n'
'         |“Escolha qualquer um destes itens”).   |           | QWERTY     |\n'
'------------------------------------------------------------------------- |\n'
'    ()   |Uma subexpressão agrupada (são avaliadas  (a*b)*   | aaabaab,   |\n'
'         |antes, na "ordem de operações" das     |           | abaaab,    |\n'
'         |expressões regulares).                 |           | ababaaaaab |\n'
'------------------------------------------------------------------------- |\n'
'  {m, n} |Faz a correspondênciq com o caractere, |a{2,3}b{2,3} aabbb,     |\n'
'         |a subexpressão ou o caractere entre    |           | aaabbb,    |\n'
'         |colchetes anterior, entre m e n vezes  |           | aabb       |\n'
'         |(inclusive).                           |           |            |\n'
'------------------------------------------------------------------------- |\n'
'         |                                       |           |            |\n'
'         |                                       |           |            |\n'
'         |   VERIFIQUE OUTROS EXEMPLOS NA        |           |            |\n'
'         |   PÁGINAS 43 E 44 DO LIVRO            |           |            |\n'
'         |   "WEB SCRAPING COM PYTHON"           |           |            |\n'
'         |                                       |           |            |\n'
)



'''# Um exemplo clássico de expressões regulares pode ser visto na prática de
identificação de endereços de email. '''

#  [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)i

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

