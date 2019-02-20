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
    body = articlehtml.find(class_="post-bodycopy")
    return body


# URL指定
url = sys.argv[1]

# HTML取得
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="article-list")
#トップ記事
article = articlelist.find(class_="top-news")
print("=================================================")
title = article.find(class_="top-news_desc").find("h2").text
article_url = article.a.get("href")
body = getbody(article_url)
keys = gootopic(title, body)

print(title)
print(article_url)
print(keys)

# send_to_server(title, article_url, keys)

print("=================================================")

# その他の記事
articles = articlelist.find_all(class_="sub-news")
for i, article in enumerate(articles):
    title = article.find(class_="top-news_desc").find("h2").text
    article_url = article.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)

    print(title)
    print(article_url)
    print(keys)

    # send_to_server(title, article_url, keys)

    print("=================================================")
    if i >= 10:
        break
