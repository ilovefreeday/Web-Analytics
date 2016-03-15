from bs4 import BeautifulSoup

soup = BeautifulSoup(open('in.html'))

names = soup.find_all('li',{'class':'user-name'})
citys = soup.find_all('li',{'class':'user-location'})
friends = soup.find_all('li',{'class':'friend-count'})
reviews = soup.find_all('li',{'class':'review-count'})
stars = soup.find_all('meta',{'itemprop':'ratingValue'})
dates = soup.find_all('span',{'class':'rating-qualifier'})
star=[]
s=[]
for n in stars:
	star.append(str(n))
for m in star:
	s.append(m.split('"')[1])

friend = [f.get_text() for f in friends]
city = [c.get_text() for c in citys]
name = [n.get_text() for n in names]
review = [r.get_text() for r in reviews]
date = [d.get_text() for d in dates]
s = s[-len(name):]

for i in date:
	if i.find('reviews') != -1:
		date.remove(i)

for j in date:
	if j.find('reviews') != -1:
		date.remove(j)

date1=[]
for n in date:
	date1.append(n.strip())

f = open('out.txt','w')
content = ''
for k in range(len(name)):
	content = name[k].split('\n')[1]+'\t'+city[k].split('\n')[1]+'\t'+friend[k].split(' ')[1]+'\t'+review[k].split(' ')[1]+'\t'+s[k]+'\t'+ date1[k]
	if k < len(name):
		f.write(content+'\n')
	else:
		f.write(content)
f.close()