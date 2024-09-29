"""
This type of crawler works well for projects when you want to gather all the data from
a site—not just data from a specific search result or page listing. It also works well
when the site’s pages may be disorganized or widely dispersed.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    
    def print(self):
        print(f'URL: {self.url}')
        print(f'TITLE: {self.title}')
        print(f'BODY:\n{self.body}')

class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = {}

    def getPage(url):
        try:
            html = urlopen(url)
        except Exception as e:
            print(e)
            return None
        return BeautifulSoup(html, 'html.parser')

    def safeGet(bs, selector):
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def getContent(self, url):
        """
        Extract content from a given page URL
        """
        bs = Crawler.getPage(url)
        if bs is not None:
            title = Crawler.safeGet(bs, self.site.titleTag)
            body = Crawler.safeGet(bs, self.site.bodyTag)
            return Content(url, title, body)
        return Content(url, '', '')

    def crawl(self):
        """
        Get pages from website home page
        """ 
        bs = Crawler.getPage(self.site.url)
        targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            url = targetPage.attrs['href']
            url = url if self.site.absoluteUrl else f'{self.site.url}{targetPage}'
            if url not in self.visited:
                self.visited[url] = self.getContent(url)
                self.visited[url].print()

brookings = Website(
    'Brookings', 'https://brookings.edu', '\/(research|blog)\/',
    True, 'h1', 'div.post-body')
crawler = Crawler(brookings)
crawler.crawl()

