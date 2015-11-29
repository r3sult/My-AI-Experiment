test_data = {
				't1':['mango', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
				't2':['doll', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
				't3':['mango', 'apple', 'knife', 'eggs'],
				't4':['mango', 'umbrella', 'corn', 'knife', 'yoyo'],
				't5':['corn', 'onion', 'onion', 'knife', 'eggs', 'ice_cream'],
			}

all_item = []
frequent_item_set = {}
apriori_rules = {}
min_transaction = 3

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

# print all_item

# loop_1
temp_rules = {}
for item in all_item:
	count_item = 0
	for item_set in test_data:
		if item in test_data[item_set]:
			count_item = count_item + 1
	temp_rules.update({item:{'count':count_item, 'item_set':[item]}})

frequent_item_set.update({'loop_1': temp_rules})
# print frequent_item_set['loop_1']

# filtering rules
temp_selected_rules = {}
for item in frequent_item_set['loop_1']:
	if frequent_item_set['loop_1'][item]['count'] >= min_transaction:
		temp_selected_rules.update({item:frequent_item_set['loop_1'][item]})

# print temp_selected_rules

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
			if temp_item['count'] >= 3:
				item_len = len(temp_item['item_set'])
				print temp_item['item_set']
				print temp_item['item_set'][0:(-1 + (item_len))], ' ===> ',temp_item['item_set'][(item_len-1)]

				temp_rules = {'count':temp_item['count'], 'antecendent':temp_item['item_set'][0:(-1 + (item_len))], 'consequent':temp_item['item_set'][(item_len-1)], 'support':0.0, 'confidence':0.0, 'support_confidence':0.0}
				apriori_rules.update({'_'.join(temp_item['item_set']):temp_rules})
	print "\n"

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

# menghitung support * confidence

for rules in apriori_rules:
	print rules, '. ===========================> '
	print apriori_rules[rules]
	# print '\n'
