import urllib
import re

htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=10&p=25m&f=c&df=cpct&auto=1&ts=1417704777655&ei=DXWAVKmQEtKq8gaGq4GgCw").read()

print htmltext.split()[len(htmltext.split())-1]




execfile("/Users/YeTian/SublimeText/Python Web Scraping/scrape.py")
