# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:13:10 2015

@author: YeTian
"""

"""
Reads a list of reviews and decide if each review is positive or negative,
based on the occurences of positive and negative words.
Writes the results in a file.
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


#load the positive and negative lexicons
posLex=loadLexicon('positive-words.txt')

file_writer=open('winner.txt','w')

word_freq = dict()
data_conn=open('input.txt')
for line in data_conn: # for every line in the file (1 review per line)
    #list of positive words in the review
    
    line=line.strip()    
    
    words=line.split(' ') # slit on the space to get list of words
    
    for word in words: #for every word in the review
        if word in posLex:
            
            if word in word_freq:# the word has been seen before, add +1 to its count.
                word_freq[word]=word_freq[word]+1
            else:
                word_freq[word]=1

count = 0
winner = ''
for y in word_freq:
    if word_freq[y]>count:
        count = word_freq[y]
        winner = y
        print winner
#print winner
file_writer.write(winner) #write the review

           
file_writer.close()
data_conn.close()