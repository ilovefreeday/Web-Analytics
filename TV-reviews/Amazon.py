# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:29:55 2015

@author: nehaanandpara
"""

import urllib2,re,sys,time

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
page=1
reviews=list()
rate1=list()
date1=list()

def fx(html,reviews,rate1,date1):
    a=[]
    b=[]
    c=[]
    retext=re.finditer('<span class="a-size-base review-text">(.*?)</span>',html)
    redate=re.finditer('review-date">on (.*?)</span>',html)
    rerate=re.finditer('review-rating"><span class="a-icon-alt">(.*?) out of 5 stars',html)
    
    for review in retext:
        reviewtext=review.group(1)
        a.append(reviewtext)
        
    for date in redate:
        date=date.group(1)
        b.append(date)
        
    for rate in rerate:
        rates=rate.group(1)
        c.append(rates)
    print b
    if b!=[]:
        del b[0],b[1]
    if c!=[]:
        del c[0],c[1]
    
    if len(a)==len(b) and len(b)==len(c):
        reviews.extend(a)
        rate1.extend(b)
        date1.extend(c)
    
l=0   
while len(date1)<=1000:
    url='http://www.amazon.com/VIZIO-E50-C1-50-Inch-1080p-Smart/product-reviews/B00SMBFP4U/ref=cm_cr_pr_btm_link_'+str(page)+'?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber='+str(page)
    try:
        #use the browser to get the url.
        response=browser.open(url)    
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    html=response.read()
    time.sleep(1)
    fx(html,reviews,rate1,date1)
    if l==len(rate1):
        page-=1
    l=len(rate1)
    print page
    page+=1
fw=open('reviews.txt','w')
for i in range(1000):
    fw.write('amazon.com'+'\t'+reviews[i]+'\t'+str(date1[i])+'\t' + str(rate1[i])+'\n')
fw.close()

        
      
    




    
        
       
    
    
    
    