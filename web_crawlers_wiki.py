from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])


'''
Se analisarmos os links que apontam para
páginas de artigos (em oposição a outras páginas internas), veremos que
todos eles têm três características em comum:
• Estão na div com o id definido com bodyContent.
• Os URLs não contêm dois-pontos.
• Os URLs começam com /wiki/.
Essas regras podem ser usadas para uma pequena revisão no código a fim
de obter somente os links desejados para artigos, usando a expressão
regular ^(/wiki/)((?!:).)*$"):
'''
print('\n'*5,'----->>> RESULTADO DO CÓDIGO REVISADO')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

'''
Se esse código for executado, veremos uma lista de todos os URLs de
artigos para os quais o artigo da Wikipédia sobre Kevin Bacon aponta.
É claro que ter um script que encontre todos os links de artigos em um
único artigo da Wikipédia previamente definido, apesar de ser interessante,
é um tanto quanto inútil na prática. É necessário transformar esse código
em algo mais parecido com o seguinte:
• Uma única função, getLinks, que receba um URL de um artigo da
Wikipédia no formato /wiki/<Nome_do_Artigo> e devolva uma lista com os
URLs de todos os artigos associados, no mesmo formato.
• Uma função principal que chame getLinks com um artigo inicial, escolha
um link de artigo aleatório na lista devolvida e chame getLinks
novamente, até que você interrompa o programa ou nenhum link de artigo seja encontrado na nova página.
Eis o código completo para isso:
'''
print('\n'*5,'--->>> Código refatorado ---> CRAWLER ASSUNTOS ALEATÓRIOS WIKI\n')
print('Press crtl+z to quit')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed()#datetime.datetime.now())
print(random.random())

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

'''    
A primeira tarefa do programa, depois de importar as bibliotecas
necessárias, é definir a semente (seed) para o gerador de números
aleatórios com o horário atual do sistema. Isso praticamente garante que
haja um caminho aleatório novo e interessante pelos artigos da Wikipédia
sempre que o programa executar.

Números pseudoaleatórios e sementes aleatórias

No exemplo anterior, o gerador de números aleatórios de Python foi usado para selecionar um artigo aleatório em cada página a fim de continuar percorrendo a Wikipédia aleatoriamente. No entanto, os números aleatórios devem ser utilizados com cautela.Embora sejam ótimos para calcular respostas corretas, os computadores são péssimos para inventar algo. Por esse motivo, os números aleatórios podem ser um desafio. A maioria dos algoritmos para números aleatórios se esforça em gerar uma sequência de número uniformemente distribuídos e difíceis de prever, mas um número para “semente” (seed) deve ser fornecido a esses algoritmos para que tenham um valor com o qual poderão trabalhar inicialmente. A mesma semente sempre produzirá exatamente a mesma sequência de números “aleatórios”; por esse motivo, usei o relógio do sistema para iniciar novas sequências de números aleatórios e, desse modo, novas sequências de artigos aleatórios. Isso faz com que executar o programa seja um pouco mais emocionante.

Para os curiosos, o gerador de números pseudoaleatórios de Python usa o algoritmo Mersenne Twister. Embora gere números aleatórios difíceis de prever e uniformemente distribuídos, ele exige um pouco do processador. Números aleatórios bons assim não são baratos!
Em seguida, o programa define a função getLinks, que aceita o URL de um
artigo no formato /wiki/..., insere o nome de domínio da Wikipédia,
http://en.wikipedia.org, como prefixo e obtém o objeto BeautifulSoup para o
HTML que está nesse domínio. Então, uma lista de tags com links para artigos é gerada com base nos parâmetros discutidos antes, e essa lista é
devolvida.
O corpo principal do programa começa definindo uma lista de tags de links
para artigos (a variável links) com a lista de links da página inicial:
https://en.wikipedia.org/wiki/Kevin_Bacon. Em seguida, o código executa
um laço, encontrando uma tag de link aleatória para um artigo na página,
extraindo o atributo href dela, exibindo a página e obtendo uma nova lista
de links do URL extraído.
É claro que um pouco mais de trabalho é necessário para resolver o
problema do Six Degrees of Wikipedia, além de construir um scraper que
ande de página em página. Também é necessário armazenar e analisar os
dados resultantes. Para ver uma continuação da solução desse problema,
leia o Capítulo 6.
Trate suas exceções!
Embora esses códigos de exemplo omitam a maior parte do tratamento de exceções para que
sejam mais concisos, esteja ciente de que podem surgir muitos problemas possíveis. O que
aconteceria se a Wikipédia mudasse o nome da tag bodyContent, por exemplo? Quando o
programa tentasse extrair o texto da tag, um AttributeError seria gerado.
Embora não haja problemas em executar esses scripts como exemplos a serem observados de
perto, um código autônomo em um ambiente de produção exigirá muito mais tratamento de
exceções do que seria apropriado inserir neste livro. Volte ao Capítulo 1 para obter mais
informações a esse respeito.
'''


