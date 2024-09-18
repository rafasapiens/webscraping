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

def scrapeCNN(url):
    bs = BeautifulSoup(urlopen(url), 'html.parser')
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'article__content'}).text
    print('body: ')
    print(body)
    return Content(url, title, body)

def scrapeRafa(url):
    bs = BeautifulSoup(urlopen(url), 'html.parser')
    title = bs.find('h1').text
    body = bs.find('div', {'class': ''}).text
    return Content(url, title, body)

url = 'https://rafasapiens.com/portfolio/'  #'https://www.brookings.edu/research/robotic-rulemaking/'
content = scrapeRafa(url)
content.print()

url = 'https://www.cnn.com/2023/04/03/investing/\
dogecoin-elon-musk-twitter/index.html'
content = scrapeCNN(url)
content.print()
