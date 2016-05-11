import re,urllib2,os,requests

url = 'http://www.careercup.com/categories'

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
response = browser.open(url)
html=response.read()
html = html.split('<div class="box">')[1]
# print html

linklist,companylist = [],[]
allcompany = re.finditer('interview-questions">(.*?)</a>',html)
alllink = re.finditer('<a href="/page?(.*?)-interview-questions">',html)
for i in alllink:
	linklist.append(i.group(1)[5:])
for i in allcompany:
	companylist.append(i.group(1))

for i in range(len(linklist)):
	page = 1
	company = companylist[i]
 	if not os.path.exists(company):
 		os.makedirs(company)
 	name_html = os.path.join(company+'/','questions.html')
 	name_txt = os.path.join(company+'/','questions.txt')
 	fw=open(name_html,'w')
 	f = open(name_txt,'w')
 	while True:
		link = 'http://www.careercup.com/page?pid='+linklist[i]+'-interview-questions&n=' +str(page)
		print link
		response = browser.open(link)
		html=response.read()
		if html.find('Sorry - no more questions!')!= -1:
			break
		print link
		html = html.split('<script>writeBookLink')[0]
		questions = html.split('<li class="question">')
		for j in range(1,len(questions)):
			content = re.finditer('<p>(.*?)</p>',questions[j])
			for k in content:
				new = k.group(1).split('<br>')[0]
				new = new.replace('\r<br/>','\n')
				# print new
				fw.write(new +'\n')
				f.write(new +'\n')
		page +=1
	f.close()
	fw.close()


# for i in range(len(linklist)):
# 	company = companylist[i]
# 	if not os.path.exists(company):
# 		os.makedirs(company)

# 	for l in range(num[i]):
# 		link = 'http://www.careercup.com/page?pid='+linklist[i]+'-interview-questions&n='+str(num[i])
# 		name = company +'_page_'+str(i) + '.html'
# 		fw = open(name,'w')
# 		fw.write(link)
# 		fw.close()

	# 	print link
	# 	response = browser.open(link)
	# 	html = response.read()
		# questions = html.split('<li class="question">')
		# for j in range(1,len(questions)):
		# 	content = re.finditer('<p>(.*?)</p>',questions[j])
		# 	for k in content:
		# 		new = k.group(1).split('<br>')[0]
		# 		new = new.replace('\r<br/>','\n')
		# 		print new
		# 		fw.write(new +'\n')


