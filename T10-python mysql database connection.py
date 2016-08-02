from threading import Thread
import urllib
import re
import mysql.connector

gmap = {}

def th(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	regex = '<span id="yfs_l84_'+ur.lower()+'">(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern,htmltext)
	try:
		gmap[ur] = results[0]
	except:
		print "got an error"

symbolslist = open("/Users/YeTian/SublimeText/Python Web Scraping/symbols.txt").read()

symbolslist = symbolslist.split("\n")

threadlist = []

for u in symbolslist:
	t = Thread(target = th, args = (u,))
	t.start()
	threadlist.append(t)

for b in threadlist:
	b.join()

conn = mysql.connector.connect(host='localhost', user='root')
cursor = conn.cursor()

for key in gmap.keys():
	print key,gmap[key]
	cursor.execute("CREATE DATABASE IF NOT EXISTS " + 'stock_data')
	use = 'use stock_data'
	cursor.execute(use)
	query = "INSERT INTO tutorial (symbol,last) values ('AAPL')"
	query = query + "'" + key + "'," + gmap[key] + ")"
	cursor.execute(query)
	conn.commit()
	row = cursor.fetchall()

# execfile("/Users/YeTian/SublimeText/Python Web Scraping/T10-python mysql database connection")


