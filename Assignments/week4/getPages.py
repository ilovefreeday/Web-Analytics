"""
This script reads the file that was created by getFreelancerUsers.py line-by-line.
Each line contains the url to the profile page of a freelancer. The script then downloads
the profile page for each url and stores it in a new file. The name of the new file should
be the same as the username of the corresponding freelancer.

 """ 
 
# import the libraries we will be using
import urllib2,os,sys

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

# this is the name of the folder where we will download the profile pages.
outFolder='freelancerPages'

# if the folder doesn't exist, make it 
if not os.path.exists(outFolder): # use path.exists() from the os library to check if something exists
    os.mkdir(outFolder) # use mkdir() from the os library to make a new directory

# open a connection to the file you want to read
fileReader=open('freelancers.txt')
for line in fileReader: # this syntax allows us to read the file line-by-line
        
        link=line.strip() # .strip() removes white spaves and line-change characters from the beginning and end of a string
        
        print 'Donwloading: ', link
        
        try:
            #use the browser to get the url.
            response=browser.open(link)    
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',link
            print error_type, 'Line:', error_info.tb_lineno
            continue
    
        html=response.read()    
    
        name=link[link.rfind('/')+1:]
        
        #open a new file in the pre-specified folder, write the html  , and close it.
        fileWriter=open(outFolder+'/'+name, 'w')
        fileWriter.write(html)
        fileWriter.close()

   
fileReader.close()