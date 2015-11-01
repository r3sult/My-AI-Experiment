 # input
# ----------------------------------------------------------------------
# jarak : dekat (0 to 250 turun), sedang (200 to 300 naik, 300 to 400 turun), jauh (350 to 500 naik)
# darah : sangat rendah (0 to 20 turun, rendah (10 to 30 naik, 30 to 50 turun), sedang (40 to 60 naik, 60 to 80 turun), tinggi (70 to 90 naik, 90 to 110 turun), sangat tinggi (100 to 120 naik)

# output
#------------------------------------------------------------------------
# aksi  :  mundur (0 to 40 turun), kabur (20 to 40 naik, 40 to 80 turun), serang (70 to 100 naik)

# menggunakan cara perhitungan COG dibantu dengan Persamaan Garis

import random
import os
import time
class FuzzyRTSEngine:

    def __init__(self, jarak=0, darah=0):
        self.jarak = jarak
        self.darah = darah
        
    def jarak_membership(self, jarak):
        
        jarak_dict = {}
        temp = 0
        
        # dekat (0 to 250 turun)
        if jarak <= 0 or jarak >= 250:
            jarak_dict.update({'near':0})
        elif 0 < jarak <= 250:
            temp = (- (jarak - 250.0) )/ (250.0 - 0)
            jarak_dict.update({'near':temp}) 
        
        # sedang (200 to 300 naik, 300 to 400 turun)
        if jarak <= 200 or jarak >= 400:
            jarak_dict.update({'medium':0})
        elif 200 < jarak <= 300:
            temp = (jarak - 200.0) / (300.0 - 200.0)
            jarak_dict.update({'medium':temp})
        elif 300 < jarak <= 400:
            temp = (- (jarak - 400.0) )/ (400.0 - 300.0)
            jarak_dict.update({'medium':temp}) 
        
        # jauh (350 to 500 naik)
        if jarak <= 350 or jarak >= 500:
            jarak_dict.update({'far':0})
        elif 350 < jarak <= 500:
            temp = (jarak - 350.0) / (500.0 - 350.0)
            jarak_dict.update({'far':temp})
        
        return jarak_dict

    def darah_membership(self, darah):
        darah_dict = {} 
        temp = 0
        
        #sangat rendah (0 to 20 turun, 
        if darah <= 0 or darah >= 20:
            darah_dict.update({'verylow':0})
        elif 0 < darah <= 20:
            temp = (- (darah - 20.0) )/ (20.0 - 0)
            darah_dict.update({'verylow':temp}) 
        
        #rendah (10 to 30 naik, 30 to 50 turun), 
        if darah <= 10 or darah >= 50:
            darah_dict.update({'low':0})
        elif 10 < darah <= 30:
            temp = (darah - 10.0) / (30.0 - 10.0)
            darah_dict.update({'low':temp})
        elif 30 < darah <= 50:
            temp = (- (darah - 50.0) )/ (50.0 - 30.0)
            darah_dict.update({'low':temp}) 
        
        #sedang (40 to 60 naik, 60 to 80 turun), 
        if darah <= 40 or darah >= 80:
            darah_dict.update({'medium':0})
        elif 40 < darah <= 60:
            temp = (darah - 40.0) / (60.0 - 40.0)
            darah_dict.update({'medium':temp})
        elif 60 < darah <= 80:
            temp = (- (darah - 80.0) )/ (80.0 - 60.0)
            darah_dict.update({'medium':temp}) 
            
        #tinggi (70 to 90 naik, 90 to 110 turun), 
        if darah <= 70 or darah >= 110:
            darah_dict.update({'high':0})
        elif 70 < darah <= 90:
            temp = (darah - 70.0) / (90.0 - 70.0)
            darah_dict.update({'high':temp})
        elif 90 < darah <= 110:
            temp = (- (darah - 110.0) )/ (110.0 - 90.0)
            darah_dict.update({'high':temp}) 
        
        #sangat tinggi (100 to 120 naik)
        if darah <= 100 or darah >= 120:
            darah_dict.update({'veryhigh':0})
        elif 100 < darah <= 120:
            temp = (darah - 100.0) / (120.0 - 100.0)
            darah_dict.update({'veryhigh':temp})
        
        return darah_dict

    def find_x_clip(self, y, x1, y1, x2, y2):
        temp1 = (x2*y)-(x1*y)-(x2*y1)+(x1*y1)
        temp2 = temp1 / (y2-y1)
        x = temp2 + x1
        return x

    def find_y_clip(self, x, x1, y1, x2, y2):
        temp1 = (x*y2)-(x*y1)-(x1*y2)+(x1*y1)
        temp2 = temp1 / (x2-x1)
        y = temp2 + y1
        return y
        
    def find_max_dict(self, dicto):
        temp_v = 0
        temp_k = ''
        for k in dicto:
            if dicto[k] > temp_v:
                temp_v = dicto[k]
                temp_k = k
        
        return temp_k
    
    def action_inference(self, data_jarak, data_darah):
        action_dict = {}
        fallback_choice = []
        walk_choice = []
        attack_choice = []
        temp = 0

        # if darah = VERYLOW and jarak = NEAR  then aksi =  FALLBACK
        if data_darah['verylow'] and data_jarak['near'] :
            temp = min(data_darah['verylow'], data_jarak['near'])
            fallback_choice.append(temp)
            
        # if darah = LOW and jarak = NEAR  then aksi =  FALLBACK
        if data_darah['low'] and data_jarak['near'] :
            temp = min(data_darah['low'], data_jarak['near'])
            fallback_choice.append(temp)
            
        # if darah = MEDIUM and jarak = NEAR  then aksi =  WALK
        if data_darah['medium'] and data_jarak['near'] :
            temp = min(data_darah['medium'], data_jarak['near'])
            walk_choice.append(temp)
            
        # if darah = HIGH and jarak = NEAR  then aksi =  WALK
        if data_darah['high'] and data_jarak['near'] :
            temp = min(data_darah['high'], data_jarak['near'])
            walk_choice.append(temp)
        
        # if darah = VERYHIGH and jarak = NEAR  then aksi =  ATTACK
        if data_darah['veryhigh'] and data_jarak['near'] :
            temp = min(data_darah['veryhigh'], data_jarak['near'])
            attack_choice.append(temp)
            
        
        # if darah = VERYLOW and jarak = MEDIUM  then aksi =  FALLBACK
        if data_darah['verylow'] and data_jarak['medium'] :
            temp = min(data_darah['verylow'], data_jarak['medium'])
            fallback_choice.append(temp)
            
        # if darah = LOW and jarak = MEDIUM  then aksi =  WALK
        if data_darah['low'] and data_jarak['medium'] :
            temp = min(data_darah['low'], data_jarak['medium'])
            walk_choice.append(temp)
            
        # if darah = MEDIUM and jarak = MEDIUM  then aksi =  ATTACK
        if data_darah['medium'] and data_jarak['medium'] :
            temp = min(data_darah['medium'], data_jarak['medium'])
            attack_choice.append(temp)
            
        # if darah = HIGH and jarak = MEDIUM  then aksi =  ATTACK
        if data_darah['high'] and data_jarak['medium'] :
            temp = min(data_darah['high'], data_jarak['medium'])
            attack_choice.append(temp)
            
        # if darah = VERYHIGH and jarak = MEDIUM  then aksi =  ATTACK
        if data_darah['veryhigh'] and data_jarak['medium'] :
            temp = min(data_darah['veryhigh'], data_jarak['medium'])
            attack_choice.append(temp)
            
        
        # if darah = VERYLOW and jarak = FAR  then aksi =  FALLBACK
        if data_darah['verylow'] and data_jarak['far'] :
            temp = min(data_darah['verylow'], data_jarak['far'])
            fallback_choice.append(temp)
            
        # if darah = LOW and jarak = FAR  then aksi =  WALK
        if data_darah['low'] and data_jarak['far'] :
            temp = min(data_darah['low'], data_jarak['far'])
            walk_choice.append(temp)
            
        # if darah = MEDIUM and jarak = FAR  then aksi =  ATTACK
        if data_darah['medium'] and data_jarak['far'] :
            temp = min(data_darah['medium'], data_jarak['far'])
            attack_choice.append(temp)
            
        # if darah = HIGH and jarak = FAR  then aksi =  ATTACK
        if data_darah['high'] and data_jarak['far'] :
            temp = min(data_darah['high'], data_jarak['far'])
            attack_choice.append(temp)
            
        # if darah = VERYHIGH and jarak = FAR  then aksi =  ATTACK
        if data_darah['veryhigh'] and data_jarak['far'] :
            temp = min(data_darah['veryhigh'], data_jarak['far'])
            attack_choice.append(temp)
        
        
        # clipping
        if len(fallback_choice) != 0:
            action_dict.update({'fallback':max(fallback_choice)})
        else:
            action_dict.update({'fallback':0})
        if len(walk_choice) != 0:
            action_dict.update({'walk':max(walk_choice)})
        else:
            action_dict.update({'walk':0})
        if len(attack_choice) != 0:
            action_dict.update({'attack':max(attack_choice)})
        else:
            action_dict.update({'attack':0})
        
        print "action_dict : ", action_dict, '\n'
        
        # menentukan batas garis miring tiap fungsi keanggotaan setelah clipping
        # batas garing - 1
        garing_1 = self.find_x_clip(action_dict['fallback'], 0, 1, 40, 0)
        
        # batas garing - 2
        garing_2 = self.find_x_clip(action_dict['walk'], 20, 0, 40, 1)
        
        # batas garing - 3
        garing_3 = self.find_x_clip(action_dict['walk'], 40, 1, 80, 0)
        
        # batas garing - 4
        garing_4 = self.find_x_clip(action_dict['attack'], 70, 0, 100, 1)
        
        # menentukan daftar sample titik
        rand_point = []
        
        if action_dict['fallback'] != 0:
            rand_point += range(0, 41, random.randint(1, 11))
        if action_dict['walk'] != 0:
            rand_point += range(20, 81, random.randint(1, 11))
        if action_dict['attack'] != 0:
            rand_point += range(70, 101, random.randint(1, 11))
        
        
        # menentukan proyeksi x ke y untuk setiap sample titik
        #mundur (0 to 40 turun), 
        fallback_point = {}
        for point in rand_point:
            if point <= 0 or point >= 40:
                pass
            elif 0 <= point <= garing_1:
                temp_key = round(action_dict['fallback'], 2)
                if fallback_point.has_key(temp_key):
                    temp_lst = fallback_point.get(temp_key)
                    temp_lst.append(point)
                    fallback_point[temp_key] = temp_lst
                else:
                    fallback_point.update({temp_key:[point]})
            elif garing_1 < point <= 40:
                temp = round(self.find_y_clip(point, garing_1, action_dict['fallback'], 40, 0), 2)
                if fallback_point.has_key(temp):
                    temp_lst = fallback_point.get(temp)
                    temp_lst.append(point)
                    fallback_point[temp] = temp_lst
                else:
                    fallback_point.update({temp:[point]})
        
              
        #kabur (20 to 40 naik, 40 to 80 turun), 
        walk_point = {}
        for point in rand_point:
            if point <= 20 or point >= 80:
                pass
            elif 20 <= point < garing_2:
                temp = round(self.find_y_clip(point, 20, 0, garing_2, action_dict['walk']), 2)
                if walk_point.has_key(temp):
                    temp_lst = walk_point.get(temp)
                    temp_lst.append(point)
                    walk_point[temp] = temp_lst
                else:
                    walk_point.update({temp:[point]})
            elif garing_2 <= point <= garing_3:
                temp_key = round(action_dict['walk'], 2)
                if walk_point.has_key(temp_key):
                    temp_lst = walk_point.get(temp_key)
                    temp_lst.append(point)
                    walk_point[temp_key] = temp_lst
                else:
                    walk_point.update({temp_key:[point]})
            elif garing_3 < point <= 80:
                temp = round(self.find_y_clip(point, garing_3, action_dict['walk'], 80, 0), 2)
                if walk_point.has_key(temp):
                    temp_lst = walk_point.get(temp)
                    temp_lst.append(point)
                    walk_point[temp] = temp_lst
                else:
                    walk_point.update({temp:[point]})
        
        
        #serang (70 to 100 naik)
        attack_point = {}
        
        for point in rand_point:
            if point <= 70 or point >= 100:
                pass
            elif 70 <= point < garing_4:
                temp = round(self.find_y_clip(point, 70, 0, garing_4, action_dict['attack']), 2)
                if attack_point.has_key(temp):
                    temp_lst = attack_point.get(temp)
                    temp_lst.append(point)
                    attack_point[temp] = temp_lst
                else:
                    attack_point.update({temp:[point]})
            elif garing_4 <= point <= 100:
                temp_key = round(action_dict['attack'], 2)
                if attack_point.has_key(temp_key):
                    temp_lst = attack_point.get(temp_key)
                    temp_lst.append(point)
                    attack_point[temp_key] = temp_lst
                else:
                    attack_point.update({temp_key:[point]})
                
        # menampilkan informasi setiap data fuzzy
        
        print "random point : ", rand_point, '\n'
        print "fallback point : ", fallback_point, '\n'
        print "walk point : ", walk_point, '\n'
        print "attack point : ", attack_point, '\n'
        
        # menjumlahkan setiap sample titik dan dikalikan dengan bobot
        # menjumlahkan setiap pembagi bobot berdasarkan banyak titik
        temp1 = 0
        temp2 = 1
        
        if len(fallback_point) != 0 or len(walk_point) != 0 or len(attack_point) != 0:
            temp2 = 0
        else:
            temp2 = 1
            
        for key in fallback_point:
            temp1 += (sum(fallback_point[key]) * key)
            temp2 += (len(fallback_point[key]) * key)
        
        for key in walk_point:
            temp1 += (sum(walk_point[key]) * key)
            temp2 += (len(walk_point[key]) * key)
        
        for key in attack_point:
            temp1 += (sum(attack_point[key]) * key)
            temp2 += (len(attack_point[key]) * key)
        
        output = round(temp1 / temp2)
        
        
        action = ''
        if 0 <= output <= garing_1:
            action = 'fallback'
        elif garing_1 < output <= 40:
            action = self.find_max_dict(action_dict)
        if 20 <= output < garing_2:
            action = self.find_max_dict(action_dict)
        elif garing_2 <= output <= garing_3:
            action= 'walk'
        elif garing_3 < output <= 80:
            action = self.find_max_dict(action_dict)
        if 70 <= output < garing_4:
            action = self.find_max_dict(action_dict)
        elif garing_4 <= output <= 100:
            action = 'attack'
        print output
        return action

# parameter input dari luar sistem
jarak = 300
darah = 100

print "jarak yang diketahui : ", jarak
print "darah yang diketahui : ", darah

fuzzengine = FuzzyRTSEngine(jarak, darah)

# fuzzyfikasi
raw_data_jarak = fuzzengine.jarak_membership(jarak)
print 'data_jarak : ', raw_data_jarak

raw_data_darah = fuzzengine.darah_membership(darah)
print 'data_darah : ', raw_data_darah

action = fuzzengine.action_inference(raw_data_jarak, raw_data_darah)
print "action : ", action

"""
# inferensi
while True:
    time.sleep(0.4)
    os.system('clear')
    action = fuzzengine.action_inference(raw_data_jarak, raw_data_darah)
    print "action : ", action
"""
