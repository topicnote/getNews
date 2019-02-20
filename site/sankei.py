# coding: UTF-8
import sys
import urllib.request as rq
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
# from mylib.sendserver import send_to_server


def getbody(url):
    articlepage = rq.urlopen(url)
    articlehtml = BeautifulSoup(articlepage, "lxml")
    body = articlehtml.find(class_="post_content")
    return body


url = sys.argv[1]

html = rq.urlopen(url)
soup = BeautifulSoup(html, "lxml")
articlelist = soup.find(class_="entry_list")
articles = articlelist.find_all("article")
print("=================================================")
for i, article in enumerate(articles):
    content = article.find("h3")
    if content == None:
        continue
    title = content.find("a").text
    article_url = content.a.get("href")
    body = getbody(article_url)
    keys = gootopic(title, body)

    print(title)
    print(article_url)
    print(keys)

    # send_to_server(title, article_url, keys)

    print("=================================================")

    if i >= 10:
        break

