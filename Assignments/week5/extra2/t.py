"""
Created on Tue Oct  6 20:17:16 2015

@author: NEPTUNE
"""
TTT=[]
import re
page=open('in.html','r').read()
col=page.split('str-author-box authorbox')
for html in col:
    name=''
    location='Location hidden'
    date=''
    names=re.finditer('<div class="authorsn x-author">(.*?)</div>',html)
    names1=re.finditer('data-messageto="(.*?)" title=',html)
    locations=re.finditer('<a data-t="post-geoip" href=".*?">\n(.*?)\n</a>',html)
    locations1=re.finditer('<p class="geoip x-geoip">\n(.*?)\n</p>',html)
    dates=re.finditer('<span class="x-post-time">(.*?)</span>',html)
    for i in names:
        name=i.group(1)
    if name=='':
        for i in names1:
            name=i.group(1)
    for i in locations:
        location=i.group(1)
    if location=='Location hidden':
        for i in locations1:
            location=i.group(1)
    for i in dates:
        date=i.group(1)
    
    if name!='' and location!='' and date!='':
        TTT.append(name+'\t'+location+'\t'+date)
print (TTT)

T=[]
for i in TTT:
    if i[0].isupper():
        for j in i:
            if j.islower():
                T.append(i)
                break
            if j=='\t':
                break
        

print len(T)


fw=open('out.txt','w')
for i in T:
    fw.write(i+'\n')
fw.close()