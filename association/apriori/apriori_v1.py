test_data = {
				't1':['mango', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
				't2':['doll', 'onion', 'nintendo', 'knife', 'eggs', 'yoyo'],
				't3':['mango', 'apple', 'knife', 'eggs'],
				't4':['mango', 'umbrella', 'corn', 'knife', 'yoyo'],
				't5':['corn', 'onion', 'onion', 'knife', 'eggs', 'ice_cream'],
			}

all_item = []
frequent_item_set = {}

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

print all_item

# loop_1
temp_rules = {}
for item in all_item:
	count_item = 0
	for item_set in test_data:
		if item in test_data[item_set]:
			count_item = count_item + 1
	temp_rules.update({item:{'count':count_item, 'item_set':[item]}})

frequent_item_set.update({'loop_1': temp_rules})
print frequent_item_set['loop_1']

# filtering rules
temp_selected_rules = {}
for item in frequent_item_set['loop_1']:
	if frequent_item_set['loop_1'][item]['count'] >= min_transaction:
		temp_selected_rules.update({item:frequent_item_set['loop_1'][item]})

print temp_selected_rules

# buat kombinasi baru
temp_selected_rules_2 = temp_selected_rules
combined_rules = {}
for rules in temp_selected_rules:
	for rules_2 in temp_selected_rules_2:
		temp_comb_item = clean_double_item(temp_selected_rules[rules]['item_set'] + temp_selected_rules_2[rules_2]['item_set'])
		if len(temp_comb_item) > 1:
			combined_rules.update({'_'.join(temp_comb_item):{'count':0, 'item_set':temp_comb_item }})

for rules in combined_rules:
	print combined_rules[rules]

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
		
	print item, ":", count_item
	temp_rules.update({item:{'count':count_item, 'item_set':temp_comb_item_set}})

frequent_item_set.update({'loop_2': temp_rules})
print frequent_item_set['loop_2']

# filtering rules
temp_selected_rules = {}
for item in frequent_item_set['loop_2']:
	if frequent_item_set['loop_2'][item]['count'] >= min_transaction:
		temp_selected_rules.update({item:frequent_item_set['loop_2'][item]})

# buat kombinasi baru
temp_selected_rules_2 = temp_selected_rules
combined_rules = {}
for rules in temp_selected_rules:
	for rules_2 in temp_selected_rules_2:
		temp_comb_item = clean_double_item(temp_selected_rules[rules]['item_set'] + temp_selected_rules_2[rules_2]['item_set'])
		if len(temp_comb_item) > 2:
			combined_rules.update({'_'.join(temp_comb_item):{'count':0, 'item_set':temp_comb_item }})

for rules in combined_rules:
	print combined_rules[rules]

# loop_3
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
		
	print item, ":", count_item
	temp_rules.update({item:{'count':count_item, 'item_set':temp_comb_item_set}})

frequent_item_set.update({'loop_3': temp_rules})
# print frequent_item_set['loop_3']

# filtering rules
temp_selected_rules = {}
for item in frequent_item_set['loop_3']:
	if frequent_item_set['loop_3'][item]['count'] >= min_transaction:
		temp_selected_rules.update({item:frequent_item_set['loop_3'][item]})
		
# buat kombinasi baru
temp_selected_rules_2 = temp_selected_rules
combined_rules = {}
for rules in temp_selected_rules:
	for rules_2 in temp_selected_rules_2:
		temp_comb_item = clean_double_item(temp_selected_rules[rules]['item_set'] + temp_selected_rules_2[rules_2]['item_set'])
		if len(temp_comb_item) > 3:
			combined_rules.update({'_'.join(temp_comb_item):{'count':0, 'item_set':temp_comb_item }})

for rules in combined_rules:
	print combined_rules[rules]

# loop_4
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
		
	print item, ":", count_item
	temp_rules.update({item:{'count':count_item, 'item_set':temp_comb_item_set}})

frequent_item_set.update({'loop_4': temp_rules})
print frequent_item_set['loop_4']

# END OF APRIORI ALGORITM
for rules in frequent_item_set:
	print rules
	print frequent_item_set[rules]
	print