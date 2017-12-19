import json, requests
from time import sleep


#load["LOCdictionary_one.json"]
# we want to load the json file to work with it
data = json.load(open('LOCdictionary_one.json'))

# make a new list for our results
new_list = []

for record in data:

	# if "genre_tag" in data(record) = "Rap (Music)"
	# if "format" in data(record) = "sound disc"

	# see if the tag we want is in the genre tag list and sound disc in the format
	if "Rap (Music)" in record['genre_tag']:

		if "sound disc" in record['format']:

			# if it has a title and author
			if record['artist245'] != None and record['title'] != None:
					
				# lets clean up the the artist value to remove periods etc
				# save it into a new variable
				artist = record['artist245']

				# remove periods
				artist = artist.replace('.','')

				artist = artist.replace('[','')

				artist = artist.replace(']','')

				artist = artist.replace('written and performed by','')

				artist = artist.replace('\u0301','')

				artist = artist.replace('\u0301x','')

				artist = artist.replace('+','')

				artist = artist.replace(';','')

				artist = artist.replace('all lyrics by','')

				artist = artist.replace('performed by','')


				# copy over the title to make it eaiser for us
				album = record['title']

				album = album.replace('.','')


				# request the API

				print("Got", artist, album)

				payload = {"method": "album.getTopTags", "artist": artist, "album": album, "api_key": "5b89e0e699ac209fb9d130258d7570f8", "format": "json"}

				r = requests.get('http://ws.audioscrobbler.com/2.0', params=payload)
				
				# turn the request of the request into data
				# print(r.text)

				results = json.loads(r.text)

				# save the results back into the file we loaded at the start
				record['last_fm'] = results

				# and then add it to our new list
				new_list.append(record)


				# save the new list to disk as json
				# we should do this at the very end, but lets do it each loop incase the script timesout with the APi we won't loose everything
				json.dump(new_list,open('rap_results.json','w'),indent=2)

				# stop the execution for a fraction of a second so we don't overload the API
				sleep(0.1)


# payload = {"method": "album.getTopTags", "artist": "artist245", "album": "title", "api_key": 5b89e0e699ac209fb9d130258d7570f8, "format": json}
# r = requests.get('http://ws.audioscrobbler.com/2.0', params=payload)
# print(r.text)

# data = json.loads

