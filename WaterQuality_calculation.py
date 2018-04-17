
import csv

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







Si[1] = 30
Si[2] = 7
Si[3] = -999
Si[4] = 45
Si[5] = 200
Si[6] = 25
Si[7] = 75
Si[8] = -999
Si[9] = -999
Si[10] = -999
Si[11] = 250
Si[12] = 1
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

print "Check begin\n\n"

for i in range(1,10):
	print i
	#print "\t"
	for j in range(1,16):
		print a[i][j]
		#print "\t"
	print "\n\n"

print "Check End\n\n"


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





for i in range (1,134):
	a[i][17] = 0

	for x in range (1,15):
		a[i][17] = a[i][17] + a[i][x]  

	for x in range (1,15):
		if a[i][17] == 0:
			break
		sub_wei[i][x] = a[i][x] / a[i][17]
		Ci_mgPl[i][x] = a[i][x]
		qual_scale[i][x] = ( Ci_mgPl[i][x] / Si[x] )*100
		sub_index[i][x] = a[i][x] * qual_scale

	for x in range (1,15):
		water_quality[i] = sub_index[i][x]




