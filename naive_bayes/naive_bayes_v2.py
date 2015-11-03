# contoh test data
# test_data = [
#                 {'age': 'lte30', 'income':'medium', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':''},
#                 {'age': '31to40', 'income':'high', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':''},
#                 {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':''},
#             ]

classifier = ""
criteria_data = {}
probability_data = {}
training_data = []
headers = []
test_data = []

def init_bayesian():
    len_data = len(training_data)

    # menghitung P(Ci)
    for classy in criteria_data[classifier]:
        temp = 0.0
        for data in training_data:
            if data[classifier] == classy:
                temp = temp + 1

        probability_data[classy]['value'] = temp / len_data
        probability_data[classy]['length'] = temp

def naive_bayes(item):
    # menghitung P(X | Ci)
    for classy in criteria_data[classifier]:
        for key in item:
            if key != classifier:
                # print item[key]
                temp = 0.0
                for data in training_data:
                    if data[key] == item[key] and data[classifier] == classy:
                        temp = temp + 1
                
                # print temp
                probability_data[classy][key][item[key]] = temp / probability_data[classy]['length']

    # menghitung P(X)
    for classy in criteria_data[classifier]:
        temp = 1.0
        for key in item:
            if key != classifier:
                temp = temp * probability_data[classy][key][item[key]]

        probability_data[classy]['p_x'] = temp

    # menghitung P(Ci | X)
    result = []
    for classy in criteria_data[classifier]:
        probability_data[classy]['p_ci_x'] = probability_data[classy]['p_x'] * probability_data[classy]['value']
        result.append(probability_data[classy]['p_ci_x'])

    final_result = max(result)

    for classy in criteria_data[classifier]:
        if final_result == probability_data[classy]['p_ci_x']:
            item[classifier] = classy 

    # print probability_data
    print "\n====== HASIL AKHIR ======"
    print item

# ======== READ FILE PROCESS ========

# membaca file yang akan dilakukan pemrosesan clustering
files = open('data/zoo.txt', 'r')

for line in files:
    if line.find('@classifier') == 0:
        classifier = line.replace('@classifier','').strip()
        break

files.seek(0)
for line in files:
    if line.find('@attribute') == 0:
        attr_list = line.replace('@attribute','').strip()
        for attrib in attr_list.split(','):
            criteria_data.update({attrib:[]})
        break

files.seek(0)
process_criteria_data = False
for line in files:
    if line.find('@criteria') == 0:
        process_criteria_data = True
        continue

    if line.find('@end_criteria') == 0:
        break

    if process_criteria_data:
        temp_criteria_data = line.split(':')

        for item in criteria_data:
            if item == temp_criteria_data[0]:
                temp_criteria_list = temp_criteria_data[1].split(',')
                i = 0
                for criteria_list in temp_criteria_list:
                    temp_criteria_list[i] = criteria_list.replace('\n', '')

                    if item == classifier:
                        probability_data.update({ criteria_list.replace('\n', ''):{ 'value': 0.0, 'length': 0, 'p_x': 0.0, 'p_ci_x': 0.0 } })
                    i = i + 1 

                criteria_data[item] = temp_criteria_list



for probe in probability_data:
    for criteria_list in criteria_data:
        if criteria_list != classifier:
            temp_criteria = {}
            for criteria_item in criteria_data[criteria_list]:
                    temp_criteria.update({ criteria_item : 0.0 })

            probability_data[probe].update({criteria_list: temp_criteria})
        else:
            continue

print probability_data

files.seek(0)
for line in files:
    if line.find('@header') == 0:
        header_list = line.replace('@header', '').strip()
        for head in header_list.split(','):
            headers.append(head)
        break

files.seek(0)
process_data = False
for line in files:
    if line.find('@data') == 0:
        process_data = True
        continue

    if line.find('@end_data') == 0:
        break

    if process_data:
        temp_training_data = line.split(',')
        temp_training = {}
        
        i = 0
        for head in headers:
            temp_training[head] = temp_training_data[i].replace('\n', '')
            i = i + 1

        training_data.append(temp_training)

files.seek(0)
process_data = False
for line in files:
    if line.find('@test_data') == 0:
        process_data = True
        continue

    if line.find('@end_test_data') == 0:
        break

    if process_data:
        # print line
        temp_training_data = line.split(',')
        temp_training = {}
        
        i = 0
        for head in headers:
            temp_training[head] = temp_training_data[i].replace('\n', '')
            i = i + 1

        test_data.append(temp_training)

print "\n============= TRAINING DATA ==============="
for dat in training_data:
    print dat

print "\n============= TEST DATA ==================="
for dat in test_data:
    print dat

files.close()

# ======== MAIN PROCESS ==========
init_bayesian()
for i in test_data:
    naive_bayes(i)