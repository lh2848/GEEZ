all_data = []
import json
from pymarc import MARCReader
with open('Music.2014.part01.utf8', 'rb') as fh:
	reader = MARCReader(fh)
	for record in reader:
		print('-----------------')
		# print(record.title())

		field_data = {"artist245": False,
					"artist700": False,
					"title": False,
					"publication date": False,
					"format": False,
					"format2": False,
					"genre_tag":[],
					"note_field":[]}

		# print(record['650'])
		# print(record['655']['a'])

		# if "650" in record:
		# 	if "a" in record['650']:

		# 		print(record['650']['a'])
		for f650 in record.get_fields('650'):
			# print(f650['a'])
			field_data ["genre_tag"].append(f650['a'])

		for f655 in record.get_fields('655'):
			# print(f650['a'])
			field_data ["genre_tag"].append(f655['a'])

		for f500 in record.get_fields('500'):
			# print(f650['a'])
			field_data ["note_field"].append(f500['a'])

		# check for publication date greater than 2000
		for f260 in record.get_fields('260'):
			print(f260['c'])

			field_data ["publication date"] = f260['c']

		for f245 in record.get_fields('245'):
			print(f245['a'])

			field_data ["title"] = f245['a']
			field_data ["artist245"] = f245['c']

		for f700 in record.get_fields('700'):
			print(f700['a'])

			field_data ["title"] = f700['a']
			field_data ["artist700"] = f700['c']

		for f300 in record.get_fields('300'):
			print(f300['a'])

			field_data ["format"] = f300['a']
			field_data ["format2"] = f300['c']


		all_data.append(field_data)

json.dump(all_data,open('LOCdictionary_one.json','w'),indent=4)
		# print(field_data)

		# check for format CD
		# for f300 in record.get_fields('300'):

		# store in dictionary 