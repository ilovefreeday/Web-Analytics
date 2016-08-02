import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = 'https://nytimes.com'

br = mechanize.Browser() 
urls = [url]
visited = [url]

while len(urls) > 0:
	br.open(urls[0])

	urls.pop(0)
	for link in br.links():
		newurl = urlparse.urljoin(link.base_url, link.url)
		b1 = urlparse.urlparse(newurl).hostname
		b2 = urlparse.urlparse(newurl).path
		print 'https://'+str(b1)+str(b2)

		if newurl not in visited:
			visited.append(newurl)
			urls.append(newurl)
			print newurl
