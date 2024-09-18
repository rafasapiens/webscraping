import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
 
    def print(self):
        print(f'TITLE: {self.title}')
        print(f'URL: {self.url}')
        print(f'BODY: {self.body}')

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeCNN(url):
    bs = BeautifulSoup(urlopen(url), 'html.parser')
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'article__content'}).text
    print('Body: ')
    print(body)
    return Content(url, title, body)

def scrapeBroos(url):
    bs = BeautifulSoup(urlopen(url), 'html.parser')
    title = bs.find('h1').text
    body = bs.find('div', {'class': ''}).text
    print('Body: BROOKINGS')
    print(body)
    return Content(url, title, body)
'''
def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class": 'byo-block -narrow wysiwyg-block wysiwyg'})#.text #  "post-body"}).text
    return Content(url, title, body)
'''
url = 'https://rafasapiens.com/portfolio/'   # 'https://www.brookings.edu/regions/latin-america-the-caribbean/central-america/'

content = scrapeBroos(url)


print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)


url =  'https://rafasapiens.com/portfolio/' #  'https://www.brookings.edu/research/robotic-rulemaking/'
content = scrapeBroos(url)
content.print()


url = 'https://www.cnn.com/2023/04/03/investing/\
dogecoin-elon-musk-twitter/index.html'
content = scrapeCNN(url)
content.print()

