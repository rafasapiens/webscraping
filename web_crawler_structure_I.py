# código chatgpt funcional porém sites sem os topicos pesquisados

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class Content:
    """Classe base comum para todos os artigos/páginas"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """Imprime as informações do artigo"""
        print(f'Novo artigo encontrado para o tópico: {self.topic}')
        print(f'URL: {self.url}')
        print(f'TÍTULO: {self.title}')
        print(f'CORPO:\n{self.body}')


class Website:
    """Armazena informações sobre a estrutura do site"""

    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    """Realiza o crawling no site especificado"""

    def __init__(self, website):
        self.site = website
        self.found = {}

    def getPage(self, url):
        """Obtém a página da web a partir da URL"""
        try:
            # Definindo cabeçalhos para evitar bloqueio por alguns sites
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req)
            return BeautifulSoup(html, 'html.parser')
        except Exception as e:
            print(f"Erro ao abrir a página {url}: {e}")
            return None

    def safeGet(self, bs, selector):
        """Extrai de forma segura o conteúdo da tag HTML fornecida"""
        selectedElems = bs.select(selector)
        if selectedElems and len(selectedElems) > 0:
            return '\n'.join([elem.get_text().strip() for elem in selectedElems])
        return ''

    def getContent(self, topic, url):
        """Extrai o conteúdo de uma página específica"""
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            return Content(topic, url, title, body)
        return Content(topic, url, 'Título não encontrado', 'Corpo não encontrado')

    def search(self, topic):
        """Realiza a busca no site para o tópico fornecido"""
        searchUrl = self.site.searchUrl + topic
        bs = self.getPage(searchUrl)
        if bs is not None:
            searchResults = bs.select(self.site.resultListing)
            for result in searchResults:
                url = result.select(self.site.resultUrl)[0].attrs['href']
                # Verifica se a URL é relativa ou absoluta
                url = url if self.site.absoluteUrl else self.site.url + url
                if url not in self.found:
                    self.found[url] = self.getContent(topic, url)
                    self.found[url].print()
        else:
            print(f"Não foi possível realizar a busca para o tópico: {topic}")


# Dados dos sites para crawling
siteData = [
    ['Reuters', 'http://reuters.com',
     'https://www.reuters.com/search/news?blob=',
     'div.search-result-indiv', 'h3.search-result-title a',
     False, 'h1', 'div.ArticleBodyWrapper'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.article-info', 'h4.title a', True, 'h1', 'div.core-block'],
    ['Pythonscraping', 'https://pythonscraping.com', 'h1']

]

# Cria uma lista de objetos Website
sites = [Website(name, url, search, rListing, rUrl, absUrl, tt, bt) for name, url, search, rListing, rUrl, absUrl, tt, bt in siteData]

# Inicializa os crawlers para cada site
crawlers = [Crawler(site) for site in sites]

# Tópicos de pesquisa
topics = ['python', 'data science']

# Realiza a pesquisa para cada tópico em cada site
for topic in topics:
    print(f"\nPesquisando por: {topic}\n")
    for crawler in crawlers:
        crawler.search(topic)




'''

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Content:
    """Common base class for all articles/pages"""
    
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url
    
    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic: {}'.format(self.topic))
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))

class Website:
    """ Contains information about website structure"""

    def __init__(self, name, url, searchUrl, resultListing,
        resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl=absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:
    def __init__(self, website):
        self.site =  website
        self.found = {}

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


    def getContent(self, topic, url):
        """
        Extract content from a given page URL
        """
        bs = Crawler.getPagr(url)
        if bs is not None:
            title = Crawler.safeGet(bs, self.site.tittleTag)
            body = Crawler.safeGet(bs, self.site.bodyTag)
            return Content(topic, url, tittle, body)
        return Content(topic, url, '', '')

    def search(self, topic):
        """
        Searches a given wrbsite for a given topic and records all pages found
        """
        bs = Crawler.getPage(self.site.searchUrl + topic)
        searchResults = bs.select(self.site.resultListing)
        for result in searchResults:
            url = result.select(self.site.resultUrl)[0].attrs['href']
            #Check to see wheter it's a relative or an absolute URL
            url = url if self.site.absoluteUrl else self.site.url + url
            if url not in self.found:
                self.found[url] = self.getContent(topic, url)
            self.found[url].print()




siteData = [
    ['Reuters', 'http://reuters.com',
    'https://www.reuters.com/search/news?blob=',
    'div.search-result-indiv', 'h3.search-result-title a', 
    False, 'h1', 'div.ArticleBodyWrapper'],
    ['Brookings', 'http://www.brookings.edu',
    'https://www.brookings.edu/search/?s=',
    'div.article-info', 'h4.title a', True, 'h1', 'div.core-block']
]
sites = []
for name, url, search, rListing, rUrl, absUrl, tt, bt in siteData:
    sites.append(Website(name, url, search, rListing, rUrl, absUrl, tt, bt))

crawlers = [Crawler(site) for site in sites]
topics = ['python', 'data%20science']

for topic in topics:
    for crawler in crawlers:
        crawler.search(topic)



# código chat gpt não funcional'

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Content:
    """Common base class for all articles/pages"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic: {}'.format(self.topic))
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))


class Website:
    """ Contains information about website structure"""

    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def __init__(self, website):
        self.site = website
        self.found = {}

    def getPage(self, url):
        try:
            html = urlopen(url)
        except Exception:
            return None
        return BeautifulSoup(html, 'html.parser')

    def safeGet(self, bs, selector):
        """
        Utility function used to get a content string from a Beautiful Soup
        object and a selector. Returns an empty string if no object
        is found for the given selector
        """
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def getContent(self, topic, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            return Content(topic, url, title, body)
        return Content(topic, url, '', '')

    def search(self, topic):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.getPage(self.site.searchUrl + topic)
        if bs is not None:
            searchResults = bs.select(self.site.resultListing)
            for result in searchResults:
                url = result.select(self.site.resultUrl)[0].attrs['href']
                # Check to see whether it's a relative or an absolute URL
                url = url if self.site.absoluteUrl else self.site.url + url
                if url not in self.found:
                    self.found[url] = self.getContent(topic, url)
                self.found[url].print()


siteData = [
    ['Reuters', 'http://reuters.com',
     'https://www.reuters.com/search/news?blob=',
     'div.search-result-indiv', 'h3.search-result-title a',
     False, 'h1', 'div.ArticleBodyWrapper'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.article-info', 'h4.title a', True, 'h1', 'div.core-block'],
    ['Pythonscraping', 'https://pythonscraping.com, 'p']
]

sites = []
for name, url, search, rListing, rUrl, absUrl, tt, bt in siteData:
    sites.append(Website(name, url, search, rListing, rUrl, absUrl, tt, bt))

crawlers = [Crawler(site) for site in sites]
topics = ['python', 'data%20science']

for topic in topics:
    for crawler in crawlers:
        crawler.search(topic)

'''
