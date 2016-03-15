"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

def loadtest(fname):
	reviews=[]
	f=open(fname)
	for line in f:
		reviews.append(line.lower())    
	f.close()
	return reviews

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')

#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#build a SVM classifier on the training data
# gnb=GaussianNB()
# gnb.partial_fit(counts_train,labels_train,np.unique(labels_train))

gnb=BernoulliNB()
gnb.fit(counts_train,labels_train)

#use the classifier to predict
predicted=gnb.predict(counts_test)

#print the accuracy
print accuracy_score(predicted,labels_test)
