from nltk.corpus import stopwords
import nltk.data
from nltk.util import ngrams
import re

stop = stopwords.words('english')

#read the input
f=open('in.txt')
text=f.read().strip().lower()
f.close()


#split sentences
sentences=re.split('\.',text)
print 'NUMBER OF SENTENCES: '+ str(len(sentences))

all2grams=set()

content = ''
allcontent = []
count1 = dict()
# for each sentence
for sentence in sentences:
    
    noun=set()#adjectives in this sentence
    other=set()#adverbs in this sentences
    
    sentence=re.sub('[^a-z\d]',' ',sentence)#replace chars that are not letters or numbers with a space
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower())   
    
    tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence
    
    for pair in tagged_terms: 
        
        #if the word is an adjective
        if pair[1].startswith('NN'): noun.add(pair[0])
        
        #if the word is an adverb
        # elif pair[1].startswith('RB'): adverbs.add(pair[0]) 
           
    twograms = ngrams(terms,2) #compute 2-grams
    
    #for each 2gram
    for tg in twograms:  
        if (tg[0] in noun and tg[1] not in stop) or (tg[1] in noun and tg[0] not in stop): # if the 2gram is a an adverb followed by an adjective
        	allcontent.append([tg[0],tg[1]])
        	if tg in count1:
        		count1[tg] +=1
        	else:
        		count1[tg] = 1
c=[]
for i in count1:
	if count1[i]>1:
		c.append([i[0],i[1]])
c.sort()
cs=''
for k in c:
	cs += k[0]+' '+k[1] +'\n'

fw = open('out.txt','w')
fw.write(cs)
fw.close
