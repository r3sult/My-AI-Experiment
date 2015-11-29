
from multiprocessing import Process, Queue
import time

test_data = {}
all_item = []
frequent_item_set = {}
apriori_rules = {}
min_transaction = 0
min_confidence = 0.0

def clean_double_item(input_list):
	temp_list = []
	for item in input_list:
		if item not in temp_list:
			temp_list.append(item)
	return temp_list

# membaca file yang akan dilakukan pemrosesan apriori
file_data = ['diaper', 'groceries', 'groceries-1', 'groceries-2', 'groceries-3', 'groceries-4', 'groceries-5', 'retail_sample']
files = open('data/'+file_data[2]+'.txt', 'r')

for line in files:
    if line.find('@min_transaction') == 0:
        min_transaction = int(line.replace('@min_transaction','').strip())
        break

files.seek(0)
for line in files:
    if line.find('@min_confidence') == 0:
        min_confidence = float(line.replace('@min_confidence','').strip())
        break

files.seek(0)
process_data = False
i = 1
for line in files:
    if line.find('@data') == 0:
        process_data = True
        continue

    if line.find('@end_data') == 0:
        break

    if process_data:
        temp_training_data = line.split(',')
        temp_training = {}

        temp_data = []
        for train_data in temp_training_data:
        	temp_data.append(train_data.replace('\n', ''))

        test_data.update({'t'+str(i):temp_data})
        i = i + 1

# print "\n============= TEST DATA ==================="
# for dat in test_data:
#     print test_data[dat]

files.close()

# print test_data
print min_transaction
print min_confidence

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

print "====> step 1"
i = 2
while temp_selected_rules != {}:
	temp_selected_rules_2 = temp_selected_rules
	combined_rules = {}
	for rules in temp_selected_rules:
		time.sleep(0.0001)
		for rules_2 in temp_selected_rules_2:
			time.sleep(0.001)
			temp_comb_item = clean_double_item(temp_selected_rules[rules]['item_set'] + temp_selected_rules_2[rules_2]['item_set'])
			print temp_comb_item
			if len(temp_comb_item) > i - 1:
				combined_rules.update({'_'.join(temp_comb_item):{'count':0, 'item_set':temp_comb_item }})


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
		temp_rules.update({item:{'count':count_item, 'item_set':temp_comb_item_set}})

	idx = str(i)
	frequent_item_set.update({'loop_'+idx: temp_rules})
	
	# filtering rules
	temp_selected_rules = {}
	for item in frequent_item_set['loop_'+idx]:
		if frequent_item_set['loop_'+idx][item]['count'] >= min_transaction:
			temp_selected_rules.update({item:frequent_item_set['loop_'+idx][item]})

	
	i = i + 1

print "====> step 2"
# generate rules
for item_set in frequent_item_set:
	if item_set != 'loop_1':
		for item in frequent_item_set[item_set]:
			temp_item = frequent_item_set[item_set][item]
			if temp_item['count'] >= min_transaction:
				item_len = len(temp_item['item_set'])
				temp_rules = {'count':temp_item['count'], 'antecendent':temp_item['item_set'][0:(-1 + (item_len))], 'consequent':temp_item['item_set'][(item_len-1)], 'support':0.0, 'confidence':0.0, 'support_confidence':0.0}
				apriori_rules.update({'_'.join(temp_item['item_set']):temp_rules})

print "====> step 3"
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

print "\n"
# END OF APRIORI ALGORITHM
for rules in apriori_rules:
	print rules, '. ===========================> '
	print apriori_rules[rules]
	print
