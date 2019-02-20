# getnews
Web scraping and get related phrases

## 段階
[[getNews]] -> makeTopic -> webView

## 実行方法
`python3 genrereq.py [pol:政治　eco:経済　int:国際　spo:スポーツ　soc:社会　ent:エンタメ　it:IT]`

## 出力
（`~/tmp/` に中間ファイルを生成）

`~/` に結果をjson形式で出力

→makeTopicが出力を使用して、[トピック - 記事]の対応データを生成
