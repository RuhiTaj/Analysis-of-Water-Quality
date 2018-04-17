

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
# 16-place;

# 17-T_weight = 0;

Si[1] = 30
Si[2] = 7
Si[3] =
Si[4] = 45
Si[5] = 200
Si[6] = 25
Si[7] = 75
Si[8] = 
Si[9] = 
Si[10] =
Si[11] = 250
Si[12] = 1
Si[14] = 1.25



for i in range (1,134):
	a[i][17] = 0

	for x in range (1,15):
		a[i][17] = a[i][17] + a[i][x]  

	for x in range (1,15):
		sub_wei[i][x] = a[i][x] / a[i][17]
		Ci_mgPl[i][x] = a[i][x]
		qual_scale[i][x] = ( Ci_mgPl[i][x] / Si[x] )*100
		sub_index[i][x] = a[i][x] * qual_scale

	for x in range (1,15):
		water_quality[i] = sub_index[i][x]



