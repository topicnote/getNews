# coding: UTF-8
import json

def send_to_server(dic, name):
	print(dic)
	f = open(name+".txt", 'w')
	json.dump(dic, f)


