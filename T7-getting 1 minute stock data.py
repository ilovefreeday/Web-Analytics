import urllib
import re
import json

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/AAPL:US")

data = json.load(htmltext) # should load a file,but read() is a string 

datapoints = data['data_values']

for point in datapoints:
	print point[1]
print 'the number of points is',len(datapoints)



execfile("/Users/YeTian/SublimeText/Python Web Scraping/T7-getting 1 minute stock data")



