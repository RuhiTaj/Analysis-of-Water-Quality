
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

print X
print "\n\n\n"
print Y
print "\n\n\n"
# feature extraction
pca = PCA(n_components=8)
fit = pca.fit(X)

print "\n\n\n\n\nHey\n\n\n\n"
print fit
print "\n\n\n\n\nHey\n\n\n\n"

# summarize components
print("Explained Variance: %s") % fit.explained_variance_ratio_
print("\n\n\n\n\n\n")
print(fit.components_)
print "\n\n\n\n\n"
