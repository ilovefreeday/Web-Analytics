
import re
import time,sys
from selenium import webdriver

#extract the set of users in a given html page and add them to the given set
def parsePage(html,userSet):
    users=re.finditer('<span property="v:reviewer" class="BVRRNickname">(.*?)</span>',html)    
    for user in users:
        userSet.add(user.group(1).strip())

#main url of the item
url='http://www.bestbuy.com/site/westinghouse-40-class-39-5-diag--led-1080p-hdtv-black/7617086.p?id=1219680881728&skuId=7617086'

#open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

#sleep for 2 seconds
time.sleep(2)

#find the 'Ratings and Reviews' button based on its css path
button=driver.find_element_by_css_selector('#ui-id-3')
button.click() #click on the button
time.sleep(2) #sleep

#includes all the distinct users we could retrieve.
allusers=set()

#parse the first page of reviews
parsePage(driver.page_source,allusers)
print 'page 1 done'


page=2
while True:
    #get the css path of the 'next' button
    cssPath='#BVRRDisplayContentFooterID > div > span.BVRRPageLink.BVRRNextPage > a'
    
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break

    #click the button to go the next page, then sleep    
    button.click()
    time.sleep(2)
    
    #parse the page
    parsePage(driver.page_source,allusers)

    print 'page',page,'done'
    page+=1
    
#write the results
fw=open('bestbuy.txt','w')
for user in allusers:
    fw.write(user+'\n')
fw.close()
