"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


#read the reviews and their polarities from a given file
def loadData(fname,sec=None):
	
	if sec is None:
	    reviews=[]
	    labels=[]
	    f=open(fname)
	    for line in f:
	        review,rating=line.strip().split('\t')  
	        reviews.append(review.lower())    
	        labels.append(int(rating))
	    f.close()
	    return reviews,labels

	else:
		reviews=[]
		labels=[]
		f1=open(fname)
		f2=open(sec)
		review=f1.read().strip().split('\n')
		for i in range(len(review)):
			reviews.append(review[i].lower())
		rating =f2.read().strip().split('\n')
		for j in range(len(rating)):
			labels.append(int(rating[j]))
		f1.close()
		f2.close()
		return reviews,labels


rev_train,labels_train=loadData('train.txt')
rev_test,labels_test=loadData('in.txt','correct.txt')


#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#build a 3-NN classifier on the training data
KNN=KNeighborsClassifier(500) 
KNN.fit(counts_train,labels_train)

#use the classifier to predict
predicted=KNN.predict(counts_test)
for i in predicted:
	print i
#print the accuracy
print accuracy_score(predicted,labels_test)
