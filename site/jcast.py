# coding: UTF-8
import sys
import urllib.request as rq
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
# from mylib.sendserver import send_to_server


def getbody(url):
    articlepage = rq.urlopen(url)
    articlehtml = BeautifulSoup(articlepage, "lxml")
    body = articlehtml.find(class_="entry-text")
    return body

url = sys.argv[1]

html = rq.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="category-entry-list")
articles = articlelist.find_all("li")
print("=================================================")
for article in articles:

    title = article.find(class_="entry-title").string.strip()
    article_url = article.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)

    print(title)
    print(article_url)
    print(keys)

    # send_to_server(title, article_url, keys)

    print("=================================================")
