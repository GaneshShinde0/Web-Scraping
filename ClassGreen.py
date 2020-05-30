from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html)
nameList=bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
nameList = bsObj.findAll(text="the prince")
print(len(nameList))
##############################################################
#The keyword argument allows you to select tags that contain a particular attribute.
#For example:
allText = bsObj.findAll(id="text")
print(allText[0].get_text())

#BeautifulSoup.findAll() keyword argument, previously discussed).2 For example,
#if you try the following call, you’ll get a syntax error due to the nonstandard use
#of class:
#bsObj.findAll(class="green")
#Instead, you can use BeautifulSoup’s somewhat clumsy solution, which involves
#adding an underscore:
bsObj.findAll(class_="green")
#Alternatively, you can enclose class in quotes:
bsObj.findAll("", {"class":"green"}

'''
NavigableString objects
Used to represent text within tags, rather than the tags themselves (some
functions operate on, and produce, NavigableStrings, rather than tag
objects).
The Comment object
Used to find HTML comments in comment tags, <!--like this one-->
These four objects are the only objects you will ever encounter (as of the time of
this writing) in the BeautifulSoup library.
'''
