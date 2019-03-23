package main

import (
	"fmt"

	"github.com/mmcdole/gofeed"
)

func main()  {
	fp := gofeed.NewParser()

	feed, _ := fp.ParseURL("http://www.news24.jp/rss/index.rdf")
	items := feed.Items

	for _, item := range items{
		fmt.Println(item.Title)
		fmt.Println(item.Link)
		fmt.Println()
	}
}