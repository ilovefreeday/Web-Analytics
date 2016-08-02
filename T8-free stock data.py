import urllib
import re
import json


symbolslist = open('/Users/YeTian/SublimeText/Python Web Scraping/symbols.txt').read()
symbolslist = symbolslist.split("\n")

for symbol in symbolslist:
	myfile = open('/Users/YeTian/SublimeText/Python Web Scraping/daily_price/' + symbol + '.txt','w')
	myfile.close()

	htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ symbol + ":US")
	data = json.load(htmltext) # should load a file,but read() is a string 
	datapoints = data['data_values']
	
	myfile = open('/Users/YeTian/SublimeText/Python Web Scraping/daily_price/' + symbol + '.txt','a')
	for point in datapoints:
		print "symbol",symbol,"time",point[0],"price",point[1]
		myfile.write(str(symbol)+','+str(point[0])+','+str(point[1])+'\n')
	myfile.close()

 

execfile("/Users/YeTian/SublimeText/Python Web Scraping/T8-free stock data.py")

