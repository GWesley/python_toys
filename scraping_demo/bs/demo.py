# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bsObj = BeautifulSoup(html.read(),"html.parser")
# print(bsObj.h1)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())