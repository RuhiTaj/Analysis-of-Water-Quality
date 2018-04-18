import numpy
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from pandas import read_csv
# load data
url = '/home/ranjith/Analysis-of-Water-Quality-master/dataset.csv'

names = ['MG','PH','K','NITRATE','SULPHATE','CARBONATE','CHLORIDE','FLUORIDE', 'Water Quality']
dataframe = read_csv(url, names=names)
array = dataframe.values

X_train = array[0:18][:,0:8]
y_train = array[0:18][:,8]
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)
X_test = array[18:23][:,0:8]
y_test = array[18:23][:,8]




#SVM
clf = svm.SVC(kernel="rbf", C=100, gamma=0.1)
clf.fit(X_train, y_train) 

#Using this we can print output

predicted_labels = clf.predict(X_test)
print predicted_labels
print"\n\n"
print('{:.2%}\n'.format(accuracy_score(y_test, predicted_labels)))

#Output is 1
