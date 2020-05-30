from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages=set()

def getLinks(pageUrl):
    global pages
    c=0
    html=urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj=BeautifulSoup(html,features="lxml")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")): 
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                c+=1
                #print(newPage)
                pages.add(newPage)
                getLinks(newPage)
    print(c)
getLinks("")
