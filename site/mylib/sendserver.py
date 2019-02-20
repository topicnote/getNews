# coding: UTF-8
import json

def send_to_server(dic, name):
	print(dic)
	f = open("~/tmp/" + name + "_" + random.randint(0,100) + ".json", 'w')
	json.dump(dic, f)


