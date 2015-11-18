import MySQLdb
import re

# konfigurasi program
conn = MySQLdb.connect("localhost","root","root","jokowi_sentiment")
inflection_suffix_list = "(.*)lah$|(.*)kah$|(.*)ku$|(.*)mu$|(.*)nya$"
word_particle_list = "(.*)lah$|(.*)kah$|(.*)tah$|(.*)pun$"
possesive_pronoun_list = "(.*)ku$|(.*)mu$|(.*)nya$"
derivation_suffix_list = "(.*)an$|(.*)kan$|(.*)i$"
derivation_prefix_list = "di(.*)$|ke(.*)$|se(.*)$|me(.*)$|be(.*)$|pe(.*)$|te(.*)$"
derivation_prefix_format_me_1 = "ny[a|i|u|e|o](.*)$"
derivation_prefix_format_me_2 = "ng[a-z](.*)$"
derivation_prefix_format_me_3 = "m[a-z](.*)$"
derivation_prefix_format_be_1 = "r[^aeiou](.*)$"

# contoh kata yang akan distem
test_words = ['sepakan', 'sepekan', 'kelistrikan', 'komputer', 'kamulah', 'topimu', 'bajuku', 'mobilnya', 'listrik', 
				'awan', 'bersatu', 'jayalah', 'selalu', 'bajukulah', 'dimanapun', 'kesehatannya', 'uangmu', 'kesalahannyalah', 
				'menyelesaikannya', 'menggalakkan', 'persawahan' ,'menyalahi', 'mempergunakan', 'memberdayakan', 'tarian', 'seimbang', 'bekantan', 'beo', 'membeo']

def stringify(bag_of_words):
	res = ""
	i = 1
	for words in bag_of_words:
		temp = '"' +words+ '"'
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

	print temp_words
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

	print "after word particle list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari word particles
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

	print "after possesive pronoun list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari inflection suffixes
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+inflection_suffix_list, words, re.M|re.I)
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

	print "after inflection suffix list:"
	print unstemmed_words
	print ""

	# membersihkan unstemmed_words dari derivation suffixes
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+derivation_suffix_list, words, re.M|re.I)
		if (temp_words is not None):
			for re_words in temp_words.groups():
				if re_words != None:
					temp_word_list.append(re_words)
		else:
			temp_word_list.append(words)

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "after derivation suffix list:"
	print unstemmed_words
	print ""

	# restore list yang sudah distem derivation suffixes
	temp_unstemmed_words = []
	for words in prev_unstemmed_words:
		for words2 in unstemmed_words: 
			x = re.search(r''+words2+'(.*)', words)
			if x != None:
				temp_unstemmed_words.append(x.string)

	print temp_unstemmed_words
	
	# membersihkan unstemmed words dari derivation prefix
	unstemmed_words = temp_unstemmed_words
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+derivation_prefix_list, words, re.M|re.I)
		if (temp_words is not None):
			temp_clean_words = ""
			for re_words in temp_words.groups():
				if re_words != None:
					temp_clean_words = re_words

			clean_words = ""
			re_clean_words = re.match(r''+derivation_prefix_format_me_1, temp_clean_words)
			if (re_clean_words is not None):
				clean_words = temp_clean_words.replace('ny', 's')
			else:
				clean_words = temp_clean_words

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
			re_clean_words = re.match(r''+derivation_prefix_format_be_1, temp_clean_words)
			if (re_clean_words is not None):
				clean_words = temp_clean_words.replace('r', '')
			else:
				clean_words = temp_clean_words

			temp_word_list.append(clean_words)
		else:
			temp_word_list.append(words)

	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "after derivation prefix list:"
	print unstemmed_words
	print ""

	
	# membersihkan unstemmed_words dari derivation suffixes
	temp_word_list = []
	for words in unstemmed_words:
		temp_words = re.match(r''+derivation_suffix_list, words, re.M|re.I)
		if (temp_words is not None):
			for re_words in temp_words.groups():
				if re_words != None:
					temp_word_list.append(re_words)
		else:
			temp_word_list.append(words)

	prev_unstemmed_words = unstemmed_words
	unstemmed_words = temp_word_list
	temp_root_words = check_root_words(unstemmed_words)
	stemmed_words = stemmed_words + temp_root_words
	unstemmed_words = get_unstemmed_words(unstemmed_words, stemmed_words)

	print "after derivation suffix list:"
	print unstemmed_words
	print ""

	return stemmed_words

# main process
result = stemming_nazief_adriani(test_words)
print result