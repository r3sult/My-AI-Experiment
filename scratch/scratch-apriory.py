# menentukan barang yang dibeli
bought_item = {
                'T1': ['Mango','Mango','Mango', 'Onion', 'Nintendo', 'Key-chain', 'Eggs', 'Yo-yo'],
                'T2': ['Doll', 'Onion', 'Nintendo', 'Key-chain', 'Eggs', 'Yo-yo'],
                'T3': ['Mango', 'Apple', 'Key-chain', 'Eggs'],
                'T4': ['Mango', 'Umbrella', 'Corn', 'Key-chain', 'Yo-yo'],
                'T5': ['Corn', 'Onion', 'Onion', 'Key-chain', 'Ice-cream', 'Eggs'],
            }

# menghitung banyaknya jenis barang yang ada di tiap transaksi
amount_item_per_transaction = {}

for items in bought_item:
    print "processing ", items, "...."
    bought_item_set = list(set(bought_item[items]))
    for item in bought_item_set:
        if item not in amount_item_per_transaction:
            # periksa apakah item sudah ada di amount_item_per_transaction
            amount_item_per_transaction.update({item:1})
        elif item in amount_item_per_transaction:
            # periksa apakah item sudah dihitung
            temp_amount = amount_item_per_transaction[item]
            amount_item_per_transaction[item] = temp_amount + 1
             
print "\namount item per transaction : \n", amount_item_per_transaction, "\n"

# mengeliminasi jenis transaksi yang kurang dari 3
minimum_transaction = 3
temp_dict = dict(amount_item_per_transaction)
for item in temp_dict:
    if amount_item_per_transaction[item] < minimum_transaction:
        del(amount_item_per_transaction[item])

print "\namount item per transaction above 3 transaction : \n", amount_item_per_transaction, "\n"

# membentuk pasangan item dari suatu transaksi
temp_dict = dict(amount_item_per_transaction)
amount_item_per_transaction_combined_1 = {}
i = 1
for items in amount_item_per_transaction:
    print "combinantion -  ", items
    for item in temp_dict:
        if items != item:
            print items, " - ", item
            temp_item_key = "combination%d" % (i)
            temp_item_dict = {'item':[items, item], 'amount':0}
            amount_item_per_transaction_combined_1[temp_item_key] = temp_item_dict
            i += 1
    del(temp_dict[items])


# menghitung banyaknya keberadaan pasangan di tiap transaksi
for item in amount_item_per_transaction_combined_1:
    for bought_set in bought_item:
        i = 0
        for combined_item_1 in amount_item_per_transaction_combined_1[item]['item']:
            if combined_item_1 in bought_item[bought_set]:
                i += 1
        if i == 2:
            amount_item_per_transaction_combined_1[item]['amount'] += 1
        
print "amount_item_per_transaction_combined_1 : ", amount_item_per_transaction_combined_1


