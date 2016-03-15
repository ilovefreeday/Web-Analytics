"""
Introductory Python Script, BIA660-Fall 2015.
Counts the number of posts per user
"""

#Make a new empty dictionary. This will hold the number of posts per user.
user_freq=dict()

file_conn=open('data')#open a connection to the input file

for line in file_conn: # for every line in the input

    columns=line.split('@') # split according to the delimeter
  
    user=columns[0] # get the user
    day=columns[1] # get the day   
    post=columns[2]    #get the post

    if user in user_freq: # the user has been seen before, add +1 to his count.
        user_freq[user]=user_freq[user]+1
    else: # first time we see this user, initialise his count to 1. 
        user_freq[user]=1

file_conn.close() # always remember to close the connection once your are done working with a file

#print the counts
for user in user_freq:#for each user
    print user,user_freq[user] # print the user's name and his count.
    
#write the results to a file
newfile_conn=open('user_counts.txt','w')#create a new file and open a connection to it.
for user in user_freq:#for each user
    newfile_conn.write(user+' '+str(user_freq[user])+'\n') # write the user's name and his count to the file. Why do we use str() here?
newfile_conn.close()#close the connection 


    
    
    
