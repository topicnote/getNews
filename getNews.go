package getnews

import (
	"os"
	"fmt"

	"../structs"
	"github.com/mmcdole/gofeed"
)

func makeNewsStruct(item *gofeed.Item) structs.NewsStruct {
	var news structs.NewsStruct
	news.Title = item.Title
	news.URL = item.Link
	return news
}

//GetNews 渡されたRSSのURLに入ってるニュースをNewsStruct(のSlice)にして返す関数
func GetNews(URL string) []structs.NewsStruct {
	var newsTitle string
	var newsList []structs.NewsStruct
	fp := gofeed.NewParser()
	feed, _ := fp.ParseURL(URL)
	items := feed.Items

	// pythonのための中間ファイルの用意
	newsListPath := os.Getenv("NLP_MODEL_PATH") + "/newsList.txt"
	if err := os.Remove(newsListPath); err != nil {
        fmt.Println(err)
    }
	file, _ := os.OpenFile(newsListPath, os.O_WRONLY|os.O_CREATE, 0666)
	defer file.Close()

	for _, item := range items { //sliceにappend
		news := makeNewsStruct(item)
		newsList = append(newsList, news)
		newsTitle = news.Title + "\n"
		file.Write(([]byte)(newsTitle))
	}
	return newsList
}

// func main() {
// 	articles := GetNews("https://www3.nhk.or.jp/rss/news/cat0.xml")
// 	for _, article := range articles {
// 		fmt.Println(article.Title)
// 	}
// }
