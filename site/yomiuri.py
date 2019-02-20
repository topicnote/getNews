# coding: UTF-8
import sys
import urllib.request as rq
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
# from mylib.sendserver import send_to_server


def getbody(article_url):
    article_page = rq.urlopen(article_url)
    article_html = BeautifulSoup(article_page, "lxml")
    body = article_html.find("article")
    return body


# URL指定
# url = "https://www.yomiuri.co.jp/politics/"
url = sys.argv[1]

# HTML取得
html = rq.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="pbNested span-main-inr")

# トップ記事
articles = articlelist.find(class_="list-top").find_all("li")
print("=================================================")
for i, article in enumerate(articles):
    title = article.find(class_="headline").text
    article_url = article.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)
    keys.pop('AD', None)

    print(title)
    print(article_url)
    print(keys)
    print("=================================================")
    if i >= 10:
        break

# その他の記事
articles = articlelist.find(class_="list-common").find_all("li")
for i, article in enumerate(articles):
    title = article.find(class_="headline").text
    article_url = article.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)

    print(title)
    print(article_url)
    print(keys)

    print("=================================================")

    if i >= 10:
        break
