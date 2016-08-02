from threading import Thread
import urllib
import re

def th(ur):
	base = "http://finance.yahoo.com/q?s="+ur
	regex = '<span id="yfs_l84_'+ur.lower()+'">(.+?)</span>'
	pattern = re.compile(regex)
	htmltext = urllib.urlopen(base).read()
	results = re.findall(pattern,htmltext)
	print str(ur) + " " + str(results[0])

symbolslist = open("/Users/YeTian/SublimeText/Python Web Scraping/symbols.txt").read()
symbolslist = symbolslist.split("\n")

threadlist = []

for u in symbolslist:
	t = Thread(target = th, args = (u,))
	t.start()
	threadlist.append(t)


for b in threadlist:
	try:
		b.join()
	except:
		pass

# execfile("/Users/YeTian/SublimeText/Python Web Scraping/T9-multithreaded python.py")


