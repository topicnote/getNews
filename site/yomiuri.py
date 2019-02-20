# coding: UTF-8
import sys
import urllib.request as rq
from bs4 import BeautifulSoup
from mylib.gettopic import gootopic
from mylib.sendserver import send_to_server


def getbody(article_url):
    article_page = rq.urlopen(article_url)
    article_html = BeautifulSoup(article_page, "lxml")
    body = article_html.find("article")
    return body

def main():
    # URL指定
    # url = "https://www.yomiuri.co.jp/politics/"
    url = sys.argv[1]

    # HTML取得
    html = rq.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    articlelist = soup.find(class_="pbNested span-main-inr")

    dic = {}

    # トップ記事
    articles = articlelist.find(class_="list-top").find_all("li")
    print("=================================================")

    for i, article in enumerate(articles):
        title = article.find(class_="headline").text
        article_url = article.a.get("href")
        body = getbody(article_url)
        keys = gootopic(title, body)
        keys.pop('AD', None)

        dic.append({'title':title, 'url':article_url, 'keys':keys})

        if i >= 10:
            break


    # その他の記事
    articles = articlelist.find(class_="list-common").find_all("li")

    for i, article in enumerate(articles):
        title = article.find(class_="headline").text
        article_url = article.a.get("href")
        body = getbody(article_url)
        keys = gootopic(title, body)

        dic.append({'title':title, 'url':article_url, 'keys':keys})

        if i >= 10:
            break

    send_to_server(dic, "yomiuri")

if __name__ == "__main__":
    main()