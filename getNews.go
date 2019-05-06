package getnews

import (
	"os"

	"github.com/mmcdole/gofeed"
)

//NewsStruct 記事の構造体
type NewsStruct struct {
	ID    int
	Title string
	URL   string
}

func makeNewsStruct(item *gofeed.Item) NewsStruct {
	var news NewsStruct
	news.Title = item.Title
	news.URL = item.Link
	return news
}

//GetNews 渡されたRSSのURLに入ってるニュースをNewsStruct(のSlice)にして返す関数
func GetNews(URL string) []NewsStruct {
	var newsTitle string
	var newsList []NewsStruct
	fp := gofeed.NewParser()
	feed, _ := fp.ParseURL(URL)
	items := feed.Items

	// pythonのための中間ファイルの用意
	file, _ := os.OpenFile("./newsList.txt", os.O_WRONLY|os.O_CREATE, 0666)
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
