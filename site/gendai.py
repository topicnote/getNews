# coding: UTF-8
import sys
import urllib.request as rq
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
# from mylib.sendserver import send_to_server

def getbody(url):
    articlepage = rq.urlopen(articleurl)
    articlehtml = BeautifulSoup(articlepage, "lxml")
    body = articlehtml.find(class_="full-text")
    return body

url = sys.argv[1]

html = rq.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="article-wrap")
articles = articlelist.find_all(class_="article-box")
print("=================================================")
for i, article in enumerate(articles):
    content = article.find(class_="entry-ttl")
    if content == None:
        continue
    title = content.text.lstrip()
    articleurl = "https://www.nikkan-gendai.com" + content.a.get("href")
    body = getbody(articleurl)
    keys = gootopic(title,body)

    print(title)
    print(articleurl)
    print(keys)

    # send_to_server(title, article_url, keys)

    print("=================================================")
    if i >= 10:
        break


