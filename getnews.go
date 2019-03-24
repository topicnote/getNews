package getnews

import (
	"github.com/mmcdole/gofeed"
)

type newsStruct struct {
	id    int
	title string
	url   string
}

var articles []newsStruct

func Getnews() []newsStruct {
	fp := gofeed.NewParser()

	feed, _ := fp.ParseURL("http://www.news24.jp/rss/index.rdf")
	items := feed.Items

	var newsSlice []newsStruct

	for index, item := range items { //sliceにappend
		var news newsStruct
		news.title = item.Title
		news.url = item.Link
		news.id = index
		newsSlice = append(newsSlice, news)
	}
	return newsSlice
}

func main() {
	articles = Getnews()
}
