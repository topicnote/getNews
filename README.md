# getnews
Web scraping and get related phrases

## 段階
[[getNews]] -> makeTopic -> webView

## ライブラリインポート
`go get github.com/mmcdole/gofeed`

## 実行方法
`go run getnews.go`

## 出力
（とりあえずPrintlnしてるのでどっかに格納予定）

（`~/tmp/` に中間ファイルを生成）

`~/` に結果をjson形式で出力

→makeTopicが出力を使用して、[トピック - 記事]の対応データを生成
