package getnews

import (
	"github.com/mmcdole/gofeed"
)

type NewsStruct struct {
	Id    int
	Title string
	Url   string
}

var articles []NewsStruct

func Getnews() []NewsStruct {
	fp := gofeed.NewParser()

	feed, _ := fp.ParseURL("http://www.news24.jp/rss/index.rdf")
	items := feed.Items

	var newsSlice []NewsStruct

	for index, item := range items { //sliceにappend
		var news NewsStruct
		news.Title = item.Title
		news.Url = item.Link
		news.Id = index
		newsSlice = append(newsSlice, news)
	}
	return newsSlice
}

func main() {
	articles = Getnews()
}
