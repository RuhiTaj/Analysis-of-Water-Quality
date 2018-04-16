from sklearn import svm
# X and y have to be taken as input 
X = [[0, 0], [1, 1]]
y = [0, 1]

#SVM
clf = svm.SVC()
clf.fit(X, y) 

#Using this we can print output
#print clf.predict([[1, 1]])
#Out put is 1
