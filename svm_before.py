from sklearn import svm
# X and y have to be taken as input
import numpy
from pandas import read_csv
from sklearn.decomposition import PCA
# load data
url = '/home/ubuntu/Desktop/ScoftComputng/dataset.csv'


names = ['MG','PH','K','NITRATE','SULPHATE','CARBONATE','CHLORIDE','FLUORIDE', 'Water Quality']
dataframe = read_csv(url, names=names)
array = dataframe.values



X = array[:,0:8]
Y = array[:,8]

P = array[0:5,0:8]

y=0

for i in X:
	y=y+1
	
#	if y< 18:
#		C[y] = X[y]
#	else:
#		P[y] = X[y]

print X
print "\n\n\n"
print Y
print "\n\n\n"


#names = ['MG','PH','K','NITRATE','SULPHATE','CARBONATE','CHLORIDE','FLUORIDE']
#dataframe = read_csv(url, names=names)
#array = dataframe.values

#pedda

print P

#SVM
clf = svm.SVC()
clf.fit(X, Y) 

print "\n\n\n--------------------\n\n\n\n\n\n"

for i in P:
	print clf.predict([i])

print "\n\n\n--------------------\n\n\n\n\n\n"
#for i in P:
 #print i

#Using this we can print output
#print clf.predict([[1, 1]])
#Out put is 1
