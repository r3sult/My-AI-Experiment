"""
created by  : ridwanbejo
deskripsi   : contoh implementasi algoritma K-Means untuk clustering data
"""

# library yang dibutuhkan untuk clustering k-means
import math
import collections
import copy
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

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
            # print k
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
    print cluster_attribute
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
        centroid_item['label'] = centroid['label']
        
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

def print_cluster(temp_cluster):
    print "\n====== HASIL AKHIR CLUSTER =====\n"
    for item in temp_cluster:
        print item

# contoh data yang akan dicluster
cluster = 2

prev_centroid = []
new_cluster = []

cluster_attribute = ['a', 'b', 'c', 'd', 'e']
data_cluster = [
                    {'a':100.0, 'b':94.0, 'c':100.0, 'd':75.0, 'e':100.0, 'cluster':'', 'label':"Riyan"},
                    {'a':100.0, 'b':90.0, 'c':80.0, 'd':89.0, 'e':100.0, 'cluster':'', 'label':"Bachtiar"},
                    {'a':100.0, 'b':96.0, 'c':74.0, 'd':99.0, 'e':87.5, 'cluster':'', 'label':"Asti"},
                    {'a':100.0, 'b':94.0, 'c':82.0, 'd':77.0, 'e':100.0, 'cluster':'', 'label':"Sigit"},
                    {'a':100.0, 'b':82.0, 'c':80.0, 'd':80.0, 'e':100.0, 'cluster':'', 'label':"Eka"},
                    {'a':100.0, 'b':78.0, 'c':80.0, 'd':78.0, 'e':100.0, 'cluster':'', 'label':"Andri"},
                    {'a':95.0, 'b':74.0, 'c':80.0, 'd':76.0, 'e':87.5, 'cluster':'', 'label':"Alifia"},
                    {'a':95.0, 'b':80.0, 'c':60.0, 'd':80.0, 'e':91.25, 'cluster':'', 'label':"Cecep"},
                    {'a':100.0, 'b':50.0, 'c':92.0, 'd':57.0, 'e':100, 'cluster':'', 'label':"Sukendi"},
                ]

centroid = [    
                {'a':100.0, 'b':90.0, 'c':80.0, 'd':89.0, 'e':100.0, 'cluster':'c1', 'label':"Bachtiar"},
                {'a':100.0, 'b':78.0, 'c':80.0, 'd':78.0, 'e':100.0, 'cluster':'c2', 'label':"Andri"},
            ]

colors = ['red', 'blue', 'green', 'yellow', 'purple']

# main process
prev_centroid = centroid
new_cluster = do_cluster(centroid, data_cluster)
print_cluster( new_cluster )

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

print_cluster(new_cluster)