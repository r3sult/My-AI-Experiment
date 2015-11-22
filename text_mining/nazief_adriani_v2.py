import MySQLdb
import re

# konfigurasi program
inflection_suffix_list = "(.*)lah$|(.*)kah$|(.*)ku$|(.*)mu$|(.*)nya$"
word_particle_list = "(.*)lah$|(.*)kah$|(.*)tah$|(.*)pun$"
possesive_pronoun_list = "(.*)ku$|(.*)mu$|(.*)nya$"
derivation_suffix_list = ["(.*)kan$", "(.*)an$",  "(.*)i$"]
derivation_prefix_list = "di(.*)$|ke(.*)$|se(.*)$|me(.*)$|be(.*)$|pe(.*)$|te(.*)$"
derivation_prefix_format_me_1 = "ny[a|i|u|e|o](.*)$"
derivation_prefix_format_me_2 = "ng[a-z](.*)$"
derivation_prefix_format_me_3 = "m[^aeiou](.*)$"
derivation_prefix_format_me_4 = "n[a-z](.*)$"
derivation_prefix_format_be_1 = "r[^aeiou](.*)$"
derivation_prefix_format_be_2 = "l[aeiou](.*)$"
derivation_prefix_format_pe_1 = "t[^aeiou](.*)$"

# contoh kata yang akan distem
# test_words = ['sepakan', 'sepekan', 'kelistrikan', 'komputer', 'kamulah', 'topimu', 'bajuku', 'mobilnya',
# 				'awan', 'bersatu', 'jayalah', 'selalu', 'bajukulah', 'dimanapun', 'kesehatannya', 'uangmu', 'kesalahannyalah', 
# 				'menyelesaikannya', 'menggalakkan', 'persawahan' ,'menyalahi', 'mempergunakan', 'memberdayakan', 'tarian', 
# 				'seimbang', 'bekantan', 'beo', 'membeo', 'kekeliruan', 'tercatat', 'tercantum', 'mengharapkan', 'balasan', 'tersedia',
# 				'persediaannya', 'ketersediaannya' ,'berkesempatan', 'menaruh', 'menanam', 'menanak', 'menukarkan', 'pewangi', 'belajar', 'belikan',
# 				'pelamar', 'pemakan', 'penanti', 'penyiram', 'penyabar', 'pemikir', 'pemotong', 'pemberi', 'pembunuh', 'pemberian', 'pembunuhan',
# 				'penjahit', 'pendidik', 'pencuci', 'penzina', 'penikam', 'perkantoran', 'pergelaran', 'perhitungan', 'keatas', 'kelakuan', 
# 				'mewarna', 'merawat', 'menaik', 'memasak', 'melempar', 'menyapu', 'menyatu', 'memberi', 'membesuk', 'mengoplos', 'mengasuh', 'mengubah',
# 				'mengekor', 'menginap', 'seekor', 'searah', 'senasib', 'sebungkus', 'melemparkanmu', 'memberikannya', 'arti', 'kenyamanan', 'bernyali',
# 				'diminum', 'ditahan', 'dipuja']

# test_words = ['sebungkus', 'senasib', 'searah', 'seekor']
# test_words = ['menginap', 'mengasuh', 'mengubah', 'mengekor', 'mengoplos', 'memberi', 'membesuk', 'membusuk', 'menyapu', 'menyatu', 'menanam', 'menukar', 'melempar', 'memasak', 'menaik', 'merawat', 'mewarna']
test_words = ['kebawa', 'keatas', 'perhitungan', 'pergelaran', 'perkantoran', 'penukar', 'penikam', 'penjahit', 'pendidik', 'pencuci', 'penzina', 'pemberi', 'pembunuh', 'penyiram', 'penyabar', 'pelamar', 'pemakan', 'penanti', 'pewangi']

def stringify(bag_of_words):
	res = ""
	i = 1
	for words in bag_of_words:
		temp_words = ''.join(words)
		temp = '"' +temp_words+ '"'
		res = res + temp

		if len(bag_of_words) == i:
			continue
		else:
			res = res + ", " 
		i = i + 1

	return res

def to_list_words (query_result):
	temp_words = []
	for rows in query_result:
		temp_words.append(rows[0])

	return temp_words

def get_unstemmed_words(bags, stemmed):
	temp_words = []

	for words in bags:
		if words in stemmed:
			continue
		else:
			temp_words.append(words)

	return temp_words

def check_root_words(bag_of_words):
	temp_words = stringify(bag_of_words)

	# print temp_words
	conn = MySQLdb.connect("localhost","root","root","jokowi_sentiment")
	cursor = conn.cursor()
	cursor.execute('SELECT  katadasar FROM tb_katadasar where katadasar in ('+temp_words+')')
	temp_result = cursor.fetchall()

	result = to_list_words(temp_result)
	conn.close()
	return result

# proses stemming
def stemming_nazief_adriani(bag_of_words):
	stemmed_words = []
	
	# melewat kata - kata yang sudah menjadi root word.
	unstemmed_words = bag_of_words
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)
	
	# membersihkan unstemmed_words dari word particles
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+word_particle_list, words, re.M|re.I)
		if (temp_words is not None):
			for re_words in temp_words.groups():
				if re_words != None:
					temp_word_list.append(re_words)
		else:
			temp_word_list.append(words)

	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after word particle list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari posessive pronouns
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+possesive_pronoun_list, words, re.M|re.I)
		if (temp_words is not None):
			for re_words in temp_words.groups():
				if re_words != None:
					temp_word_list.append(re_words)
		else:
			temp_word_list.append(words)
			
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after possesive pronoun list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari inflection suffixes
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+inflection_suffix_list, words, re.M|re.I)
		if (temp_words is not None):
			temp_re_words = ""
			for re_words in temp_words.groups():
				if re_words != None:
					temp_re_words = re_words
			temp_word_list.append(temp_re_words)
		else:
			temp_word_list.append(words)

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after inflection suffix list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari derivation suffixes
	temp_word_list = []
	for words in unstemmed_words:
		found = 0
		for re_pattern in derivation_suffix_list:
			temp_words = re.match(r''+re_pattern, words, re.M|re.I)
			if (temp_words is not None):
				temp_re_words = ""
				for re_words in temp_words.groups():
					if re_words != None:
						temp_re_words = list(re_words)

				temp_re_words = ''.join(temp_re_words)
				temp_re_root_words = check_root_words([temp_re_words])
				
				if (len(temp_re_root_words) == 0):
					continue
				else:
					temp_word_list.append(temp_re_root_words[0])
					found = found + 1
					break
		
		if found == 0:
			temp_word_list.append(words)

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after derivation suffix list:"
	print unstemmed_words
	print ""

	# restore list yang sudah distem derivation suffixes
	temp_unstemmed_words = []
	for words in prev_unstemmed_words:
		for words2 in unstemmed_words: 
			x = re.search(r''+words2+'(.*)', words)
			if x != None:
				temp_unstemmed_words.append(x.string)

	print "\n==> after restoration:"
	print temp_unstemmed_words
	print ""
	
	## membersihkan unstemmed words dari derivation prefix
	unstemmed_words = temp_unstemmed_words
	temp_word_list = []
	for words in unstemmed_words:
		# potong kata tersebut
		# check apakah ada di kamus
		# kalau ada simpan sebagai stemmed
		# kalau ga ada simpan sebagai bahan untuk recoding
		temp_words = re.match(r''+derivation_prefix_list, words, re.M|re.I)
		if (temp_words is not None):
			temp_clean_words = ""
			for re_words in temp_words.groups():
				if re_words != None:
					temp_clean_words = re_words
			temp_word_list.append(temp_clean_words)
		else:
			temp_word_list.append(words)

	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after derivation prefix list:"
	print unstemmed_words
	print ""


	# proses recoding kata - kata
	temp_word_list = []
	for words in unstemmed_words:
		
		temp_clean_words = words
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_me_1, words)
		if (re_clean_words is not None):
			clean_words = temp_clean_words.replace('ny', 's')
		else:
			clean_words = words
		
		temp_clean_words = clean_words	
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_me_2, temp_clean_words)
		if (re_clean_words is not None):
			clean_words = temp_clean_words.replace('ng', '')
		else:
			clean_words = temp_clean_words
		
		temp_clean_words = clean_words	
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_me_3, temp_clean_words)
		if (re_clean_words is not None):
			clean_words = temp_clean_words.replace('m', '')
		else:
			clean_words = temp_clean_words

		temp_clean_words = clean_words	
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_me_4, temp_clean_words)
		if (re_clean_words is not None):
			temp_clean_words = list(temp_clean_words)
			temp_clean_words[0] = 't'
			clean_words = ''.join(temp_clean_words)
		else:
			clean_words = temp_clean_words

		temp_clean_words = clean_words	
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_be_1, temp_clean_words)
		if (re_clean_words is not None):
			temp_clean_words = list(temp_clean_words)
			temp_clean_words[0] = ''
			clean_words = ''.join(temp_clean_words)
		else:
			clean_words = temp_clean_words

		temp_clean_words = clean_words	
		clean_words = ""
		re_clean_words = re.match(r''+derivation_prefix_format_pe_1, temp_clean_words)
		if (re_clean_words is not None):
			temp_clean_words = list(temp_clean_words)
			temp_clean_words[0] = ''
			clean_words = ''.join(temp_clean_words)
		else:
			clean_words = temp_clean_words

		# temp_clean_words = clean_words	
		# clean_words = ""
		# re_clean_words = re.match(r''+derivation_prefix_format_be_2, temp_clean_words)
		# if (re_clean_words is not None):
		# 	temp_clean_words = list(temp_clean_words)
		# 	temp_clean_words[0] = ''
		# 	clean_words = ''.join(temp_clean_words)
		# else:
		# 	clean_words = temp_clean_words
		
		temp_word_list.append(clean_words)	

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after recoding"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari derivation suffixes
	temp_word_list = []
	for words in unstemmed_words:
		found = 0
		for re_pattern in derivation_suffix_list:
			temp_words = re.match(r''+re_pattern, words, re.M|re.I)
			if (temp_words is not None):
				temp_re_words = ""
				for re_words in temp_words.groups():
					if re_words != None:
						temp_re_words = list(re_words)
						
				temp_re_words = ''.join(temp_re_words)
				temp_re_root_words = check_root_words([temp_re_words])
				
				if (len(temp_re_root_words) == 0):
					continue
				else:
					temp_word_list.append(temp_re_root_words[0])
					found = found + 1
					break
		
		if found == 0:
			temp_word_list.append(words)

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "==> after derivation suffix list:"
	print unstemmed_words
	print ""

	# restore list yang sudah distem derivation suffixes
	temp_unstemmed_words = []
	for words in prev_unstemmed_words:
		for words2 in unstemmed_words: 
			x = re.search(r''+words2+'(.*)', words)
			if x != None:
				temp_unstemmed_words.append(x.string)

	print "\n==> after restoration #2:"
	print temp_unstemmed_words
	print ""

	# ## membersihkan unstemmed words dari derivation prefix
	# unstemmed_words = temp_unstemmed_words
	# temp_word_list = []
	# for words in unstemmed_words:
	# 	# potong kata tersebut
	# 	# check apakah ada di kamus
	# 	# kalau ada simpan sebagai stemmed
	# 	# kalau ga ada simpan sebagai bahan untuk recoding
	# 	temp_words = re.match(r''+derivation_prefix_list, words, re.M|re.I)
	# 	if (temp_words is not None):
	# 		temp_clean_words = ""
	# 		for re_words in temp_words.groups():
	# 			if re_words != None:
	# 				temp_clean_words = re_words
	# 		temp_word_list.append(temp_clean_words)
	# 	else:
	# 		temp_word_list.append(words)

	# unstemmed_words = temp_word_list
	# temp_root_words = check_root_words(unstemmed_words)
	# stemmed_words = stemmed_words + temp_root_words
	# unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	# print "==> after derivation prefix list:"
	# print unstemmed_words
	# print ""


	# # proses recoding kata - kata
	# temp_word_list = []
	# for words in unstemmed_words:
		
	# 	temp_clean_words = words
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_me_1, words)
	# 	if (re_clean_words is not None):
	# 		clean_words = temp_clean_words.replace('ny', 's')
	# 	else:
	# 		clean_words = words
		
	# 	temp_clean_words = clean_words	
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_me_2, temp_clean_words)
	# 	if (re_clean_words is not None):
	# 		clean_words = temp_clean_words.replace('ng', '')
	# 	else:
	# 		clean_words = temp_clean_words
		
	# 	temp_clean_words = clean_words	
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_me_3, temp_clean_words)
	# 	if (re_clean_words is not None):
	# 		clean_words = temp_clean_words.replace('m', '')
	# 	else:
	# 		clean_words = temp_clean_words

	# 	temp_clean_words = clean_words	
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_me_4, temp_clean_words)
	# 	if (re_clean_words is not None):
	# 		temp_clean_words = list(temp_clean_words)
	# 		temp_clean_words[0] = 't'
	# 		clean_words = ''.join(temp_clean_words)
	# 	else:
	# 		clean_words = temp_clean_words

	# 	temp_clean_words = clean_words	
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_be_1, temp_clean_words)
	# 	if (re_clean_words is not None):
	# 		temp_clean_words = list(temp_clean_words)
	# 		temp_clean_words[0] = ''
	# 		clean_words = ''.join(temp_clean_words)
	# 	else:
	# 		clean_words = temp_clean_words

	# 	temp_clean_words = clean_words	
	# 	clean_words = ""
	# 	re_clean_words = re.match(r''+derivation_prefix_format_pe_1, temp_clean_words)
	# 	if (re_clean_words is not None):
	# 		temp_clean_words = list(temp_clean_words)
	# 		temp_clean_words[0] = ''
	# 		clean_words = ''.join(temp_clean_words)
	# 	else:
	# 		clean_words = temp_clean_words

	# 	# temp_clean_words = clean_words	
	# 	# clean_words = ""
	# 	# re_clean_words = re.match(r''+derivation_prefix_format_be_2, temp_clean_words)
	# 	# if (re_clean_words is not None):
	# 	# 	temp_clean_words = list(temp_clean_words)
	# 	# 	temp_clean_words[0] = ''
	# 	# 	clean_words = ''.join(temp_clean_words)
	# 	# else:
	# 	# 	clean_words = temp_clean_words
		
	# 	temp_word_list.append(clean_words)	

	# prev_unstemmed_words = unstemmed_words
	# unstemmed_words = temp_word_list
	# temp_root_words = check_root_words(unstemmed_words)
	# stemmed_words = stemmed_words + temp_root_words
	# unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	# print "==> after recoding"
	# print unstemmed_words
	# print ""

	# # membersihkan unstemmed_words dari derivation suffixes
	# temp_word_list = []
	# for words in unstemmed_words:
	# 	found = 0
	# 	for re_pattern in derivation_suffix_list:
	# 		temp_words = re.match(r''+re_pattern, words, re.M|re.I)
	# 		if (temp_words is not None):
	# 			temp_re_words = ""
	# 			for re_words in temp_words.groups():
	# 				if re_words != None:
	# 					temp_re_words = list(re_words)
						
	# 			temp_re_words = ''.join(temp_re_words)
	# 			temp_re_root_words = check_root_words([temp_re_words])
				
	# 			if (len(temp_re_root_words) == 0):
	# 				continue
	# 			else:
	# 				temp_word_list.append(temp_re_root_words[0])
	# 				found = found + 1
	# 				break
		
	# 	if found == 0:
	# 		temp_word_list.append(words)

	# prev_unstemmed_words = unstemmed_words
	# unstemmed_words = temp_word_list
	# temp_root_words = check_root_words(unstemmed_words)
	# stemmed_words = stemmed_words + temp_root_words
	# unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	# print "==> after derivation suffix list:"
	# print unstemmed_words
	# print ""

	# # restore list yang sudah distem derivation suffixes
	# temp_unstemmed_words = []
	# for words in prev_unstemmed_words:
	# 	for words2 in unstemmed_words: 
	# 		x = re.search(r''+words2+'(.*)', words)
	# 		if x != None:
	# 			temp_unstemmed_words.append(x.string)

	# print "\n==> after restoration:"
	# print temp_unstemmed_words
	# print ""

	return stemmed_words

# main process
result = stemming_nazief_adriani(test_words)
print "\n\n===> HASIL STEMMING:"
print len(test_words)
print len(result)
print result