stopwords = []
kewywords =  []
classifier = "text_class"
probability_data = {}

criteria_data = {
                'text_class': ['positive', 'negative']
            }

test_data = [
                {
                    'title':'sample-05', 
                    'raw_text':"""Bukan Prabowonya yg jelek, tp menurutku Jokowi lebih baik drpd Prabowo untuk bisa jadi presiden. Dapat dilihat dr prestasi yg dibuktikan JKW""", 
                    'processed_text':'',
                    'text_class':'',
                },
            ]
training_data = [
                    {
                        'title':'sample-20', 
                        'raw_text':"""PKS ini doyan banget beritain jelek Pa Jokowi? apa karena Pa Prabowo ga punya prestasi yg bagus? atau karena pendidikan Islamnya kurang?""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-19', 
                        'raw_text':"""Kadang liat orang yg ngina om jokowi ini prihatin udah macam mukanya bagus kali :( udah jelek sok ganteng ga ada prestasi pulak -_- uppss""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-18', 
                        'raw_text':"""Kasihan saya, Pak Jokowi memiliki prestasi yg dikenal di dunia tetapi dihina dan di jelek-jelekkan di negeri sendiri. Indonesia maunya apa?""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-17', 
                        'raw_text':"""BALIKKAN JOKOWI KE KAMPUNGNYA.. BBM maju mundur jelek.. GAK ADA PRESTASI, UTANG NAMBAH.. MEDIA ISLAM DI BLOKIR""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-16', 
                        'raw_text':"""Mahasiswa Brawijaya Beri Rapor Buruk untuk Jokowi""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-15', 
                        'raw_text':"""tapi aku tdk bs menghormati Jokowi dan bu Mega sbg oknum presiden ^_^ krn prestasi mrk yg luar biasa jelek""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-14', 
                        'raw_text':"""Miskin Prestasi, Jokowi Didesak Ganti Menteri Jelek""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-13', 
                        'raw_text':"""Sanksi FIFA adalah satu lagi prestasi buruk jokowi yg dianggap bagus oleh para pengikutnya""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-12', 
                        'raw_text':"""Djarot nih bagus, sama seperti Jokowi. Beliau fokus di bawah, dia suka UKM. Banyak prestasi juga. Sangat layak.. bisa jadi pasangan serasi""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-01', 
                        'raw_text':"""Tren ekonomi jelek saat itu terus berlanjut sampe jokowi jadi presiden. Target ekonomi gagal total, gak tercapai""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-02', 
                        'raw_text':"""gak munafik kalo ada yg bagus dari jokowi dia dukung kalo ada yg jelek kritisnya bukan maen.. wkwk""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-03', 
                        'raw_text':"""iye emang.. udah muka nya jelek.. kentutnya bau.. doyan duit cukong""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-04', 
                        'raw_text':"""Mungkin berita yang muncul selanjutnya, ini merupakan rekayasa dari jokowi agar partai kubu terlihat jelek :v""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-05', 
                        'raw_text':"""Yang sudah baik jadi jelek, yang sudah bersatu malah bercerai berai. Jokowi-JK gagal mengurus Bangsa Indonesia""", 
                        'processed_text':'',
                        'text_class':'negative',
                    },
                    {
                        'title':'sample-06', 
                        'raw_text':"""awal yg bagus pak, tolong pembangunan infrastruktur difokuskan di wilayah timur/papua pak, jangan hanya jawa. salam. :)""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-07', 
                        'raw_text':"""Selamat kpd bpk jokowi dalam kunjungan suku anak dalam yang sangat bagus dan menjadi contoh, kita semua bersaudara.""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-08', 
                        'raw_text':"""bagus dan keren abis bapak jokowi mengunjungi, membangun rumah, dan berbincang langsung dengan salah satu Suku Anak Dalam di jambi""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-09', 
                        'raw_text':"""Yang sudah baik jadi jelek, yang sudah bersatu malah bercerai berai. Jokowi-JK gagal mengurus Bangsa Indonesia""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-10', 
                        'raw_text':"""Prestasi DPR bagus kinerjanya berbeda dgn Jokowi bekerja tanpa lelah selalu dicaci maki oleh pembenci""", 
                        'processed_text':'',
                        'text_class':'positive',
                    },
                    {
                        'title':'sample-11', 
                        'raw_text':"""Prestasi Jokowi juga bagus, beliau berhasil mencatatkan kurs Rupiah menjadi 14.450/USD hari ini.""", 
                        'processed_text':'',
                        'text_class':'positive',
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
    raw_txt = txt['raw_text'].replace('\t', ' ')
    raw_txt = raw_txt.replace('\n', ' ')
    raw_txt = raw_txt.replace('(', ' ')
    raw_txt = raw_txt.replace(')', ' ')
    raw_txt = raw_txt.replace('.', ' ')
    raw_txt = raw_txt.replace(',', ' ')
    raw_txt = raw_txt.replace('_', ' ')

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