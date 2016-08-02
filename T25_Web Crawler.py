import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://www.buckysroom.org/trade/search.php?page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a',{"class":'item-name'}):
			href = "https://www.thenewboston.com" + link.get('href')
			print(href)
			print(title)
			get_single_item_data(href)
		page += 1

def get_single_item_data(item_url):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for itemname in soup.findAll('div',{"class":'i-name'}):
		print(itemname.string)
	for link in soup.findAll('a'):
		href = 'https://buckysroom.org' + link.get('href')
		print(href)
		
trade_spider(4)