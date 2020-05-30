from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime
pages=set()
random.seed(datetime.datetime.now())
#Retrieves A List Of All Internal Links found on page
def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]
    #FInds All Links that begin with a "/"
    for link in bsObj.findAll("a",href=recompile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks
#Retrieve a list of all External Links found in page
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
#Split Address
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts
def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,features="lxml")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
def followExternalOnly(startingPage):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("Random external Link is:"+externalLink)
    followExternalOnly(externalLink)
followExternalOnly("http://oreilly.com")
