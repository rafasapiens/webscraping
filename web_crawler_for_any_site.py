'''
Ao usar as classes Content e Website, podemos então escrever um Crawler para
coletar o título e o conteúdo de qualquer URL fornecido para uma dada
página web de um dado site:
'''

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


print('Crawler trabalhando...')

class Content:
    """
    Classe-base comum para todos os artigos/páginas
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Uma função flexível de exibição controla a saída
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Website:
    """
    Contém informações sobre a estrutura do site
    """
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag



class Crawler:
    
    def getPage(url):
        try:
            html = urlopen(url)
        except Exception:
            return None
        return BeautifulSoup(html, 'html.parser')
    def safeGet(bs, selector):
        """
    Utility function used to get a content string from a Beautiful Soup
    object and a selector. Returns an empty string if no object
    is found for the given selector
    """
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    '''
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return print('Algo deu errado ao obter a página')#None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Função utilitária usada para obter uma string de conteúdo de um
        objeto BeautifulSoup e um seletor. Devolve uma string
        vazia caso nenhum objeto seja encontrado para o dado seletor
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        Extrai conteúdo de um dado URL de página
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
                print('até o fim veio')
    '''

    def getContent(website, path):
        """
 Extract content from a given page URL
 """
        url = website.url+path
        bs = Crawler.getPage(url)
        if bs is not None:
            title = Crawler.safeGet(bs, website.titleTag)
            body = Crawler.safeGet(bs, website.bodyTag)
            return Content(url, title, body)
        return Content(url, '', '')

# Eis o código que define os objetos do site e dá início ao processo:

siteData = [
 ['O\'Reilly', 'https://www.oreilly.com', 'h1', 'div.title-description'],
 ['Reuters', 'https://www.reuters.com', 'h1', 'div.ArticleBodyWrapper'],
 ['Brookings', 'https://www.brookings.edu', 'h1', 'div.post-body'],
 ['CNN', 'https://www.cnn.com', 'h1', 'div.article__content']
]
websites = []
for name, url, title, body in siteData:
 websites.append(Website(name, url, title, body))
Crawler.getContent(
 websites[0],
 '/library/view/web-scraping-with/9781491910283'
 ).print()
Crawler.getContent(
 websites[1],
 '/article/us-usa-epa-pruitt-idUSKBN19W2D0'
 ).print()
Crawler.getContent(
 websites[2],
 '/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/'
 ).print()
Crawler.getContent(
 websites[3],
 '/2023/04/03/investing/dogecoin-elon-musk-twitter/index.html'
 ).print()


'''
crawler = Crawler()
siteData = [
['O\'Reilly Media', 'http://oreilly.com','h1', 'section#product-description'],
['Reuters', 'http://reuters.com', 'h1','div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu','h1', 'div.post-body'],
['New York Times', 'http://nytimes.com','h1', 'p.story-content']
]
websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')

'''
