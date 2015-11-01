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
from mpl_toolkits.mplot3d import Axes3D
import random

# fungsi - fungsi yang terlibat dalam perhitungan clustering k-means
def get_euclidean_distance(point_a, point_b):
    temp = math.sqrt((point_a['x'] - point_b['x']) ** 2 + (point_a['y'] - point_b['y']) ** 2 + (point_a['z'] - point_b['z']) ** 2 ) 
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
        summation_z = 0.0
        for item in temp_cluster:
            if centroid['cluster'] == item['cluster']:
                
                # print item['x'], item['y']

                summation_x = summation_x + item['x']
                summation_y = summation_y + item['y']
                summation_z = summation_z + item['z']
                num = num + 1

                # print summation_x, summation_y

        temp_centroid_x = summation_x / num
        temp_centroid_y = summation_y / num
        temp_centroid_z = summation_z / num
        
        temp_centroid.append({'x':temp_centroid_x, 'y':temp_centroid_y, 'z':temp_centroid_z, 'cluster':centroid['cluster']})


    return temp_centroid

def check_centroid_similarity(old_centroid, new_centroid):
    i = 0
    counter = 0
    for center in old_centroid:
        if center['x'] != new_centroid[i]['x'] or center['y'] != new_centroid[i]['y'] or center['z'] != new_centroid[i]['z']: 
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
                    {'x':22.21, 'y':11.64, 'z':30.0, 'cluster':''},
                    {'x':43.25, 'y':8.95, 'z':40.0,'cluster':''},
                    {'x':19.71, 'y':10.93, 'z':50,'cluster':''},
                    {'x':21.05, 'y':10.38, 'z':60,'cluster':''}, 
                    {'x':17.93, 'y':12.85, 'z':70,'cluster':''},
                ]

centroid = []

colors = ['red', 'blue', 'green', 'yellow', 'purple']

# generate centroid random
for i in range (1, 6):
    temp_x = float(random.randrange(1, 100))
    temp_y = float(random.randrange(1, 100))
    temp_z = float(random.randrange(1, 100))
    
    random_centroid = {'x':temp_x, 'y':temp_y, 'z':temp_z, 'cluster':'c'+str(i-1)}
    centroid.append(random_centroid)

# generate data random
for i in range(0, 5000):
    temp_cluster_x = float(random.randrange(1, 100))
    temp_cluster_y = float(random.randrange(1, 100))
    temp_cluster_z = float(random.randrange(1, 100))

    random_cluster = {'x':temp_cluster_x, 'y':temp_cluster_y, 'z':temp_cluster_z, 'cluster':''}
    data_cluster.append(random_cluster)


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
        # print '\nnew cluster: ', new_cluster
        prev_centroid = new_centroid
        # print "\nprev centroid: ", prev_centroid
        # print "\n"

# print_cluster(new_cluster)

# menampilkan ke dalam grafik scatter 3D
area = np.pi * ( 4 ) ** 2
fig = plt.figure()
ax = Axes3D(fig)

i = 0
for item in new_centroid:
    x_list = []
    y_list = []
    z_list = []
    for data in new_cluster:
        if item['cluster'] == data['cluster']:
            x_list.append(data['x'])
            y_list.append(data['y'])
            z_list.append(data['z'])

    ax.scatter(x_list, y_list, z_list, zdir=u'z', s=area, c=colors[i])

    i = i + 1

plt.show()