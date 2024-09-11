from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
#idem anterior
print(bs.html.body.h1,"\n"*2)

print(bs.html,"\n"*2)

print(bs.head,"\n"*2)

print(bs.title,"\n"*2)

print(bs.body,"\n"*2)

print(bs.div)
