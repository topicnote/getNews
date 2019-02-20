# coding: UTF-8
import sys
import json
import subprocess
from site import *

# コマンドライン引数としてジャンルのキーを受ける
# pol:政治　eco:経済　int:国際　spo:スポーツ　soc:社会　ent:エンタメ　it:IT　

genre = sys.argv[1]
jsonname = "json/"+genre+".json"
f = open(jsonname, 'r')
json_dict = json.load(f)
for target in json_dict:
    script = "site/" + format(json_dict[target]["script"])
    site_url = format(json_dict[target]["url"])
    print(script)
    subprocess.call(["python3", script, site_url])
print("fin")
