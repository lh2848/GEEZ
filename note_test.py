import json, requests
from time import sleep


#load["LOCdictionary_one.json"]
# we want to load the json file to work with it
data = json.load(open('LOCdictionary_two.json'))

# make a new list for our results
new_list = []

for record in data:

	# if "genre_tag" in data(record) = "Rap (Music)"
	# if "format" in data(record) = "sound disc"

	# see if the tag we want is in the genre tag list and sound disc in the format
	if "Rap (Music)" in record['genre_tag']:

		if record['format'] != False:

			if "sound disc" in record['format']:

				for note in record['note_field']:
					if "hip" in note and "hop" in note:
						print(note)


# payload = {"method": "album.getTopTags", "artist": "artist245", "album": "title", "api_key": 5b89e0e699ac209fb9d130258d7570f8, "format": json}
# r = requests.get('http://ws.audioscrobbler.com/2.0', params=payload)
# print(r.text)

# data = json.loads

