import matplotlib.pyplot as plt
import numpy as np
import math

from pandas import read_csv
from sklearn.decomposition import PCA
# load data
url = '/home/ubuntu/Desktop/SoftComputing/SoftComp1/water quality date sample.csv'

names = ['MG','PH','K','NITRATE','SULPHATE','CARBONATE','CHLORIDE','FLUORIDE', 'Water Quality']
dataframe = read_csv(url, names=names)
array = dataframe.values

#print "-------\n\n"
#print X
#print "-------\n\n"

X = array[:,0:8]
Y = array[:,8]

#print X
#print "\n\n\n"
#print Y
#print "\n\n\n"
# feature extraction
num = 5
pca = PCA(n_components=num)
fit = pca.fit(X)

#print "\n\n\n\nFit:\n\n"
#print fit


#print("\n\n\nExplained Variance: %s") % fit.explained_variance_ratio_
#print("\n\n\n\nFit componentes:\n\n")
#print(fit.components_)
#print "\n\n\n\n\n"

for i in range(0,8):
	#print " Vector of "
	#print names[i]
	value =0
	for j in range(0,num):
		#print fit.components_[j][i]
		value = value + (fit.components_[j][i] * fit.components_[j][i])
		Y[i] = math.sqrt(value)
		
	#print "\n\n\n"
	

# for i in range (1,6):
# 	no_pc[i] = fit.components_[i]

#for i in range(0,8):
	#print names[i]
	#print Y[i]
	#print "\n\n"



#print "\n\n\n\nCheck\n\n\n\n"

#print pca

print "\n\n\n\nInput Matrix:\n"
print X
print "\n\n\n\nOut Matrix after dimension reduction:\n"
print pca.transform(X)
print "\n\n\n\nOriginal vectors in terms of reduced dimensions\n\n"
print (pca.fit(X)).components_
value = "string"
val=0


print "\n\n\n\n\n"	
for i in range(0,8):
	print "Eigen Vector of the original component - %s : \n" % names[i]
	#print names[i]
	value =0
	valu = 0
	for j in range(0,num):
		print fit.components_[j][i]
		valu =  (fit.components_[j][i] * fit.explained_variance_ratio_[j])
		valu = valu * valu
		value = value + valu
	Y[i] = math.sqrt(value)
		
	print "\n\n\n"

print("\n\n\nExplained Variance of the reduced dimensions :\n\n\n %s") % fit.explained_variance_ratio_


#print "Order of the Attributes contribution to the new dimensions:\n"
for i in range(0,8):
	count = 0 
	#print names[i]

value = "string"
val=0

for i in range(0,8):
	for j in range(1,8):
		if Y[i]>Y[j]:
			val = Y[i]
			Y[i] = Y[j]
			Y[j] = val
			value = names[i]
			names[i] = names[j]
			names[j] = value
			
print "\n\n\nOrder of the Attributes contribution to the new dimensions:\n"
for i in range(0,8):
	print "",i+1,names[i]


#print X
count = 0 
for i in X:
	count = count +1
print "\n\n\n"
#print count
#print "\n\n\n\n----\n\n\n\n"

#print res
count = 0 
for i in X:
	count = count +1
#print "\n\n\n"
#print count
#print "\n\n\n---\n\n\n"
#print (pca.fit(X)).components_


# summarize components
