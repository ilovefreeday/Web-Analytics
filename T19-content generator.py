import nltk
import urllib
import mechanize
import readability
from bs4 import BeautifulSoup
from readability.readability import Document

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

url = 'http://www.nytimes.com/interactive/2015/02/15/us/politics/jeb-bush-letters.html'

html = urllib.urlopen(url).read()

readable_article = Document(html).summary()
readable_title = Document(html).short_title()

soup = BeautifulSoup(readable_article)

final_article = soup.text

links = soup.findAll('img', scr=True)

print final_article
print readable_title

