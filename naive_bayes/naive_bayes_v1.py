# contoh data training
classifier = 'buy_computer'

criteria_data = {
                'age': ['lte30', '31to40', 'gt40'],
                'income' : ['high', 'medium', 'low'],
                'student' : ['no', 'yes'],
                'credit_ratings': ['fair', 'excellent'],
                'buy_computer': ['no', 'yes']
            }

probability_data = {
                    'yes' : {
                                'value': 0.0,
                                'length': 0,
                                'p_x': 0.0,
                                'p_ci_x': 0.0,
                                'age' : {
                                    'lte30':0.0,
                                    '31to40':0.0,
                                    'gt40':0.0,
                                },
                                'student': {
                                    'yes':0.0,
                                    'no':0.0
                                },
                                'income' : {
                                    'high':0.0,
                                    'medium':0.0,
                                    'low':0.0,
                                },
                                'credit_ratings' : {
                                    'fair':0.0,
                                    'excellent':0.0,
                                },
                            }, 
                    'no' : {
                                'value': 0.0,
                                'length': 0,
                                'p_x': 0.0,
                                'p_ci_x': 0.0,
                                'age' : {
                                    'lte30':0.0,
                                    '31to40':0.0,
                                    'gt40':0.0,
                                },
                                'student': {
                                    'yes':0.0,
                                    'no':0.0
                                },
                                'income' : {
                                    'high':0.0,
                                    'medium':0.0,
                                    'low':0.0,
                                },
                                'credit_ratings' : {
                                    'fair':0.0,
                                    'excellent':0.0,
                                },
                            },
                }

training_data = [
                    {'age': 'lte30', 'income':'high', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'no'},
                    {'age': 'lte30', 'income':'high', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'no'},
                    {'age': '31to40', 'income':'high', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'low', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'low', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'no'},
                    {'age': '31to40', 'income':'low', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': 'lte30', 'income':'medium', 'student':'no', 'credit_ratings':'fair', 'buy_computer':'no'},
                    {'age': 'lte30', 'income':'low', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'lte30', 'income':'medium', 'student':'yes', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': '31to40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'yes'},
                    {'age': '31to40', 'income':'high', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':'yes'},
                    {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':'no'},
                ]

test_data = [
                {'age': 'lte30', 'income':'medium', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':''},
                {'age': '31to40', 'income':'high', 'student':'yes', 'credit_ratings':'fair', 'buy_computer':''},
                {'age': 'gt40', 'income':'medium', 'student':'no', 'credit_ratings':'excellent', 'buy_computer':''},
            
            ]

def naive_bayes(item):
    len_data = len(training_data)

    # menghitung P(Ci)
    for classy in criteria_data[classifier]:
        temp = 0.0
        for data in training_data:
            if data['buy_computer'] == classy:
                temp = temp + 1

        probability_data[classy]['value'] = temp / len_data
        probability_data[classy]['length'] = temp

    # print probability_data['yes']['value'] 
    # print probability_data['no']['value'] 
    
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

# +======= MAIN PROCESS ==========
for i in test_data:
    naive_bayes(i)