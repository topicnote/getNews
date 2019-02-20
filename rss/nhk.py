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
    # url = sys.argv[1]
    url = "http://www.news24.jp/rss/index.rdf"

    # XML取得
    xml = rq.urlopen(url)
    soup = BeautifulSoup(xml, "xml")
    articles = soup.find_all("item")

    print("=================================================")
    for i, article in enumerate(articles):
        title = article.find("title").contents
        article_url = article.find('link').string
        # body = getbody(article_url)
        body = article.find("description").contents
        keys = gootopic(title, body)

        print(title)
        print(article_url)
        print(keys)

        dic.append({'title':title, 'url':article_url, 'keys':keys})


if __name__ == "__main__":
    main()
