# coding: UTF-8
import sys
import urllib.request as rq
import urllib.error
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
# from mylib.sendserver import send_to_server


def getbody(article_url):
    articlepage = rq.urlopen(article_url)
    articlehtml = BeautifulSoup(articlepage, "lxml")
    body = articlehtml.find("article")
    return body

url = sys.argv[1]

html = rq.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="ArticleListMain")
articles = articlelist.find_all("li")
print("=================================================")
for i, article in enumerate(articles):
    title = article.find("p").string
    article_url = "https://www.jiji.com"+article.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)

    print(title)
    print(article_url)
    print(keys)

    # send_to_server(title, article_url, keys)
    print("=================================================")
    if i >= 10:
        break
