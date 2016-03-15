import urllib2,re,time,HTMLParser,string

page=open('in.html',"r").read()
fw=open('score.txt','w')
i=1
div='<div class="review-list" data-component-bound="true" style="position: relative;">'
webpage=page[page.find(div):] 

names=re.finditer('<meta itemprop="author" content="(.*?)">',webpage)
locations=re.finditer('<li class="user-location">\n.*?<b>(.*?)</b>',webpage)
frdnos=re.finditer('<i class="i ig-common_sprite i-18x18_friends_c-common_sprite"></i> <b>(.*?)</b>',webpage)
revnos=re.finditer('<i class="i ig-common_sprite i-18x18_review_c-common_sprite"></i> <b>(.*?)</b>',webpage)
stars=re.finditer('<meta itemprop="ratingValue" content="(\d{1}.\d{1})">',webpage)
dates=re.finditer('<meta itemprop="datePublished" content=".*?">\n\s*(.*?)\n',webpage)

for (name, location, frdno, revno, star, date) in zip(names, locations, frdnos, revnos, stars, dates):

    n=name.group(1)  
    l=location.group(1)    
    f=frdno.group(1)
    r=revno.group(1)
    s=star.group(1)
    d=date.group(1)
    fw.write(n+'\t'+l+'\t'+f+'\t'+r+'\t'+s+'\t'+d+'\n')
    print 'no.'+str(i)+'\t'+n+'\t'+l+'\t'+f+'\t'+r+'\t'+s+'\t'+d+'\n'
    i=i+1
    
fw.close()