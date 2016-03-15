"""
Introductory Python Script, BIA660-Fall 2015.
Counts the number of tweets per day

"""

#Make a new empty dictionary. This will hold the number of posts per day.
day_freq=dict()

file_conn=open('data')#open a connection to the input file

for line in file_conn: # for every line in the input

    columns=line.split('@') # split according to the delimeter
  
    user=columns[0] # get the user
    day=columns[1] # get the day   
    post=columns[2]    #get the post

    if day in day_freq: # the day has been seen before, add +1 to his count.
       day_freq[day]=day_freq[day]+1
    else: # first time we see this day, initialise his count to 1. 
       day_freq[day]=1

file_conn.close() # always remember to close the connection once your are done working with a file

#print the counts
for day in day_freq:#for each user
    print day,day_freq[day] # print the user's name and his count.
    
#write the results to a file
newfile_conn=open('day_counts.txt','w')#create a new file and open a connection to it.
for day in day_freq:#for each user
    newfile_conn.write(day+' '+str(day_freq[day])+'\n') # write the user's name and his count to the file. Why do we use str() here?
newfile_conn.close()#close the connection 


    
    
    
