import re,urllib2,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# page = 'http://www.snapdeal.com/brand/lg/electronic-tv-accessories?sort=plrty'

# company_list = ['samsung','lg','philips','micromax','noble','aoc','salora','sansui','i-grasp','haier','videocon','intex','skyworth','vu','lloyd','onida','wybor','intec']
company_list = ['lg','samsung']

def parsepage(html,linklist):
	alllink = re.finditer('<a href="http://www.snapdeal.com/product/(.*?)"',html)
	for i in alllink:
			linklist.append(i.group(1))

def readpage(link):
	driver = webdriver.Chrome('./chromedriver')
	driver.get(link)
	time.sleep(1)
	elem = driver.find_element_by_tag_name('body')
	not_pagedown = 5
	while not_pagedown:
		elem.send_keys(Keys.PAGE_DOWN)
		time.sleep(0.2)
		not_pagedown -= 1

	linklist = []
	parsepage(driver.page_source,linklist)
	return linklist

def findalllink(company_list):
	alllink = []
	for j in range(len(company_list)):
		page = 'http://www.snapdeal.com/brand/'+company_list[j]+'/electronic-tv-accessories?sort=plrty'
		linklist = readpage(page)
		for i in range(len(linklist)):
			url = 'http://www.snapdeal.com/product/'+linklist[i]
			alllink.append(url)
	return alllink

def getlist(new,old):
	for i in old:
		new.append(i.group(1))

def handletext(new,old,length):
	new = old[-length-1:-1]
	return new

def handlestar(new,old,length):
	for i in range(length):
		new.append(old[i].count('active'))
	return new

def findreview(alllink,fw):
	browser=urllib2.build_opener()
	browser.addheaders=[('User-agent', 'Mozilla/5.0')]
	count=0
	for k in range(len(alllink)):
		user,date,text1,text2,star1,star2=[],[],[],[],[],[]
		response=browser.open(alllink[k])
		html=response.read()
		users = re.finditer('<span class="_reviewUserName" title="(.*?)">',html)
		getlist(user,users)
		# print len(user)
		dates = re.finditer('<div class="date LTgray">(.*?)</div>',html)
		getlist(date,dates)
		print len(date)
		stars = re.finditer('<div class="rating">((\n.*){6})',html)
		getlist(star1,stars)
		star2 = handlestar(star2,star1,len(date))
		texts = re.finditer('<p>(.*?)</p>',html)
		getlist(text1,texts)
		print len(text1)
		text2 = handletext(text2,text1,len(date))
		print len(text2)
		for n in range(len(date)):
			content =''
			content += user[n]+'\t'+date[n]+'\t'+str(star2[n])+'\n'+text2[n]+'\n'
			print content
			fw.write(content+'\n')
			count +=1
			print count
	fw.close()
	return

fw=open('output.txt','w')
findreview(findalllink(company_list),fw)

