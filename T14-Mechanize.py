import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = 'https://nytimes.com'

br = mechanize.Browser()

br.open(url)

for link in br.links():
	# print 'the base url is : ' + link.base_url
	# print 'the url is : ' + link.url

	newurl = urlparse.urljoin(link.base_url, link.url)
	b1 = urlparse.urlparse(newurl).hostname
	b2 = urlparse.urlparse(newurl).path

	# print urlparse.urlparse(newurl).path
	print 'https://'+b1+b2