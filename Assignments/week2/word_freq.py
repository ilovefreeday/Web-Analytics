"""
Introductory Python Script, BIA660-Fall 2015.
Counts the number of times that each word shows up in all the posts in the file
"""

#Make a new empty dictionary. This will hold the number of occurences per word
word_freq=dict()

file_conn=open('data')#open a connection to the input file

for line in file_conn: # for every line in the input
    
    # the strip() function removes spaces, tabs, and 'line change' 
    # character from the start and end of a piece of text. 
    #Look at what happens to the count of the word 'house' if we don't do this strip.
    line=line.strip() 
    
    columns=line.split('@') # split according to the delimeter
  
    user=columns[0] # get the user
    day=columns[1] # get the day   
    post=columns[2]    #get the post

    words=post.split(' ')#split the post on the space to get a list of the words
   
    for word in words: # for each word in the post
        if word in word_freq:# the word has been seen before, add +1 to its count.
            word_freq[word]=word_freq[word]+1
        else:
           word_freq[word]=1 # first time we see this word, initialise its count to 1.


file_conn.close() # always remember to close the connection once your are done working with a file

#print the counts
for word in word_freq:#for each user
    print word,word_freq[word] # print the user's name and his count.
    
#write the results to a file

newfile_conn=open('word_counts.txt','w')#create a new file and open a connection to it.
for word in word_freq:#for each user
    newfile_conn.write(word+' '+str(word_freq[word])+'\n') # write the user's name and his count to the file. Why do we use str() here?
newfile_conn.close()#close the connection 


    
    
    
