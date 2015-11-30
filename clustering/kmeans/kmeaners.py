"""
created by  : ridwanbejo
deskripsi   : contoh implementasi algoritma K-Means untuk clustering data
"""

# library yang dibutuhkan untuk clustering k-means
import math
import matplotlib.pyplot as plt
import numpy as np

# fungsi - fungsi yang terlibat dalam perhitungan clustering k-means
def get_euclidean_distance(point_a, point_b):
    temp = 0.0
    for attrib in cluster_attribute:
        temp = temp + (point_a[attrib] - point_b[attrib]) ** 2 
    
    temp2 = math.sqrt( temp ) 
    
    return temp2

def find_min_dict(dicto):
        temp_v = 999999999999999
        temp_k = {}

        for k in dicto:
            if k['distance'] < temp_v :
                temp_v = k['distance']
                temp_k = k

        return temp_k

def do_cluster(centroid, data_cluster):
    i = 0
    for data in data_cluster:
        temp_result = []
        for center in centroid:
            distance = get_euclidean_distance(data, center)
            temp_result.append({ 'distance':distance, 'cluster':center['cluster'] })

        closest_distance = find_min_dict(temp_result)
        
        data_cluster[i]['cluster'] = closest_distance['cluster']
        
        # indeks untuk list
        i = i + 1

    return data_cluster

def generate_centroid(old_centroid, temp_cluster):
    temp_centroid = []
    for centroid in old_centroid:
        num = 0
        summation = {}
        centroid_item = {}

        for attrib in cluster_attribute:
            summation[attrib] = 0.0

        for item in temp_cluster:
            if centroid['cluster'] == item['cluster']:
                for attrib in cluster_attribute:
                    summation[attrib] = summation[attrib] + item[attrib]
                
                num = num + 1
        
        for attrib in cluster_attribute:        
            centroid_item[attrib] = summation[attrib] / num
        
        centroid_item['cluster'] = centroid['cluster']
        # centroid_item['label'] = centroid['label']
        
        temp_centroid.append(centroid_item)

    return temp_centroid

def check_centroid_similarity(old_centroid, new_centroid):
    i = 0
    counter = 0
    for center in old_centroid:
        temp_check = True
        for attrib in cluster_attribute:
            if center[attrib] != new_centroid[i][attrib]: 
                temp_check = True
            else:
                temp_check = False

        if temp_check == True:
            counter = counter + 1
            
        i = i + 1

    return counter

def print_cluster(temp_cluster, format="", temp_centroid=""):
    print "\n====== CLUSTER BARU =====\n"
    if (format=="table"):
        for item in temp_cluster:
            for head in headers:
                print item[head], '\t',
            print item['cluster']

    elif(format == 'cluster'):
        for item in temp_centroid:
            print "\n====> ", item['cluster'].upper(), '\n'
            for data in temp_cluster:
                if (item['cluster'] == data['cluster']):
                    for head in headers:
                        print data[head], '\t',
                    print data['cluster']
            

    else:
        for item in temp_cluster:
            print item

def main_process (cluster_attribute, data_cluster, centroid):
    # contoh data yang akan dicluster
    prev_centroid = []
    new_cluster = []
    colors = ['red', 'blue', 'green', 'yellow', 'purple']

    # main process
    prev_centroid = centroid
    new_cluster = do_cluster(prev_centroid, data_cluster)
    print prev_centroid
    # print_cluster(new_cluster, 'table')

    print "\n====== PENENTUAN CENTROID =====\n"

    while True:
        new_centroid = generate_centroid(prev_centroid, new_cluster)
        print "new centroid: ", new_centroid

        centroid_similarity = check_centroid_similarity(prev_centroid, new_centroid)

        print centroid_similarity

        if (centroid_similarity <= 0):
            break
        elif (centroid_similarity > 0):
            new_cluster = do_cluster(new_centroid, data_cluster)
            prev_centroid = new_centroid
            
    print_cluster(new_cluster, 'cluster', new_centroid)

# variabel global
cluster_attribute = []
data_cluster = []
centroid = []
headers = []
cluster = 10

# membaca file yang akan dilakukan pemrosesan clustering
files = open('data/house16.txt', 'r')

for line in files:
    if line.find('@attribute') == 0:
        attr_list = line.replace('@attribute','').strip()
        for attrib in attr_list.split(','):
            cluster_attribute.append(attrib)
        break

print cluster_attribute

files.seek(0)
for line in files:
    if line.find('@header') == 0:
        header_list = line.replace('@header', '').strip()
        for head in header_list.split(','):
            headers.append(head)
        break

print headers

files.seek(0)
process_data = False
for line in files:
    if line.find('@data') == 0:
        process_data = True
        continue

    if line.find('@end_data') == 0:
        break

    if process_data:
        # print line
        temp_cluster_data = line.split(',')
        # print temp_cluster_data
        cluster_data = {}
        
        i = 0
        for head in headers:
            # print i
            if head in cluster_attribute:
                cluster_data[head] = float(temp_cluster_data[i].replace('\n', ''))
            else:
                cluster_data[head] = temp_cluster_data[i].replace('\n', '')
            
            i = i + 1

        cluster_data['cluster'] = ''
        data_cluster.append(cluster_data)

files.close()

# menentukan centroid
for k in range(cluster):
    temp_centroid = data_cluster[k]
    temp_centroid['cluster'] = 'c'+str(k)
    centroid.append(temp_centroid)

# main process
main_process(cluster_attribute, data_cluster, centroid)