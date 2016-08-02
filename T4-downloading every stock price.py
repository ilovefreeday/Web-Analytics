import urllib
import re

symbolfile = open("symbols.txt")
symbolslist = symbolfile.read()

newsymbolslist = symbolslist.split("\n")

i=0
while i<20:
	url = 'http://finance.yahoo.com/q?s='+newsymbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print 'the price of',newsymbolslist[i],price[0]
	i+=1