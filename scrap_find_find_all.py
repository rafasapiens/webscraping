'''Vamos criar um web scraper de exemplo que colete dados da página em
http://www.pythonscraping.com/pages/warandpeace.html.
Nessa página, as linhas com frases ditas pelas personagens da história estão
em vermelho, enquanto os nomes das personagens estão em verde.
Podemos ver as tags span, que fazem referência às classes CSS apropriadas,
na seguinte amostra do código-fonte da página:
<span class="red">Heavens! what a virulent attack!</span> replied
<span class="green">the prince</span>, not in the least disconcerted
by this reception.
Considerando a página inteira, podemos criar um objeto BeautifulSoup com
ela usando um programa semelhante àquele utilizado no Capítulo 1:
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
Com esse objeto BeautifulSoup, a função find_all pode ser usada para extrair
uma lista Python com nomes próprios, encontrados ao selecionar somente
o texto entre as tags <span class="green"></span> (find_all é uma função extremamente flexível que usaremos bastante mais adiante neste livro):
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
print(name.get_text())
Quando executado, esse código deve listar todos os nomes próprios do
texto, na ordem em que aparecem em War and Peace (Guerra e Paz).
Então, o que está acontecendo nesse caso? Havíamos chamado bs.tagName
antes para obter a primeira ocorrência dessa tag na página. Agora
chamamos bs.find_all(tagName, tagAttributes) para obter uma lista de todas as
tags da página, em vez de obter somente a primeira.
Depois de obter uma lista de nomes, o programa itera por todos os nomes
da lista e exibe name.get_text() para separar o conteúdo das tags.
Quando usar get_text() e quando preservar as tags
.get_text() remove todas as tags do documento com o qual você está trabalhando e
devolve uma string Unicode contendo somente o texto. Por exemplo, se você estiver
trabalhando com um bloco de texto grande, contendo muitos hiperlinks, parágrafos e outras
tags, tudo isso será removido, e restará um bloco de texto sem tags.
Lembre-se de que é muito mais fácil encontrar o que você procura em um objeto
BeautifulSoup do que em um bloco de texto. Chamar .get_text() deve ser sempre a sua
última tarefa, imediatamente antes de exibir, armazenar ou manipular os dados finais. Em
geral, você deve se esforçar ao máximo para tentar preservar a estrutura de tags de um
documento.
find()efind_all() como BeautifulSoup
find() e find_all() são as duas funções do BeautifulSoup que provavelmente
serão mais usadas. Com elas, é possível filtrar facilmente as páginas HTML
e encontrar as listas de tags desejadas – ou uma só tag – de acordo com
seus vários atributos.
As duas funções são extremamente parecidas, como mostram suas
definições na documentação do BeautifulSoup:
find_all(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
É bem provável que, em 95% do tempo, somente os dois primeiros
argumentos serão necessários: tag e attributes. Não obstante, vamos
analisar todos os argumentos com mais detalhes.
Já vimos antes o argumento tag; podemos passar o nome de uma tag como
string ou até mesmo uma lista Python de nomes de tags definidos como
strings. Por exemplo, o código a seguir devolve uma lista com todas as tags

*páginas 32 33 34 Web Scraping com Python Ryan Mitchel 
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

print()

titles = bs.find_all(['h1','h2','h3','h4','h5','h6'])
print(titles)

print()

#obter tags span do texto HTML verdes e vermelhas
tags = bs.find_all('span', {'class':{'green', 'red'}})
print(tags)

print()

nameList = bs.find_all(text='the prince')
print(len(nameList))
