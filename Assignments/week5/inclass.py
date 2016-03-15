
import re
import urllib2

browser=urllib2.build_opener()
#extract the set of users in a given html page and add them to the given set
def parsePage(html):
    users=re.finditer('<span class="a-size-base a-color-secondary review-date">on August [0-9]{2}, [0-9]{4}</span>',html)    
    count = 0    
    for user in users:
        count +=1
    return count

f=open('in.txt','r')
allnum=0
# this syntax allows us to read the file line-by-line
link=''
for line in f:
    link=line.strip()
num=1
while True:
            
            #use the browser to get the url.
            url = link+'ref=cm_cr_pr_btm_link_'+str(num)+'?ie=UTF8&showViewpoints=19&sortBy=helpful&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber='+str(num)
            response=browser.open(url)   
            html=response.read()  
            allnum = allnum + parsePage(html)
            num=num+1
            print url
            print allnum
            if html.find('Sorry, no reviews match your current selections.') != -1:
                break
    
#write the results
f.close()
fw=open('out.txt','w')
fw.write(str(allnum))
fw.close()
