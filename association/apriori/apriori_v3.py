# test_data = {
# 				't1':['mango', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
# 				't2':['doll', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
# 				't3':['mango', 'apple', 'knife', 'eggs'],
# 				't4':['mango', 'umbrella', 'corn', 'knife', 'yoyo'],
# 				't5':['corn', 'onion', 'onion', 'knife', 'eggs', 'ice_cream'],
# 			}

# test_data = {
# 				't1':['broccoli', 'green_peppers', 'corn'],
# 				't2':['asparagus', 'squash', 'corn'],
# 				't3':['corn', 'tomatoes', 'beans', 'squash'],
# 				't4':['corn', 'tomatoes', 'beans', 'squash'],
# 				't5':['beans', 'asparagus', 'broccoli'],
# 				't6':['squash', 'asparagus', 'beans', 'tomatoes'],
# 				't7':['tomatoes', 'corn'],
# 				't8':['broccoli', 'tomatoes', 'green_peppers'],
# 				't9':['squash', 'asparagus', 'beans'],
# 				't10':['beans', 'corn'],
# 				't11':['green_peppers', 'broccoli', 'beans', 'squash'],
# 				't12':['asparagus', 'beans', 'squash'],
# 				't13':['squash', 'corn', 'asparagus', 'beans'],
# 				't14':['corn', 'green_peppers', 'tomatoes', 'beans', 'broccoli'],
# 			}

# test_data = {
# 				't1': ['a', 'c', 'd', 'e'],
# 				't2': ['b', 'c', 'd', 'e'],
# 				't3': ['b', 'c', 'd'],
# 				't4': ['a', 'e'],
# 				't5': ['b', 'c', 'd'],
# 				't6': ['a', 'd', 'e'],
# 				't7': ['b', 'd'],
# 				't8': ['b', 'c'],
# 				't9': ['b', 'e'],
# 				't10': ['a', 'b', 'c'],
# 				't11': ['a', 'b', 'e'],
# 				't12': ['a', 'c'],
# 				't13': ['a', 'c', 'e'],
# 				't14': ['b', 'd', 'e'],
# 				't15': ['a', 'b', 'd'],
# 				't16': ['c', 'e'],
# 				't17': ['a', 'b', 'd', 'e'],
# 				't18': ['d','e'],
# 				't19': ['a', 'd', 'c'],
# 				't20': ['a', 'b', 'c', 'd']
# 			}

# test_data = {
# 				't1': ['ROTI BANTAL PANJANG', 'SELE BUNGKUS', 'DETOL SABUN 110 REENERGIZER', 'INDOMIE 65 KA KALDU AYAM'],
# 				't2': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 VITAPROTECT', 'CHEETOS 48 JAGUNG BAKAR', 'LAYS 40 RASA RUMPUT LAUT'],
# 				't3': ['EKONOMI 300 E500K BAG', 'EKONOMI 300 EL500K LEMON', 'FORCE MAGIC 470 KUNING LMN', 'SQ MONTES 55'],
# 				't4': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 LEMON FRESH', 'ROKOK SAMPOERNA MILD 16'],
# 				't5': ['GULA PASIR 2 KG', 'BIMOLI SPESIAL REF 2 LITER', 'KUE JAGUNG AUSTRALI 1/2 KG'],
# 				't6': ['ROTI BANTAL PANJANG', 'SELE BUNGKUS', 'TS SWEETENER 25S DIABETIC', 'KAPAS SELECTION 35', 'TEBS TSE SODA 500'],
# 				't7': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 VITAPROTECT', 'SGM 2 400 ANANDA'],
# 				't8': ['EKONOMI 300 E500K BAG', 'EKONOMI 300 EL500K LEMON', 'GULAKU 1 KG PREMIUM'],
# 				't9': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 LEMON FRESH', 'GRIP X RED, AMPLOP LEBARAN'],
# 				't10': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 VITAPROTECT'],
# 				't11': ['GULA PASIR 2 KG', 'BIMOLI SPESIAL REF 2 LITER'],
# 				't12': ['EKONOMI 300 E500K BAG', 'EKONOMI 300 EL500K LEMON'],
# 				't13': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 LEMON FRESH'],
# 				't14': ['ROTI BANTAL PANJANG', 'SELE BUNGKUS'],
# 				't15': ['GULA PASIR 2 KG', 'BIMOLI SPESIAL REF 2 LITER'],
# 				't16': ['LIF. SOAP 80 NATUREPUR', 'LIF. SOAP 85 LEMON FRESH', 'MAMY POKO M72'],
# 				't17': ['EKONOMI 300 E500K BAG', 'EKONOMI 300 EL500K LEMON'],
# 				't18': ['GULA PASIR 2 KG', 'BIMOLI SPESIAL REF 2 LITER', 'SHINZUI SOAP 100 KENSHO'],
# 				't19': ['ROTI BANTAL PANJANG', 'SELE BUNGKUS', 'ROKOK 2 3 4'],
# 				't20': ['GULA PASIR 2 KG', 'BIMOLI SPESIAL REF 2 LITER', 'DAIA 900 LEMON'],
# 			}

test_data = {
				't1': ['bread', 'milk'],
				't2': ['bread', 'diaper', 'beer', 'eggs'],
				't3': ['milk', 'diaper', 'beer', 'coke'],
				't4': ['bread', 'milk', 'diaper', 'beer'],
				't5': ['bread', 'milk', 'diaper', 'coke'],
			}

all_item = []
frequent_item_set = {}
apriori_rules = {}
min_transaction = 2

def clean_double_item(input_list):
	temp_list = []
	for item in input_list:
		if item not in temp_list:
			temp_list.append(item)

	return temp_list

# sensus dulu semua item
for item_set in test_data:
	for item in test_data[item_set]:
		if item not in all_item:
			all_item.append(item)

# loop_1
temp_rules = {}
for item in all_item:
	count_item = 0
	for item_set in test_data:
		if item in test_data[item_set]:
			count_item = count_item + 1
	temp_rules.update({item:{'count':count_item, 'item_set':[item]}})

frequent_item_set.update({'loop_1': temp_rules})

# filtering rules
temp_selected_rules = {}
for item in frequent_item_set['loop_1']:
	if frequent_item_set['loop_1'][item]['count'] >= min_transaction:
		temp_selected_rules.update({item:frequent_item_set['loop_1'][item]})

i = 2
while temp_selected_rules != {}:
	print i, '. ===========================> '
	print temp_selected_rules
	print '\n'

	# buat kombinasi baru
	temp_selected_rules_2 = temp_selected_rules
	combined_rules = {}
	for rules in temp_selected_rules:
		for rules_2 in temp_selected_rules_2:
			temp_comb_item = clean_double_item(temp_selected_rules[rules]['item_set'] + temp_selected_rules_2[rules_2]['item_set'])
			if len(temp_comb_item) > i - 1:
				combined_rules.update({'_'.join(temp_comb_item):{'count':0, 'item_set':temp_comb_item }})

	# for rules in combined_rules:
	# 	print combined_rules[rules]

	# loop_2
	temp_rules = {}
	for item in combined_rules:
		count_item = 0
		temp_comb_item_set = combined_rules[item]['item_set']
		for item_set in test_data:
			in_transact = []
			for comb_item in temp_comb_item_set:
				if comb_item in test_data[item_set]:
					in_transact.append( True )
				else:
					in_transact.append( False )
			
			conds = True
			for cond in in_transact:
				conds = conds and cond
			
			if conds:			
				count_item = count_item + 1
			
		# print item, ":", count_item
		temp_rules.update({item:{'count':count_item, 'item_set':temp_comb_item_set}})

	idx = str(i)
	frequent_item_set.update({'loop_'+idx: temp_rules})
	# print frequent_item_set['loop_'+idx]

	# filtering rules
	temp_selected_rules = {}
	for item in frequent_item_set['loop_'+idx]:
		if frequent_item_set['loop_'+idx][item]['count'] >= min_transaction:
			temp_selected_rules.update({item:frequent_item_set['loop_'+idx][item]})

	i = i + 1

# generate rules
for item_set in frequent_item_set:
	if item_set != 'loop_1':
		for item in frequent_item_set[item_set]:
			temp_item = frequent_item_set[item_set][item]
			if temp_item['count'] >= min_transaction:
				item_len = len(temp_item['item_set'])
				print temp_item['item_set']
				print temp_item['item_set'][0:(-1 + (item_len))], ' ===> ',temp_item['item_set'][(item_len-1)]

				temp_rules = {'count':temp_item['count'], 'antecendent':temp_item['item_set'][0:(-1 + (item_len))], 'consequent':temp_item['item_set'][(item_len-1)], 'support':0.0, 'confidence':0.0, 'support_confidence':0.0}
				apriori_rules.update({'_'.join(temp_item['item_set']):temp_rules})
	print "\n"

# menghitung nilai apriori
for rules in apriori_rules:
	# menghitung support
	apriori_rules[rules]['support'] = apriori_rules[rules]['count'] / (len(test_data) * 1.0)
	
	# menghitung confidence
	for item_set in frequent_item_set:
		try:
			apriori_rules[rules]['confidence'] = apriori_rules[rules]['count'] / (frequent_item_set[item_set]['_'.join(apriori_rules[rules]['antecendent'])]['count'] * 1.0)
		except:
			continue

	# menghitung support confidence
	apriori_rules[rules]['support_confidence'] = apriori_rules[rules]['support'] *  apriori_rules[rules]['confidence']

# END OF APRIORI ALGORITHM
for rules in apriori_rules:
	print rules, '. ===========================> '
	print apriori_rules[rules]
	print