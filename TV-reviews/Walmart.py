# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:42:54 2015

@author: Rohini
"""

import re,urllib2,sys
browser=urllib2.build_opener()
#file to write output 
fw=open('review.txt','w')
pagesToGet=329#no of pages to get 
a=[]
b=[]
c=[]

#list to read all reviews
#open the url 
#loop to read through pages
for page in range(1,pagesToGet+1):
    
    print 'processing page :', page

    url='https://www.walmart.com/reviews/product/25059351?limit=20&page='+str(page)+'&sort=helpful'
    
    try:
         #use the browser to get the url.
         response=browser.open(url)    
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    #read the html   
    html=response.read()
    reviews=re.finditer('<p class=js-customer-review-text data-max-height=110>(.*?)</p>',html)
    dates=re.finditer('review-date hide-content display-inline-block-m">(.*?)</span>',html)
    ratings=re.finditer('<span class=visuallyhidden>(.+?)</span>',html)

    
    
    for review in reviews:
        review_r=review.group(1)
        a.append(review_r)
        
    for rating in ratings:
        b.append(rating.group(1).replace(' stars',''));
        
    for date in dates:
        c.append(date.group(1))
        
for x,y,z in zip(a,b,c):
    fw.write('walmart.com\t'+x+'\t'+y+'\t'+z+'\n')
    
fw.close()
        
