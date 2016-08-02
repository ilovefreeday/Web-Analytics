import urllib
from bs4 import BeautifulSoup
import urlparse

htmltext = urllib.urlopen("https://nytimes.com")
soup = BeautifulSoup(htmltext)

for tag in soup.findAll('a',href = True):
	raw = tag['href']
	b1 = urlparse.urlparse(tag['href']).hostname
	b2 = urlparse.urlparse(tag['href']).path
	b3 = 'https://' + str(b1) + str(b2)
	print b3