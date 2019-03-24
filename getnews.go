package main

import (
	"fmt"

	"github.com/mmcdole/gofeed"
)

type newsStruct struct {
	id    int
	title string
	url   string
}

func getnews() []newsStruct {
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
	fmt.Println(newsSlice)
	return newsSlice
}

func main() {
	getnews()
}
