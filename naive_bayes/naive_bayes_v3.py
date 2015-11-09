stopwords = []
kewywords =  []
classifier = "text_class"
probability_data = {}

# criteria_data = {
#                 'text_class': ['information_retrieval', 'artificial_intelligence', 'data_mining', 'image_processing']
#             }
# test_data = [
#                 {
#                     'title':'Klasifikasi Posting Twitter Kemacetan Lalu Lintas Kota Bandung Menggunakan Naive Bayesian Classification', 
#                     'raw_text':"""KOMPRESI CITRA BERWARNA MENGGUNAKAN METODE POHON BINER
#                                     HUFFMAN. Makalah ini membahas tentang algoritma kompresi citra dengan menggunakan metode
#                                     pohon biner Huffman. Metode ini biasanya digunakan untuk mengkompres file teks dikembangkan
#                                     menjadi algoritma untuk mengkompres citra berwarna. Hasil yang diperoleh menunjukan bahwa
#                                     algoritma ini memiliki nilai rasio kompresi di atas satu jika jumlah warna yang terdapat dalam citra tidak
#                                     lebih dari 100 warna. Sedang kualitas citra hasil dekompresinya memiliki kualitas yang sama dengan citra
#                                     aslinya.""", 
#                     'processed_text':'',
#                     'text_class':'',
#                 },
#             ]
# training_data = [
#                 {
#                     'title':'STEMMING DOKUMEN TEKS BAHASA INDONESIA MENGGUNAKAN ALGORITMA PORTER', 
#                     'raw_text':"""Informasi merupakan hal yang
#                         sangat mudah didapatkan dan diakses. Tetapi
#                         terkadang informasi yang diperoleh tidak sesuai dengan apa yang diinginkan pengguna.
#                         Diperlukan sistem yang dapat membantu mencari informasi yang dibutuhkan secara efektif
#                         dan efisien. Sistem informasi ini sering kali disebut dengan istilah sistem temu kembali
#                         informasi (STKI). Pada STKI salah satu tahapan yang sangat penting adalah tahap
#                         Stemming. Tahapan ini merupakan tahapan mentransformasikan kata dalam sebuah kalimat
#                         atau dokumen ke kata dasarnya. Pada penelitian ini, akan dijelaskan proses Stemming pada
#                         kalimat bahasa indonesia dengan menggunakan algortitma porter untuk mendapat root word
#                         dari kata dalam dokumen teks. Tahapan yang ada pada algoritma porter diterjemahkan
#                         menjadi koding program PHP. Kamus kata dasar dan stoplist disimpan di MySql. Pada
#                         proses stemming dilakukan tidak kata perkata, akan tetapi langsung stemming pada
#                         dokumen. Sehingga proses stemming yang dilakukan lebih cepat dan efektif.""", 
#                     'processed_text':'',
#                     'text_class':'information_retrieval',
#                 },
#                 {
#                     'title':'HARD SUBJECT-BASED SEARCH ENGINE MENGGUNAKAN TF-IDF DAN JACCARDS COEFFICIENT',
#                     'raw_text':"""Paper ini memperkenalkan suatu algorima search engine berdasarkan konsep HARD (High Accuracy
#                                     Retrieval from Documents) dengan menggabungkan penggunaan metoda TF-IDF (Term Frequency Inverse
#                                     Document Frequency) dan Jaccards Coefficient. Kedua metoda, TF-IDF dan Jaccards Coefficient
#                                     dimodifikasi dan dikembangkan dengan memperkenalkan beberapa rumusan baru. Untuk lebih
#                                     memudahkan dalam mengerti algoritma dan rumusan baru yang diperkenalkan, beberapa contoh
#                                     perhitungan diberikan.""",
#                     'processed_text':'',
#                     'text_class':'information_retrieval',
#                 },
#                 {
#                     'title':'Klasifikasi Dokumen Berita Kejadian Berbahasa Indonesia dengan Algoritma Single Pass Clustering',
#                     'raw_text':"""Pengelompokan dokumen berita dibutuhkan untuk mempermudah pencarian informasi
#                                     mengenai suatu event (kejadian) tertentu. Pencarian berita-berita lain yang berkaitan dengan kejadian
#                                     tersebut tentu sulit dilakukan, bila hanya mengandalkan query biasa. Sebab pemilihan query yang
#                                     kurang spesifik akan berakibat membanjirnya dokumen-dokumen yang tidak relevan.
#                                     Penelitian ini berusaha untuk mengklasifikasi dokumen dengan menggunakan algoritma single
#                                     pass clustering. Klasifikasi ini ditekankan untuk dokumen berita berbahasa Indonesia, sebab dewasa
#                                     ini, kebutuhan konsumen di tanah air terhadap informasi semakin meningkat. Adapun keterkaitan antar
#                                     berita ini dapat diukur berdasarkan kemiripan antar dokumen (similarity).
#                                     Algoritma ini diuji coba dengan menggunakan sampel berita dari media massa berbasis web.
#                                     Hasil uji coba menunjukkan bahwa algoritma ini dapat diaplikasikan untuk pengelompokan berita-
#                                     berita berbahasa Indonesia. Pemilihan nilai threshold yang tepat akan meningkatkan kualitas
#                                     information retrieval (temu kembali informasi) pada dokumen. Kualitas ini tercermin dari tingkat
#                                     recall 79 persen dan precision 88 persen.""",
#                     'processed_text':'',
#                     'text_class':'data_mining',
#                 },
#                 {
#                     'title':'PENGELOMPOKAN MAHASISWA MENGGUNAKAN ALGORITMA K-MEANS',
#                     'raw_text':"""Makalah ini membahas pengelompokan
#                                         mahasiswa berdasarkan data akademik menggunakan teknik
#                                         clustering dan membuat aplikasinya kemudian menganalisis
#                                         hasilnya sehingga diharapkan mampu memberikan informasi bagi yang berkepentingan. Algoritma K-Means
#                                         merupakan salah satu algoritma teknik clustering yang
#                                         dimulai dengan pemilihan secara acak K, yang merupakan
#                                         banyaknya cluster yang ingin dibentuk dari data yang akan di
#                                         kluster, yaitu nilai tes mahasiswa saat masuk dan Indeks
#                                         Prestasi Komulatif mahasiswa sampai semester 8. Sistem
#                                         yang dibuat menampilkan hasil klustering data akademik
#                                         mahasiswa, yaitu pola dari prestasi mahasiswa yang
#                                         klusternya tetap, turun dan naik, dan dapat terlihat dari asal
#                                         program studi, asal kota dan asal SMA. Dari hasil studi
#                                         kasus dapat diperoleh informasi mahasiswa yang tetap pada
#                                         kluster seperti awal masuk sebanyak 422 (45,085 persen),
#                                         mahasiswa yang naik kluster sebanyak 284 (30,342 persen) dan
#                                         mahasiswa yang turun klusternya sebanyak 230 (24,573 persen),""",
#                     'processed_text':'',
#                     'text_class':'data_mining'
#                 },
#                 {
#                     'title':'Aplikasi Fuzzy Logic Controller pada Pengontrolan Lampu Lalu Lintas',
#                     'raw_text':"""Permasalahan kemacetan lalu lintas sudah
#                                     menjadi masalah yang biasa di Indonesia. Salah satu upaya
#                                     yang bisa digunakan untuk menguranginya adalah dengan
#                                     membangun sistem pengontrolan lampu lalu lintas yang
#                                     lebih baik dan efisien. Dengan sistem ini, kemacetan dan
#                                     polusi dapat dikurangi. Sistem ini menggunakan fuzzy logic.
#                                     Fuzzy logic merupakan ilmu yang sekarang sedang
#                                     dikembangkan terutama untuk sistem pengontrol. Fuzzy
#                                     logic mempunyai kelebihan seperti sederhana dan mampu
#                                     diterjemahkan ke dalam bahasa manusia. Adapun fuzzy
#                                     logic mempunyai performansi yang tidak kalah jika
#                                     dibandingkan dengan solusi sistem yang sangat kompleks.
#                                     Inilah yang membuat fuzzy logic digunakan daripada solusi
#                                     sistem yang sangat kompleks. Contoh dari fuzzy logic
#                                     controller yang telah digunakan di dunia adalah sistem
#                                     pengontrol pendingin ruangan, sistem pengontrol kereta api
#                                     bawah tanah Sendai di Jepang, dan sistem Animasi 3D
#                                     MASSIVE.
#                                     Sekarang
#                                     banyak
#                                     penelitian
#                                     sedang
#                                     dikembangkan oleh Jepang dan banyak negara lainnya yang
#                                     matanya telah terbuka bahwa fuzzy logic mempunyai masa
#                                     depan yang bagus. Adapun untuk membuat sistem
#                                     pengontrol lampu lalu lintas ini, penulis menggunakan
#                                     FIS(Fuzzy Inference System) dari perangkat lunak
#                                     MATLAB dengan menggunakan metode Mamdani.""",
#                     'processed_text':'',
#                     'text_class':'artificial_intelligence',
#                 },
#                 {
#                     'title':'KOMPRESI CITRA GRAY SCALE DENGAN MODIFIKASI ALGORITMA KUANTISASI',
#                     'raw_text':"""Suatu file yang kapasitasnya besar dapat diperkecil dengan
#                                     pemampatan (compression). Untuk file image metode kuantisasi bisa
#                                     menjadi salah satu pilihan. Pada citra grayscale metode kuantisasi
#                                     bekerja dengan mengurangi derajat keabuan, sehingga jumlah bit
#                                     yang digunakan untuk merepresentasikan citra menjadi berkurang.
#                                     Oleh karena jumlah bit berkurang maka ukuran file menjadi lebih
#                                     kecil. Dari algoritma kuantisasi yang ada, dilakukan modifikasi pada
#                                     saat konversi derajat keabuan lama ke derajat keabuan yang baru,
#                                     dengan mengabaikan unsur penyebaran derajat keabuan. Hasilnya
#                                     kapasitas citra hasil kompresi tidak berubah. Histogram citra sangat
#                                     berpengaruh terhadap hasil akhir.""",
#                     'processed_text':'',
#                     'text_class':'image_processing',
#                 },
#                 {
#                     'title':'IMPLEMENTASI METODE SUPPORT VECTOR MACHINE (SVM) DAN FUZZY ANALYTIC HIERARCHY PROCESS (FAHP) PADA SISTEM PENDUKUNG KEPUTUSAN SELEKSI PENERIMAAN STUDENT EMPLOYEE',
#                     'raw_text':"""Student Employee adalah salah satu program pembelajaran dan pengembangan keilmuan untuk mahasiswa
#                                         yang dilakukan suatu universitas guna meningkatkan kemampuan sesuai dengan bidang atau keminatan ilmu
#                                         masing-masing. Tidak semua mahasiswa dapat bergabung sebagai Student Employee melainkan mahasiswa yang
#                                         cukup berkompeten. Seleksi terhadap mahasiswa yang dilakukan pada proses awal pelaksanaan Student Employee
#                                         bertujuan untuk mencari mahasiswa yang dinilai cukup berkompeten sehingga diharapkan nantinya mampu bekerja
#                                         sesuai dengan harapan. Badan Pengembangan Teknologi dan Ilmu Komputer (BPTIK) dibawah naungan Program
#                                         Teknologi Informasi dan Ilmu Komputer Universitas Brawijaya memiliki 4 tahapan seleksi penerimaan untuk
#                                         menyaring mahasiswa yang dinilai cocok bergabung sebagai Student Employee. Adapun keempat tahapan tersebut
#                                         secara berurutan yaitu tahap administrasi, tahap psikotes, tahap tes kemampaun, dan tahap wawancara. Beberapa
#                                         tahapan dilakukan dengan cara yang bersifat subjektif dan manual sehingga resiko tingkat kesalahan pada
#                                         perhitungan akhir (human error) sangatlah besar. Untuk itu dibutuhkan suatu sistem yang mampu meminimalkan
#                                         subjektifitas penilaian dan mengurangi tingkat kesalahan pada perhitungan akhir pada seleksi penerimaan Student
#                                         Employee BPTIK. Pada sistem tersebut menerapkan algoritma Sequential Training pada metode Support Vector
#                                         Machine untuk proses training pada tahap psikotes dan metode Fuzzy Analytic Hierarchy Process untuk proses
#                                         perangkingan berdasarkan skor akhir pada tahap tes kemampuan. Hasil dari pengujian didapatkan tingkat akurasi
#                                         tertinggi pada tahap psikotes sebesar 80persen dan pada tahap tes kemampuan bidang programmer sebesar 75%, bidang
#                                         web design sebesar 100%, bidang multimedia sebesar 100%, dan bidang network admin sebesar 75%.""",
#                     'processed_text':'',
#                     'text_class':'data_mining',
#                 },
#                 {
#                     'title':'KLASIFIKASI DOKUMEN NASKAH DINAS MENGGUNAKAN ALGORITMA TERM FREQUENCY INVERSED DOCUMENT FREQUENCY DAN VECTOR SPACE MODE',
#                     'raw_text':"""Penelitian ini bertujuan untuk merancang dan mengimplementasikan sistem klasifikasi dokumen naskah dinas
#                                     dengan banyak kategori sehingga dapat mempermudah dalam penyimpanan dan pencarian dokumen naskah
#                                     dinas. Penelitian ini menerapkan metode text mining dengan supervised learning menggunakan algoritma term
#                                     frequency  inverse document frequency (TFIDF) dan vector space model. Metode text mining menggunakan
#                                     teks di dokumen untuk menentukan kata kunci. Algoritma TFIDF melakukan pemberian bobot pada setiap kata
#                                     kunci disetiap kategori dan vector space model untuk mencari kemiripan kata kunci dengan kategori yang
#                                     tersedia. Implementasi sistem ini melakukan pembelajaran untuk mendapatkan model dari setiap kategori
#                                     sehingga pada saat klasifikasi menggunakan model tersebut untuk dibandingkan dengan data uji. Hasil
#                                     penelitian ini menunjukkan bahwa perbedaan jumlah data training mempengaruhi akurasi klasifikasi dokumen.
#                                     Faktor fisik dokumen dan hasil pembacaan optical character recognition (OCR) juga menjadi factor yang dapat
#                                     mempengaruhi akurasi klasifikasi dokumen.""",
#                     'processed_text':'',
#                     'text_class':'data_mining',
#                 },
#                 {
#                     'title':'KOMPRESI CITRA BERWARNA MENGGUNAKAN METODE POHON BINER HUFFMAN',
#                     'raw_text':"""KOMPRESI CITRA BERWARNA MENGGUNAKAN METODE POHON BINER
#                                     HUFFMAN. Makalah ini membahas tentang algoritma kompresi citra dengan menggunakan metode
#                                     pohon biner Huffman. Metode ini biasanya digunakan untuk mengkompres file teks dikembangkan
#                                     menjadi algoritma untuk mengkompres citra berwarna. Hasil yang diperoleh menunjukan bahwa
#                                     algoritma ini memiliki nilai rasio kompresi di atas satu jika jumlah warna yang terdapat dalam citra tidak
#                                     lebih dari 100 warna. Sedang kualitas citra hasil dekompresinya memiliki kualitas yang sama dengan citra
#                                     aslinya.""",
#                     'processed_text':'',
#                     'text_class':'image_processing',
#                 },
#                 {
#                     'title':'IDENTIFIKASI SEL KANKER PROSTAT MENGGUNAKAN METODE SEGMENTASI BERDASAR UKURAN OBJEK PADA CITRA',
#                     'raw_text':"""Pada saat ini, dunia ilmu kedokteran memerlukan inovasi-inovasi terautomatisasi, satu diantaranya adalah
#                                     pendeteksian sel kanker prostat. Pendeteksian secara manual akan memerlukan banyak waktu, terutama pendeteksian
#                                     yang berjarak jauh dan rumit. Oleh karena perlu dibuat program yang dapat mengidentifikasi sel kanker prostat pada
#                                     suatu citra secara cepat dan automatis, sehingga diperoleh analisis dan identifikasi yang akurat.
#                                     Analisis citra merupakan salah satu metode dalam pengolahan citra digital. Proses prapengolahan citra
#                                     digital dimulai dari akuisisi data citra, deteksi tepi, segmentasi dan pengambangan, hingga citra siap dianalisis.
#                                     Analisis citra yang dilakukan dalam hal ini adalah pendeteksian sel kanker prostat menggunakan metode segmentasi
#                                     sampai dengan sel kanker prostat dapat dideteksi dan dipisahkan dari latarbelakangnya. Analisis citra juga dapat untuk
#                                     membedakan citra sel prostat yang sakit dan yang sehat dengan menghitung jumlah pikselnya.
#                                     Program yang dibuat memiliki kemampuan untuk mengenali citra sehingga dapat dihitung jumlah piksel citra
#                                     sel prostat yang sakit dan citra sel prostat yang sehat. Dari penelitian yang dilakukan, dapat disimpulkan bahwa jumlah
#                                     piksel minimum untuk sel prostat sakit sebelum penebalan tepi adalah 425 piksel dan jumlah piksel maksimumnya
#                                     adalah 703 piksel. Sedangkan jumlah piksel minimum untuk sel prostat sakit setelah penebalan tepi adalah 497 piksel
#                                     dan jumlah piksel maksimumnya adalah 808 piksel. Untuk sel prostat yang sehat, jumlah piksel minimum sebelum
#                                     penebalan tepi adalah 778 piksel dan jumlah piksel maksimumnya adalah 2427 piksel. Sedangkan untuk sel prostat
#                                     sehat setelah penebalan tepi, jumlah piksel minimumnya adalah 920 piksel dan jumlah piksel maksimumnya adalah
#                                     2599 piksel. Toleransi untuk sel prostat sakit adalah 15,73persen dan toleransi untuk sel prostat sehat adalah 11,74persen.""",
#                     'processed_text':'',
#                     'text_class':'image_processing',
#                 }
#             ]

# criteria_data = {
#                 'text_class': ['china', 'japan']
#             }
# test_data = [
#                 {
#                     'title':'sample-05', 
#                     'raw_text':"""Chinese Chinese Chinese Tokyo Japan""", 
#                     'processed_text':'',
#                     'text_class':'',
#                 },
#             ]
# training_data = [
#                     {
#                         'title':'sample-01', 
#                         'raw_text':"""Chinese Beijing Chinese""", 
#                         'processed_text':'',
#                         'text_class':'china',
#                     },
#                     {
#                         'title':'sample-02', 
#                         'raw_text':"""Chinese Chinese Shanghai""", 
#                         'processed_text':'',
#                         'text_class':'china',
#                     },
#                     {
#                         'title':'sample-03', 
#                         'raw_text':"""Chinese Macao""", 
#                         'processed_text':'',
#                         'text_class':'china',
#                     },
#                     {
#                         'title':'sample-04', 
#                         'raw_text':"""Tokyo Japan Chinese""", 
#                         'processed_text':'',
#                         'text_class':'japan',
#                     },
#                 ]

criteria_data = {
                'text_class': ['android', 'delphi', 'office']
            }
test_data = [
                {
                    'title':'sample-07', 
                    'raw_text':"""Tolong dong, gimana membuat daftar isi secara otomatis dengan Ms Word.""", 
                    'processed_text':'',
                    'text_class':'',
                },
            ]
training_data = [
                    {
                        'title':'sample-01', 
                        'raw_text':"""Bagaimana cara membuat Galeri Image
                                        pada Eclipse""", 
                        'processed_text':'',
                        'text_class':'Android',
                    },
                    {
                        'title':'sample-02', 
                        'raw_text':"""Ada yang tau gak cara membuat koneksi
                                        pada Delphi dengan MysQL""", 
                        'processed_text':'',
                        'text_class':'delphi',
                    },
                    {
                        'title':'sample-03', 
                        'raw_text':"""Saya
                                        kesulitan
                                        dalam
                                        membuat
                                        Mailmerge pada Ms Word, bagaimana
                                        caranya ya?""", 
                        'processed_text':'',
                        'text_class':'office',
                    },
                    {
                        'title':'sample-04', 
                        'raw_text':"""Membuat fungsi Sum pada Ms Excel
                                        seperti apa ya?""", 
                        'processed_text':'',
                        'text_class':'office',
                    },
                    {
                        'title':'sample-05', 
                        'raw_text':"""Bagaimana cara menghilangkan warning
                                        pada Android""", 
                        'processed_text':'',
                        'text_class':'android',
                    },
                    {
                        'title':'sample-06', 
                        'raw_text':"""Bagaimana membuat form cetak dengan
                                        Delphi""", 
                        'processed_text':'',
                        'text_class':'delphi',
                    },
                ]

def open_stopwords():
    f = open('stopword_list_tala.txt', 'r')
    for line in f:
        stopwords.append(line.replace('\n', ''))
    f.close()

def get_keywords(text_data):
    temp_keyword = []

    for txt in text_data:
        for term in  txt['processed_text']:
            if term in temp_keyword:
                continue
            else:
                temp_keyword.append(term)

    return temp_keyword

def clean_text(txt):
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
    
    temp_processed_txt = []
    for part in processed_txt:
        if part == '':
            continue
        else:
            temp_processed_txt.append(part)

    return temp_processed_txt

    ### STEMMING: Coming Soon
    ### TAGGING: Coming Soon

def initialized_docbase():
    for txt in training_data:
       txt['processed_text'] = clean_text(txt)    

def print_data(data):
    for d in data:
        print d,':',data[d]

def init_bayesian():
    len_data = len(training_data)
    for classy in criteria_data[classifier]:
        temp_dict = {classy:{'value':0.0, 'length':0.0, 'p_x':0.0, 'p_ci_x':0.0, 'n_len':0}}

        probability_data.update(temp_dict)
        
    # menghitung P(Ci)
    for classy in criteria_data[classifier]:
        temp = 0.0
        for data in training_data:
            if data[classifier] == classy:
                temp = temp + 1

        probability_data[classy]['value'] = temp / len_data
        probability_data[classy]['length'] = temp

def naive_bayes(item):
    print item['processed_text']
    
    keywords_len = len(keywords)
    print keywords_len

    # for classy in criteria_data[classifier]:
    #     temp_text_data = []
    #     for txt in training_data:
    #         if classy == txt['text_class']:
    #             temp_text_data.append(txt)

    #     probability_data[classy]['n_len'] = len(get_keywords(temp_text_data))
    #     print probability_data[classy]   

    for classy in criteria_data[classifier]:
        p_ai_vj = 1.0
        for ptxt in item['processed_text']:
            count_term = 0
            count_word = 0
            for txt in training_data:
                if classy == txt['text_class']:
                    count_word = count_word + len(txt['processed_text'])
                    for txt2 in txt['processed_text']:
                        if txt2 == ptxt:
                            count_term = count_term + 1

            # print count_term
            # print count_word
            # print keywords_len
            # print ""

            temp_p_ai_vj = (float(count_term) + 1) / (count_word + keywords_len)
            p_ai_vj = p_ai_vj * temp_p_ai_vj

        print classy, ':', p_ai_vj * probability_data[classy]['value']

    # menghitung P(X | Ci)
    # for classy in criteria_data[classifier]:
    #     for key in item:
    #         if key != classifier:
    #             temp = 0.0
    #             for data in training_data:
    #                 if data[key] == item[key] and data[classifier] == classy:
    #                     temp = temp + 1
                
    #             probability_data[classy][key][item[key]] = temp / probability_data[classy]['length']

    # menghitung P(X)
    # for classy in criteria_data[classifier]:
    #     temp = 1.0
    #     for key in item:
    #         if key != classifier:
    #             temp = temp * probability_data[classy][key][item[key]]

    #     probability_data[classy]['p_x'] = temp

    # # menghitung P(Ci | X)
    # result = []
    # for classy in criteria_data[classifier]:
    #     probability_data[classy]['p_ci_x'] = probability_data[classy]['p_x'] * probability_data[classy]['value']
    #     result.append(probability_data[classy]['p_ci_x'])

    # final_result = max(result)

    # for classy in criteria_data[classifier]:
    #     if final_result == probability_data[classy]['p_ci_x']:
    #         item[classifier] = classy 

    # # print probability_data
    # print "\n====== HASIL AKHIR ======"
    # print item

open_stopwords()
initialized_docbase()
keywords = get_keywords(training_data)

init_bayesian()

print_data( probability_data )
test_data[0]['processed_text'] = clean_text(test_data[0])
naive_bayes(test_data[0])