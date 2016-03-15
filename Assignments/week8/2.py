# from nltk.corpus import stopwords
import nltk.data
from nltk.util import ngrams

#read the input
f = open('in.txt')
fw = open('out.txt','w')
text = f.read().strip()

content = ''
sen = ''
sentences = text.split('\n')

for sentence in sentences:
    terms = sentence.split()
    tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence
               
    twograms = ngrams(terms,2) #compute 2-grams

    for tg in twograms:  
        if tg[0].lower() == 'not': # if the 2gram is a an adverb followed by an adjective
            # print sentence
            new_word = tg[0]+tg[1]
            tmp = sentence.split(tg[1])
            tmp[0] = tmp[0][:-4]
            sentence = str(str(tmp[0]) + new_word + str(tmp[1]))
            # print sentence
    content += sentence + '\n'

f.close()
fw.write(content)
fw.close()
