"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn.linear_model import LogisticRegression

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
c0=KNeighborsClassifier(5)
c1=SVC(kernel='linear',C=0.025)
c2=SVC(gamma=2,C=1)
c3=SVC()
c4=DecisionTreeClassifier(max_depth=5)
c5=MultinomialNB()
c6=AdaBoostClassifier()
# c7=LDA()
# c8=QDA()
c7=BernoulliNB()
c8=LogisticRegression()
c9=RandomForestClassifier(max_depth=5,n_estimators=10,max_features=1)

c0.fit(counts_train,labels_train)
c1.fit(counts_train,labels_train)
c2.fit(counts_train,labels_train)
c3.fit(counts_train,labels_train)
c4.fit(counts_train,labels_train)
c5.fit(counts_train,labels_train)
c6.fit(counts_train,labels_train)
c7.fit(counts_train,labels_train)
c8.fit(counts_train,labels_train)
c9.fit(counts_train,labels_train)

#use the classifier to predict
p0=c0.predict(counts_test)
p1=c1.predict(counts_test)
p2=c2.predict(counts_test)
p3=c3.predict(counts_test)
p4=c4.predict(counts_test)
p5=c5.predict(counts_test)
p6=c6.predict(counts_test)
p7=c7.predict(counts_test)
p8=c8.predict(counts_test)
p9=c9.predict(counts_test)



#print the accuracy
print accuracy_score(p0,labels_test)
print accuracy_score(p1,labels_test)
print accuracy_score(p2,labels_test)
print accuracy_score(p3,labels_test)
print accuracy_score(p4,labels_test)
print accuracy_score(p5,labels_test)
print accuracy_score(p6,labels_test)
print accuracy_score(p7,labels_test)
print accuracy_score(p8,labels_test)
print accuracy_score(p9,labels_test)
