# coding: UTF-8
import urllib.request as rq
import json
import os


def gootopic(title, body):
    path = os.path.dirname(os.path.abspath(__name__))
    token_path = os.path.join(path, '../../token.json')
    print(type(token_path))
    f = open(token_path, "r")
    token_id = json.loads(f.read())['id']
    app_id = token_id
    method = "POST"

    content = {
        "app_id": app_id,
        "request_id": "key",
        "title": title,
        "body": body.text,
        "max_num": "10"
    }

    json_data = json.dumps(content).encode("utf-8")
    headers = {"Content-Type": "application/json"}

    request = rq.Request("https://labs.goo.ne.jp/api/keyword", data=json_data, headers=headers, method=method)
    with rq.urlopen(request) as response:
        high_relative_words = response.read().decode("utf-8")  # 受け取ったものをjson形式の平文に戻す
        keyword_list = json.loads(high_relative_words)['keywords']  # json形式の平文を辞書形式に変換
        keys = {}
        for key in keyword_list:
            keys.update(key)
    return keys
