import csv

path = "/home/ubuntu/Desktop/ScoftComputng/water quality date sample.csv"

	
place = ["23"] * 139
a = []
for i in xrange(139):
     a.append([])
     for j in xrange(20):
             a[i].append(i+j)

store = ''

# Assign Values
with open(path , 'rb') as f:
    reader = csv.reader(f)
    i=-1
    for line in f :
	#print line
	i = i+1
	if i>0 :
	
		j = 0
		if i > 138:
			break
		word_no = 0

		if i>1 :
			a[i-1][15] = store

		store=''

		for word in line:

			if word == ',':
				word_no = word_no+1

			if word_no >= 1 and word!= ',':
				store = store + word

			if word == ',' and word_no>=1:
				j = j+1
				if j>=3 and j<18:
					#print a[i][j-2]
					#print "\n"

					a[i][j-2] = float(store)
					#if j==16:
						#print float(store)
					#print a[i][j-2]
					#print "\n"
				elif j==2 :
					place[i] = store
				next_store = store
				store=''

a[138][15] = 2005.0

# tocheck if properl assigned

print "Check begin\n\n"

for i in range(1,10):
	#print "\t"
	print i
	print place[i]
	for j in range(1,16):
		print a[i][j]
	
		#print "\t"
	print "\n\n\n\n"

print "Check End\n\n"


