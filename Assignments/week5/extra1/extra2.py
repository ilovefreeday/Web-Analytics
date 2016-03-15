import re,urllib2

f = open('in.html')
f = f.read()

begin =  f.find('http://www.yelp.com')
end =  f.find(' -->')

url = f[begin:end]

browser=urllib2.build_opener()

response=browser.open(url)

html=response.read() 

names = re.finditer('<meta itemprop="author" content="(.*?)">',html)
citys = re.finditer('<b>(.*?)</b>',html)
friends = re.finditer('<b>(.*?)</b> friend',html)
reviews = re.finditer('<b>(.*?)</b> review',html)
stars = re.finditer('<img alt="(.*?) star rating"',html)
dates = re.finditer('<meta itemprop="datePublished" content="(.*?)">',html)

def getlist(new,old):
	for i in old:
		new.append(i.group(1))

def handlecity(city1,city2):
	for j in city1:
		if j.find(', ')!=-1:
			city2.append(j)

name,city1,city2,friend,review,star,date = [],[],[],[],[],[],[]

getlist(name,names),getlist(city1,citys),getlist(review,reviews),getlist(friend,friends),getlist(date,dates),getlist(star,stars)
handlecity(city1,city2)


def write(name,city,friend,review,star,date,content,fw):
	for k in range(1,len(name)):
		date[k] = date[k].split('-')[1].replace('0','')+'/'+date[k].split('-')[2].replace('0','')+'/'+date[k].split('-')[0]
		print date[k]
		content = name[k]+'\t'+city2[k]+'\t'+friend[k]+'\t'+review[k]+'\t'+star[k]+'\t'+date[k]
		if k==len(name)-1:
			fw.write(content)
		else:
			fw.write(content+'\n')

fw = open('out.txt','w')
content=''
write(name,city2,friend,review,star,date,content,fw)
fw.close()

