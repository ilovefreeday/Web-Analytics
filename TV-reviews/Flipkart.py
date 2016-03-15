# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 18:46:47 2015

@author: Sapna
"""
import time,sys,urllib2
import requests
from lxml import html

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)
def remove_nextlinechar(text):
    return text.replace('\n', ' ')

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
fw=open('reviews4.txt','w')
index=0
page=0
rev = []
ratingStar=[]
ratingDate=[]
while (page<230):
    url='http://www.flipkart.com/micromax-50c1200fhd-50c5500fhd-124-cm-49-led-tv/product-reviews/ITMEYFK4AHYHMEWX?pid=TVSEYFESRAMHZJT2&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start='+str(page)

    try:
        myHtml=requests.get(url)
        time.sleep(2)
    except Exception:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
    
    tree = html.fromstring(myHtml.text)   
    reviews = tree.xpath('//span[@class="review-text"]')
    for review in reviews:
        rev.append(remove_non_ascii(review.text_content()))
    stars= tree.xpath('//div[@class="fk-stars"]/@title')
    for star in stars:
        ratingStar.append(star)
    dates=tree.xpath('//div[@class="date line fk-font-small"]/text()')
    for date in dates:
        ratingDate.append(date)
    
    page+=10
    
while (index <len(rev)):
        fw.write(str('flipkart.com') + '\t' + str(remove_nextlinechar(rev[index])) + '\t' + 
        str(ratingStar[index]) + '\t' + str(remove_nextlinechar(ratingDate[index])) + '\n') 
        index+=1    

fw.close()

