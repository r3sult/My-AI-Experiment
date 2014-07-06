# contoh data training
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

def get_x_pci(x, xval, ci, cival, buy_computer_yn):
    temp_count_xpci = 0
    for data in training_data:
        if data[x] == xval and data[ci] == cival:
            temp_count_xpci = temp_count_xpci + 1
    return (temp_count_xpci * 1.0) / buy_computer_yn
    
# menghitung banyaknya data sesuai buy_computer
buy_computer_yes = 0
buy_computer_no = 0
len_training_data = len(training_data)

for data in training_data:
    if data['buy_computer'] =='no':
        buy_computer_no = buy_computer_no + 1
    elif data['buy_computer'] == 'yes':
        buy_computer_yes = buy_computer_yes + 1

print "buy computer yes: ", buy_computer_yes
print "buy computer no: ", buy_computer_no
print "total data: ", len_training_data

# menentukan nilai P(Ci)
p_ci_bc_y = (buy_computer_yes * 1.0) / len_training_data
p_ci_bc_n = (buy_computer_no * 1.0) / len_training_data

print p_ci_bc_y
print p_ci_bc_n
print

# hitung P(X|Ci) untuk setiap kelas
print "P(X|Ci) untuk atribut age:"
p_lte30_bc_y = get_x_pci('age', 'lte30', 'buy_computer', 'yes', buy_computer_yes)
print p_lte30_bc_y
p_lte30_bc_n = get_x_pci('age', 'lte30', 'buy_computer', 'no', buy_computer_no)
print p_lte30_bc_n
p_31to40_bc_y = get_x_pci('age', '31to40', 'buy_computer', 'yes', buy_computer_yes)
print p_31to40_bc_y
p_31to40_bc_n = get_x_pci('age', '31to40', 'buy_computer', 'no', buy_computer_no)
print p_31to40_bc_n
p_gt40_bc_y = get_x_pci('age', 'gt40', 'buy_computer', 'yes', buy_computer_yes)
print p_gt40_bc_y
p_gt40_bc_n = get_x_pci('age', 'gt40', 'buy_computer', 'no', buy_computer_no)
print p_gt40_bc_n
print

print "P(X|Ci) untuk atribut income:"
p_ich_bc_y = get_x_pci('income', 'high', 'buy_computer', 'yes', buy_computer_yes)
print p_ich_bc_y
p_ich_bc_n = get_x_pci('income', 'high', 'buy_computer', 'no', buy_computer_no)
print p_ich_bc_y
p_icm_bc_y = get_x_pci('income', 'medium', 'buy_computer', 'yes', buy_computer_yes)
print p_icm_bc_y
p_icm_bc_n = get_x_pci('income', 'medium', 'buy_computer', 'no', buy_computer_no)
print p_icm_bc_y
p_icl_bc_y = get_x_pci('income', 'low', 'buy_computer', 'yes', buy_computer_yes)
print p_icl_bc_y
p_icl_bc_n = get_x_pci('income', 'low', 'buy_computer', 'no', buy_computer_no)
print p_icl_bc_y
print

print "P(X|Ci) untuk atribut student:"
p_stdy_bc_y = get_x_pci('student', 'yes', 'buy_computer', 'yes', buy_computer_yes)
print p_stdy_bc_y
p_stdy_bc_n = get_x_pci('student', 'yes', 'buy_computer', 'no', buy_computer_no)
print p_stdy_bc_n
p_stdn_bc_y = get_x_pci('student', 'no', 'buy_computer', 'yes', buy_computer_yes)
print p_stdn_bc_y
p_stdn_bc_n = get_x_pci('student', 'no', 'buy_computer', 'no', buy_computer_no)
print p_stdn_bc_n
print


print "P(X|Ci) untuk atribut credit rating:"
p_cre_bc_y = get_x_pci('credit_ratings', 'excellent', 'buy_computer', 'yes', buy_computer_yes)
print p_cre_bc_y
p_cre_bc_n = get_x_pci('credit_ratings', 'excellent', 'buy_computer', 'no', buy_computer_no)
print p_cre_bc_n
p_crf_bc_y = get_x_pci('credit_ratings', 'fair', 'buy_computer', 'yes', buy_computer_yes)
print p_crf_bc_y
p_crf_bc_n = get_x_pci('credit_ratings', 'fair', 'buy_computer', 'no', buy_computer_no)
print p_crf_bc_n
print

# dicari klasifikasi X = (age <= 30 , income = medium, student = yes, credit_rating = fair)
case1_y = p_lte30_bc_y * p_icm_bc_y * p_stdy_bc_y * p_crf_bc_y 
case1_n = p_lte30_bc_n * p_icm_bc_n * p_stdy_bc_n * p_crf_bc_n

print case1_y, " --- ", case1_n

# dicari P(X|Ci)*P(Ci)
print case1_y *  p_ci_bc_y
print case1_n *  p_ci_bc_n
