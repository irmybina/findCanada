from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
pages = set()
def getLinks(articleURL):
    try:
        html = urlopen("http://en.wikipedia.org" + articleURL)
    except HTTPError as e:
        print(e)
    else:
        if html is None:
            print("URL is not found")
        else:
            bsObj = BeautifulSoup(html)
            aTags = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
            pureLinks = []
            for aTag in aTags:
                pureLinks.append(aTag.attrs["href"])
            return pureLinks
steps = 0
links = getLinks("/wiki/Rocky_Mountains")

# for link in links:
#     print(link)

while len(links) > 0 and "/wiki/Canada" not in pages:
    if "/wiki/Canada" not in links:
        newArticle = links[random.randint(0, len(links)-1)]
        while (newArticle in pages):
            newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newArticle)
        pages.add(newArticle)
        links = getLinks(newArticle)
    else:
        pages.add("/wiki/Canada")
        print("/wiki/Canada")
        steps+=1
print(str(len(pages)) + " steps")