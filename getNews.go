package main

import (
	"github.com/mmcdole/gofeed"
)

//NewsStruct 記事の構造体
type NewsStruct struct {
	ID      int
	Title   string
	URL     string
	Keyword map[string]float64
}

func makeArticle(id int, item *gofeed.Item) NewsStruct {
	var news NewsStruct
	news.ID = id
	news.Title = item.Title
	news.URL = item.Link
	// fmt.Println(news.Title)
	// fmt.Println(item.Description)
	news.Keyword = makeTopic.getKeyword(news.Title, item.Description)
	return news
}

var articles []NewsStruct

//Getnews 構造体にニュース内容をマッピングして返す関数
func Getnews() []NewsStruct {
	fp := gofeed.NewParser()

	// feed, _ := fp.ParseURL("http://www.news24.jp/rss/index.rdf")
	feed, _ := fp.ParseURL("https://www3.nhk.or.jp/rss/news/cat0.xml")
	items := feed.Items

	var newsSlice []NewsStruct

	for index, item := range items { //sliceにappend
		article := makeArticle(index, item)
		newsSlice = append(newsSlice, article)
	}
	return newsSlice
}

func main() {
	articles = Getnews()
}
