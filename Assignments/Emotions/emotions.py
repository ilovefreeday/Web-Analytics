from nltk.corpus import stopwords
import nltk.data
from nltk.util import ngrams
import re,operator

time = 0

fdata = open('data.txt','r')
tmp_data = fdata.read().lower().split('\n')[:-1]
# tmp_data = tmp_data[:200]
fdata.close()

femotion = open('emotions.txt','r')
tmp_emotion = femotion.read().strip().lower().split('\n')
# tmp_emotion = tmp_emotion[:200]
femotion.close()
word = tmp_emotion[0].strip().split('\t')

matrix = []
for i in tmp_emotion[1:]:
	matrix.append(i.strip().split('\t'))
adv = []
for i in matrix:
	adv.append(i[0])

array = dict()
for i in matrix:
	array[i[0]] = []
	for j in range(1,len(i)):
		if i[j] =='1':
			array[i[0]].append(word[j])

remove = [k for k in array if array[k] == []]
for k in remove: 
	del array[k]

noun = set()
for i in tmp_data:
	print time
	time +=1
	i=re.sub('[^a-z\d]',' ',i)
	i=re.sub(' +',' ',i).strip()
	terms = nltk.word_tokenize(i.lower())
	# print terms
	tagged_terms=nltk.pos_tag(terms)
	for j in tagged_terms:
		if j[1] == 'NN':
			noun.add(j[0])

count = dict()
for i in noun:
	count[i] = []

for i in tmp_data:
	print time
	time +=1
	i=re.sub('[^a-z\d]',' ',i)
	i=re.sub(' +',' ',i).strip()
	tmp = i.lower().split(' ')
	for j in tmp:
		if j in count:
			for k in tmp:
				for l in adv:
					if k == l:
						count[j].append(k)

remove = [k for k in count if count[k] == []]
for k in remove: 
	del count[k]	

new = dict()
for i in count:
	print time
	time +=1
	new[i] = []
	for j in count[i]:
		if j in array:
			new[i].append(array[j])

remove = [k for k in new if new[k] == []]
for k in remove: 
	del new[k]

result = dict()
for i in word:
	result[i] = []

for i in new:
	for j in new[i]:
		for k in j:
			result[k].append(i)

for i in result:
	fw = open(i+'.txt','w')
	for  j in result[i]:
		fw.write(j+',')
	fw.close()

names = ['anger.txt', 'anticipation.txt', 'disgust.txt', 'fear.txt', 'joy.txt', 'sadness.txt', 'surprise.txt', 'trust.txt']
final = dict()
for i in range(len(names)):
	name = names[i]
	fcount = open(name,'r')
	text = fcount.read().split(',')[:-1]
	for j in text:
		if j in final:
			final[j] += 1
		else:
			final[j] = 1
	fcount.close()
	
	# final_sort = sorted(final.items(), key=operator.itemgetter(1))
	ff = open('result.txt','a')
	ff.write(name[:-4]+'\n')
	print name[:-4]
	
	for k in final:
		ff.write(k+':'+str(final[k])+', ')
		print k,final[k]
	ff.write('\n\n')
	ff.close()
	print



