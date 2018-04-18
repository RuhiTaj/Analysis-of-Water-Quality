
import csv
import math


path = "/home/ubuntu/Desktop/ScoftComputng/water quality date sample.csv"

	
		
	
# serail[i][]

# 1-mg_weight;
# 2-ph_weight;
# 3-k_weight;
# 4-nit_weight;
# 5-sulp_weight;
# 6-ec_weight;
# 7-ca_weight;
# 8-na_weight;
# 9-carb_weight;
# 10-bicarb_weight;
# 11-chl_weight;
# 12-flr_weight;
# 13-sar_weight;
# 14-rsc_weight;
# 15-year;
# 

# 17-T_weight = 0;
# according to Indian drinking water standard (BIS 2004).
# try odouble check mg/l values

#http://cgwb.gov.in/documents/wq-standards.pdf - for values

Si = [1] * 15

place = ["23"] * 139
water_quality =  [None] * 139









#-999 fake values

# 1-mg_weight;
# 2-ph_weight;
# 3-k_weight;
# 4-nit_weight;
# 5-sulp_weight;
# 6-ec_weight;
# 7-ca_weight;
# 8-na_weight;
# 9-carb_weight;
# 10-bicarb_weight;
# 11-chl_weight;
# 12-flr_weight;
# 13-sar_weight;
# 14-rsc_weight;
# 15-year;
# 



Si[1] = 30
#0.1 micro mole/L
Si[2] = 0.1 * 0.001
Si[3] = 25
Si[4] = 45
Si[5] = 200
Si[6] = 25
Si[7] = 75
Si[8] = 200
#9 and 10 combined 500
#taken care in code
Si[9] = 500
Si[10] = 500
Si[11] = 250
Si[12] = 1
Si[13] = 3
Si[14] = 1.25




# for initilaisation

#for i in range (1,134):
#	a[i][17] = 0
#
#	for x in range (1,16):
#		a[i][x] =  -100
#	place[i] = "Place"

#https://www.researchgate.net/post/How_to_calculate_water_quality_Index - for formula

w, h = 139, 20
a = [[0 for x in range(w)] for y in range(h)] 
sub_index = [[0 for x in range(w)] for y in range(h)] 
qual_scale = [[0 for x in range(w)] for y in range(h)] 
Ci_mgPl = [[0 for x in range(w)] for y in range(h)] 
sub_wei = [[0 for x in range(w)] for y in range(h)] 

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

# print "Check begin\n\n"

# for i in range(1,10):
# 	print i
# 	#print "\t"
# 	for j in range(1,16):
# 		print a[i][j]
# 		#print "\t"
# 	print "\n\n"

# print "Check End\n\n"


sub_index = []
for i in xrange(139):
     sub_index.append([])
     for j in xrange(20):
             sub_index[i].append(i+j)

qual_scale = []
for i in xrange(139):
     qual_scale.append([])
     for j in xrange(20):
             qual_scale[i].append(i+j)

Ci_mgPl = []
for i in xrange(139):
     Ci_mgPl.append([])
     for j in xrange(20):
             Ci_mgPl[i].append(i+j)

sub_wei = []
for i in xrange(139):
     sub_wei.append([])
     for j in xrange(20):
             sub_wei[i].append(i+j)


for i in range (1,139):
	a[i][9] = a[i][9]+a[i][10]

for i in range (1,139):
	a[i][2] = math.pow(10, -a[i][17])
	a[i][2] = a[i][2]*0.001

for i in range (1,139):
	a[i][17] = 0

	for x in range (1,15):
		if x!=10 and x!=6and x!=13:
			a[i][17] = a[i][17] + a[i][x]  

	for x in range (1,15):
		if a[i][17] == 0:
			break
		if x!=10 and x!=6and x!=13:
			#a[i][17] = a[i][17] + a[i][x]		
			sub_wei[i][x] = a[i][x]/a[i][17]
			Ci_mgPl[i][x] = a[i][x]
			qual_scale[i][x] = ( Ci_mgPl[i][x] / Si[x] )*100
			sub_index[i][x] = sub_wei[i][x] * qual_scale[i][x]

	water_quality[i] = 0

	for x in range (1,15):
		if x!=10 and x!=6 and x!=13:
			#a[i][17] = a[i][17] + a[i][x]  		
			water_quality[i] = sub_index[i][x] + water_quality[i]

water_index=  [None] * 139

for i in range (1,139) :
	water_index[i] = abs(5-round(water_quality[i]/100))
	print abs(5-round(water_quality[i]/100))
	print "\n\n"

for i in range(1,139) :
	if water_index[i]==0:
		water_index[i] = 1.0
	
# water_index in terms of those 1 and 2



