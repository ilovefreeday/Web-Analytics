import mechanize
from bs4 import BeautifulSoup

def getHtmlText(url):
	br = mechanize.Browser()
	htmltext = br.open(url).read()
	return htmltext

def getHtmlFile(url):
	br = mechanize.Browser()
	htmlfile = br.open(url)
	return htmlfile

def getArticleText(webtext):
	articletext = ""
	soup = BeautifulSoup(webtext)
	for tag in soup.findAll('p', attrs = { "itemprop": "articleBody"}):
		articletext += tag.text
	return articletext

def getArticle(url):
	htmltext = getHtmlText(url)
	return getArticleText(htmltext)

def getKeywords(articletext):
	common = open("common.txt").read().split('\n')
	word_dict = {}
	word_list = articletext.lower().split()
	for word in word_list:
		if word not in common and word.isalnum():

			if word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1
	top_words =  sorted(word_dict.items(), key = lambda(k,v):(v,k),reverse = True)[0:25]
	top25 = []
	for w in top_words:
		top25.append(w[0])
	return top25

url = 'http://www.nytimes.com/2015/02/15/us/politics/as-dynastys-son-jeb-bush-used-his-connections-freely.html?ref=politics'

web_text = getHtmlText(url)
articletext = getArticleText(web_text)
article = getArticle(url)

the_top_word = getKeywords(article)
# the_top_word = getKeywords(web_text)

# print web_text
# print articletext
# print article
# print the_top_word

