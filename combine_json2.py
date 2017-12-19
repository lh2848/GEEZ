import json


data1 = json.load(open('genre_list.json'))
data2 = json.load(open('genre_list2.json'))


all_data = data1 + data2

json.dump(all_data,open('topgenres.json','w'),indent=2)
