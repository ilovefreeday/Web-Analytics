import urllib
import re

symbolslist = ['aapl','fb','goog','nflx','msft','blk','nke','t']

i=0
while i<len(symbolslist):
	url = 'http://finance.yahoo.com/q?s='+symbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_'+symbolslist[i]+'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	print 'the price of',symbolslist[i],price[0]
	i+=1