from pandas import read_csv
import numpy as np
from pandas import read_csv
import sklearn
from sklearn.decomposition import PCA


from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

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
print y_train
print y_test

X_t_train = StandardScaler().fit_transform(X_train)
X_t_test = StandardScaler().fit_transform(X_test)


# feature extraction
pca = PCA(n_components=8)
pca_fit = pca.fit(X_train)


# summarize components
print("Explained Variance without Standard Scaling: %s") % pca_fit.explained_variance_ratio_
print("\n\n\n 	")
#print(pca_fit.components_)
#print type(pca_fit)
#print "\n\n\n"
var1 = np.cumsum(pca_fit.explained_variance_ratio_*100)
print var1
print "\n\n\n"

#SVM
clf = svm.SVC(kernel="rbf", C=1, gamma=0.01)
clf.fit(X_train, y_train) 

#Using this we can print output

predicted_labels = clf.predict(X_test)
print('{:.2%}\n'.format(accuracy_score(y_test, predicted_labels)))

pca = PCA(n_components=8)
pca_fit = pca.fit(X_t_train)

# summarize components
print("Explained Variance after Standard Scaling: %s") % pca_fit.explained_variance_ratio_
print("\n\n\n 	")
var1 = np.cumsum(pca_fit.explained_variance_ratio_*100)
print var1
print "\n\n\n"

clf = svm.SVC(kernel="rbf", C=1, gamma=0.1)
X_t_train1 = pca.transform(X_train)
X_t_test1 = pca.transform(X_test)
std_clf = make_pipeline(pca, clf)
std_clf.fit(X_t_train1, y_train)
pred_test_std = std_clf.predict(X_t_test1)
print('{:.2%}\n'.format(accuracy_score(y_test, pred_test_std)))
#Output is 1
