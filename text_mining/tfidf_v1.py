import math

#### CONTOH DATA
tfidf_data = { }
stopwords = []
text_data = [
				{
					'title':'STEMMING DOKUMEN TEKS BAHASA INDONESIA MENGGUNAKAN ALGORITMA PORTER', 
					'raw_text':"""Informasi merupakan hal yang
						sangat mudah didapatkan dan diakses. Tetapi
						terkadang informasi yang diperoleh tidak sesuai dengan apa yang diinginkan pengguna.
						Diperlukan sistem yang dapat membantu mencari informasi yang dibutuhkan secara efektif
						dan efisien. Sistem informasi ini sering kali disebut dengan istilah sistem temu kembali
						informasi (STKI). Pada STKI salah satu tahapan yang sangat penting adalah tahap
						Stemming. Tahapan ini merupakan tahapan mentransformasikan kata dalam sebuah kalimat
						atau dokumen ke kata dasarnya. Pada penelitian ini, akan dijelaskan proses Stemming pada
						kalimat bahasa indonesia dengan menggunakan algortitma porter untuk mendapat root word
						dari kata dalam dokumen teks. Tahapan yang ada pada algoritma porter diterjemahkan
						menjadi koding program PHP. Kamus kata dasar dan stoplist disimpan di MySql. Pada
						proses stemming dilakukan tidak kata perkata, akan tetapi langsung stemming pada
						dokumen. Sehingga proses stemming yang dilakukan lebih cepat dan efektif.""", 
					'processed_text':''
				},
				{
					'title':'HARD SUBJECT-BASED SEARCH ENGINE MENGGUNAKAN TF-IDF DAN JACCARDS COEFFICIENT',
					'raw_text':"""Paper ini memperkenalkan suatu algorima search engine berdasarkan konsep HARD (High Accuracy
									Retrieval from Documents) dengan menggabungkan penggunaan metoda TF-IDF (Term Frequency Inverse
									Document Frequency) dan Jaccards Coefficient. Kedua metoda, TF-IDF dan Jaccards Coefficient
									dimodifikasi dan dikembangkan dengan memperkenalkan beberapa rumusan baru. Untuk lebih
									memudahkan dalam mengerti algoritma dan rumusan baru yang diperkenalkan, beberapa contoh
									perhitungan diberikan.""",
					'processed_text':''
				},
				{
					'title':'Klasifikasi Dokumen Berita Kejadian Berbahasa Indonesia dengan Algoritma Single Pass Clustering',
					'raw_text':"""Pengelompokan dokumen berita dibutuhkan untuk mempermudah pencarian informasi
									mengenai suatu event (kejadian) tertentu. Pencarian berita-berita lain yang berkaitan dengan kejadian
									tersebut tentu sulit dilakukan, bila hanya mengandalkan query biasa. Sebab pemilihan query yang
									kurang spesifik akan berakibat membanjirnya dokumen-dokumen yang tidak relevan.
									Penelitian ini berusaha untuk mengklasifikasi dokumen dengan menggunakan algoritma single
									pass clustering. Klasifikasi ini ditekankan untuk dokumen berita berbahasa Indonesia, sebab dewasa
									ini, kebutuhan konsumen di tanah air terhadap informasi semakin meningkat. Adapun keterkaitan antar
									berita ini dapat diukur berdasarkan kemiripan antar dokumen (similarity).
									Algoritma ini diuji coba dengan menggunakan sampel berita dari media massa berbasis web.
									Hasil uji coba menunjukkan bahwa algoritma ini dapat diaplikasikan untuk pengelompokan berita-
									berita berbahasa Indonesia. Pemilihan nilai threshold yang tepat akan meningkatkan kualitas
									information retrieval (temu kembali informasi) pada dokumen. Kualitas ini tercermin dari tingkat
									recall 79 persen dan precision 88 persen.""",
					'processed_text':''
				},
				{
					'title':'PENGELOMPOKAN MAHASISWA MENGGUNAKAN ALGORITMA K-MEANS',
					'raw_text':"""Makalah ini membahas pengelompokan
										mahasiswa berdasarkan data akademik menggunakan teknik
										clustering dan membuat aplikasinya kemudian menganalisis
										hasilnya sehingga diharapkan mampu memberikan informasi bagi yang berkepentingan. Algoritma K-Means
										merupakan salah satu algoritma teknik clustering yang
										dimulai dengan pemilihan secara acak K, yang merupakan
										banyaknya cluster yang ingin dibentuk dari data yang akan di
										kluster, yaitu nilai tes mahasiswa saat masuk dan Indeks
										Prestasi Komulatif mahasiswa sampai semester 8. Sistem
										yang dibuat menampilkan hasil klustering data akademik
										mahasiswa, yaitu pola dari prestasi mahasiswa yang
										klusternya tetap, turun dan naik, dan dapat terlihat dari asal
										program studi, asal kota dan asal SMA. Dari hasil studi
										kasus dapat diperoleh informasi mahasiswa yang tetap pada
										kluster seperti awal masuk sebanyak 422 (45,085 persen),
										mahasiswa yang naik kluster sebanyak 284 (30,342 persen) dan
										mahasiswa yang turun klusternya sebanyak 230 (24,573 persen),""",
					'processed_text':'',
				},
				{
					'title':'Aplikasi Fuzzy Logic Controller pada Pengontrolan Lampu Lalu Lintas',
					'raw_text':"""Permasalahan kemacetan lalu lintas sudah
									menjadi masalah yang biasa di Indonesia. Salah satu upaya
									yang bisa digunakan untuk menguranginya adalah dengan
									membangun sistem pengontrolan lampu lalu lintas yang
									lebih baik dan efisien. Dengan sistem ini, kemacetan dan
									polusi dapat dikurangi. Sistem ini menggunakan fuzzy logic.
									Fuzzy logic merupakan ilmu yang sekarang sedang
									dikembangkan terutama untuk sistem pengontrol. Fuzzy
									logic mempunyai kelebihan seperti sederhana dan mampu
									diterjemahkan ke dalam bahasa manusia. Adapun fuzzy
									logic mempunyai performansi yang tidak kalah jika
									dibandingkan dengan solusi sistem yang sangat kompleks.
									Inilah yang membuat fuzzy logic digunakan daripada solusi
									sistem yang sangat kompleks. Contoh dari fuzzy logic
									controller yang telah digunakan di dunia adalah sistem
									pengontrol pendingin ruangan, sistem pengontrol kereta api
									bawah tanah Sendai di Jepang, dan sistem Animasi 3D
									MASSIVE.
									Sekarang
									banyak
									penelitian
									sedang
									dikembangkan oleh Jepang dan banyak negara lainnya yang
									matanya telah terbuka bahwa fuzzy logic mempunyai masa
									depan yang bagus. Adapun untuk membuat sistem
									pengontrol lampu lalu lintas ini, penulis menggunakan
									FIS(Fuzzy Inference System) dari perangkat lunak
									MATLAB dengan menggunakan metode Mamdani.""",
					'processed_text':'',
				},
				{
					'title':'KOMPRESI CITRA GRAY SCALE DENGAN MODIFIKASI ALGORITMA KUANTISASI',
					'raw_text':"""Suatu file yang kapasitasnya besar dapat diperkecil dengan
									pemampatan (compression). Untuk file image metode kuantisasi bisa
									menjadi salah satu pilihan. Pada citra grayscale metode kuantisasi
									bekerja dengan mengurangi derajat keabuan, sehingga jumlah bit
									yang digunakan untuk merepresentasikan citra menjadi berkurang.
									Oleh karena jumlah bit berkurang maka ukuran file menjadi lebih
									kecil. Dari algoritma kuantisasi yang ada, dilakukan modifikasi pada
									saat konversi derajat keabuan lama ke derajat keabuan yang baru,
									dengan mengabaikan unsur penyebaran derajat keabuan. Hasilnya
									kapasitas citra hasil kompresi tidak berubah. Histogram citra sangat
									berpengaruh terhadap hasil akhir.""",
					'processed_text':'',
				},
				{
					'title':'IMPLEMENTASI METODE SUPPORT VECTOR MACHINE (SVM) DAN FUZZY ANALYTIC HIERARCHY PROCESS (FAHP) PADA SISTEM PENDUKUNG KEPUTUSAN SELEKSI PENERIMAAN STUDENT EMPLOYEE',
					'raw_text':"""Student Employee adalah salah satu program pembelajaran dan pengembangan keilmuan untuk mahasiswa
										yang dilakukan suatu universitas guna meningkatkan kemampuan sesuai dengan bidang atau keminatan ilmu
										masing-masing. Tidak semua mahasiswa dapat bergabung sebagai Student Employee melainkan mahasiswa yang
										cukup berkompeten. Seleksi terhadap mahasiswa yang dilakukan pada proses awal pelaksanaan Student Employee
										bertujuan untuk mencari mahasiswa yang dinilai cukup berkompeten sehingga diharapkan nantinya mampu bekerja
										sesuai dengan harapan. Badan Pengembangan Teknologi dan Ilmu Komputer (BPTIK) dibawah naungan Program
										Teknologi Informasi dan Ilmu Komputer Universitas Brawijaya memiliki 4 tahapan seleksi penerimaan untuk
										menyaring mahasiswa yang dinilai cocok bergabung sebagai Student Employee. Adapun keempat tahapan tersebut
										secara berurutan yaitu tahap administrasi, tahap psikotes, tahap tes kemampaun, dan tahap wawancara. Beberapa
										tahapan dilakukan dengan cara yang bersifat subjektif dan manual sehingga resiko tingkat kesalahan pada
										perhitungan akhir (human error) sangatlah besar. Untuk itu dibutuhkan suatu sistem yang mampu meminimalkan
										subjektifitas penilaian dan mengurangi tingkat kesalahan pada perhitungan akhir pada seleksi penerimaan Student
										Employee BPTIK. Pada sistem tersebut menerapkan algoritma Sequential Training pada metode Support Vector
										Machine untuk proses training pada tahap psikotes dan metode Fuzzy Analytic Hierarchy Process untuk proses
										perangkingan berdasarkan skor akhir pada tahap tes kemampuan. Hasil dari pengujian didapatkan tingkat akurasi
										tertinggi pada tahap psikotes sebesar 80persen dan pada tahap tes kemampuan bidang programmer sebesar 75%, bidang
										web design sebesar 100%, bidang multimedia sebesar 100%, dan bidang network admin sebesar 75%.""",
					'processed_text':'',
				}
			]

def open_stopwords():
	f = open('stopword_list_tala.txt', 'r')
	for line in f:
		stopwords.append(line.replace('\n', ''))
	f.close()

def initialized_docbase():
	for txt in text_data:
		### TOKENIZING
		raw_txt = txt['raw_text'].replace('\t', '')
		raw_txt = raw_txt.replace('\n', ' ')
		raw_txt = raw_txt.replace('(', '')
		raw_txt = raw_txt.replace(')', '')
		raw_txt = raw_txt.replace('.', '')
		raw_txt = raw_txt.replace(',', '')
		raw_txt = raw_txt.replace('_', '')

		split_txt = raw_txt.split(' ')
		temp_split_txt = split_txt

		processed_txt = []

		### FILTERING
		for part in split_txt:
			if part.lower() in stopwords:
				continue
			else:
				processed_txt.append(part.lower())

		txt['processed_text'] = processed_txt
		# print txt['processed_text']		
		# print "\n"	

		### STEMMING: Coming Soon
		### TAGGING: Coming Soon

def tf_idf(key_word):
	#tf: banyak kata dalam dokumen
	#df: banyak dokumen yang mengandung kata
		
	total_docs = len(text_data)
	temp_result = {}

	for kw in key_word:
		tf = 0
		df = 0
		temp_result_item = {}
		for txt in text_data:
			for part in txt['processed_text']:
				if (part == kw):
					tf = tf + 1 
			if tf > 0:
				df = df + 1

			temp_result_item.update({txt['title']:{'tf':tf}})
			tf = 0
		
		temp_result.update({kw: temp_result_item})
		
		idf = 0.0
		if (float(df) != 0):
			idf = math.log(float(total_docs) / float(df))

		for txt in text_data:
			tf_idf = idf * temp_result[kw][txt['title']]['tf']
			temp_result[kw][txt['title']].update({'tf_idf': tf_idf})	

	final_result = []
	for txt in text_data:
		total_score = 0.0
		for res in temp_result:
			total_score = total_score + temp_result[res][txt['title']]['tf_idf']

		final_result.append({ txt['title']:total_score, 'tf_idf': temp_result[res][txt['title']]['tf_idf'] })

	for res in final_result:
		print res

# MAIN PROCESS
open_stopwords()
initialized_docbase()
tf_idf(['clustering', 'dokumen'])