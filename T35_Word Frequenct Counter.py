import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code)
	for post_text in soup.findAll('a',{'class':'reference internal'}):
		content = post_text.string
		words = content.lower().split()
		for each_word in words:
			print(each_word)
			word_list.append(each_word)
	clean_list(word_list)

def clean_list(word_list):
	clean_word_list = []
	for word in word_list:
		symbols = "!@#$%^&*():<>?,.{}|\]["
		for i in range(0,len(symbols)):
			word = word.replace(symbols[i],"")
		if len(word) > 0:
			print (word)
			clean_word_list.append(word)
	creat_dictionary(clean_word_list)

def creat_dictionary(clean_word_list):
	word_count = {}
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
		print (key, value)

  
url = 'http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html'

start(url)

