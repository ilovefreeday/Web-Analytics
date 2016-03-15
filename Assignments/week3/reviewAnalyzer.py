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
negLex=loadLexicon('negative-words.txt')


file_writer=open('results.txt','w')

data_conn=open('input.txt')
for line in data_conn: # for every line in the file (1 review per line)
    posList=[] #list of positive words in the review
    negList=[] #list of negative words in the review

    line=line.strip()    
    
    words=line.split(' ') # slit on the space to get list of words
    
    for word in words: #for every word in the review
        if word in posLex: # if the word is in the positive lexicon
            posList.append(word) #update the positive list for this review
        if word in negLex: # if the word is in the negative lexicon
            negList.append(word) #update the negative list for this review
           

    decision='Neutral'           
    if len(posList)>len(negList): # more pos words than neg
        decision='Positive'
    elif len(negList)>len(posList):  # more neg than pos
        decision='Negative'
         
    file_writer.write(line+'\n') #write the review
    file_writer.write(str(posList)+'\n') # write list of positive words
    file_writer.write(str(negList)+'\n') # write list of negative words     
    file_writer.write(decision+'\n\n') #write the decision
     
           
file_writer.close()
data_conn.close()


