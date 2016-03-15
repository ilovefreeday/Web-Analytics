# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:08:18 2015

@author: NEPTUNE
"""

import re
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver

def parsePage(html,reviewList,ratingList,dateList):
    temre=[]
    temra=[]
    temda=[]
    
    ratings=re.finditer('<span property="v:value" class="BVRRNumber BVRRRatingNumber">(.*?)</span>',html)
    for rating in ratings:
        temra.append(rating.group(1).strip())
    del temra[0]
    del temra[len(temra)-1]
    
    reviews=re.finditer('<span class="BVRRReviewText">(.*?)</span>',html)
    for review in reviews:
        temre.append(review.group(1).strip()) 
        
    dates=re.finditer('<span property="v:dtreviewed" content="(.*?)" class="BVRRValue BVRRReviewDate">(.*?)<span property="v:value-title"></span></span>',html)
    for date in dates:
        temda.append(date.group(1).strip())
    
    if len(temre)==len(temra):    
        ratingList.extend(temra)
        reviewList.extend(temre)
        dateList.extend(temda)
    

url='http://www.bestbuy.com/site/insignia-32-class-31-1-2-diag--led-720p-hdtv-black/6080010.p?id=1219191179593&skuId=6080010'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

time.sleep(2)

button=driver.find_element_by_css_selector('#ui-id-3')
button.click() #click on the button
time.sleep(2)

reviewList=[]
ratingList=[]
dateList=[]

parsePage(driver.page_source,reviewList,ratingList,dateList)
print 'page 1 done'
page=2
while len(ratingList)<=1000:
    cssPath='#BVRRDisplayContentFooterID > div > span.BVRRPageLink.BVRRNextPage > a'
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break
    
    button.click()
    time.sleep(1)
    parsePage(driver.page_source,reviewList,ratingList,dateList)
    print 'page',page,'done'
    page+=1
print len(reviewList)
print len(ratingList)
print len(dateList)


fw=open('reviews.txt','w')
for i in range(1000):
    fw.write('bestbuy.com'+'\t'+reviewList[i]+'\t'+str(ratingList[i])+'\t'+str(dateList[i])+'\n')
fw.close()