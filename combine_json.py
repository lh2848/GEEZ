import json


data1 = json.load(open('rap_results.json'))
data2 = json.load(open('rap_results2.json'))


all_data = data1 + data2

json.dump(all_data,open('rap_results_all.json','w'),indent=2)
