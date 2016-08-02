import urllib
import re
import json

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:AR")

data = json.load(htmltext) # should load a file,but read() is a string 

print data['last_price']



execfile("/Users/YeTian/SublimeText/Python Web Scraping/T6-scraping tutorial.py")

