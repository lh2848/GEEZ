from pymarc import MARCReader
with open('Music.2014.part01.utf8', 'rb') as fh:
	reader = MARCReader(fh)
	for record in reader:
		print('-----------------')
		print(record.title())

		# print(record['650'])
		# print(record['655']['a'])

		# if "650" in record:
		# 	if "a" in record['650']:

		# 		print(record['650']['a'])
		for f650 in record.get_fields('650'):
			print(f650['a'])