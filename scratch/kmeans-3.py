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

# fungsi - fungsi yang terlibat dalam perhitungan clustering k-means
def get_euclidean_distance(point_a, point_b):
    temp = math.sqrt((point_a['x'] - point_b['x']) ** 2 + (point_a['y'] - point_b['y']) ** 2)
    return temp

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

        # print temp_result

        closest_distance = find_min_dict(temp_result)
        # print closest_distance
        
        data_cluster[i]['cluster'] = closest_distance['cluster']
        
        # indeks untuk list
        i = i + 1

    return data_cluster

def generate_centroid(old_centroid, temp_cluster):
    temp_centroid = []
    
    for centroid in old_centroid:
        num = 0
        summation_x = 0.0
        summation_y = 0.0
        
        for item in temp_cluster:
            if centroid['cluster'] == item['cluster']:
                
                # print item['x'], item['y']

                summation_x = summation_x + item['x']
                summation_y = summation_y + item['y']
                num = num + 1

                # print summation_x, summation_y

        temp_centroid_x = summation_x / num
        temp_centroid_y = summation_y / num
        temp_centroid.append({'x':temp_centroid_x, 'y':temp_centroid_y, 'cluster':centroid['cluster']})


    return temp_centroid

def check_centroid_similarity(old_centroid, new_centroid):
    i = 0
    counter = 0
    for center in old_centroid:
        if center['x'] != new_centroid[i]['x'] or center['y'] != new_centroid[i]['y']: 
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

data_cluster = [
                    {'x':22.21, 'y':11.64, 'cluster':''},
                    {'x':43.25, 'y':8.95, 'cluster':''},
                    {'x':19.71, 'y':10.93, 'cluster':''},
                    {'x':21.05, 'y':10.38, 'cluster':''}, 
                    {'x':17.93, 'y':12.85, 'cluster':''},
                    {'x':17.72, 'y':12.0, 'cluster':''},
                    {'x':18.71, 'y':11.53, 'cluster':''},
                    {'x':25.86, 'y':9.33, 'cluster':''},
                    {'x':19.15, 'y':11.80, 'cluster':''},
                    {'x':18.42, 'y':11.20, 'cluster':''},
                    {'x':22.94, 'y':10.60, 'cluster':''},
                    {'x':26.89, 'y':10.44, 'cluster':''},
                    {'x':24.91, 'y':10.63, 'cluster':''},
                    {'x':22.99, 'y':11.47, 'cluster':''},
                    {'x':26.81, 'y':9.17, 'cluster':''},
                    {'x':21.09, 'y':10.67, 'cluster':''},
                    {'x':18.71, 'y':12.36, 'cluster':''},
                    {'x':20.58, 'y':10.80, 'cluster':''},
                    {'x':27.66, 'y':9.94, 'cluster':''},
                ]

centroid = [
                    {'x':20.0, 'y':9.0, 'cluster':'c1'},
                    {'x':23.0, 'y':15.0, 'cluster':'c2'},
                    {'x':27.0, 'y':11.0, 'cluster':'c3'},
                ]

colors = ['red', 'blue', 'green', 'yellow']


# main process
prev_centroid = centroid
new_cluster = do_cluster(centroid, data_cluster)
# print new_cluster

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
        print '\nnew cluster: '
        print_cluster(new_cluster)

        prev_centroid = new_centroid
        print "\nprev centroid: ", prev_centroid
        print "\n"
        
print_cluster(new_cluster)

# MENAMPILKAN ke dalam GRAFIK SCATTER 2D
area = np.pi * ( 5 ) ** 2

i = 0
for item in new_centroid:
    x_list = []
    y_list = []
    for data in new_cluster:
        if item['cluster'] == data['cluster']:
            x_list.append(data['x'])
            y_list.append(data['y'])

    plt.scatter(x_list, y_list, s=area, c=colors[i], alpha=1)

    i = i + 1

plt.show()