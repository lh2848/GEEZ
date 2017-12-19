import json

data = json.load(open('rap_results.json'))

bad_tags = ["albums I own",
			"1001 Albums You Must Hear Before You Die",
			"favourite albums"
			"Dude Chopped",
			"Rap-A-Lot",
			"my collection great 150 albumz of rap",
    		"real life rhymes",
   			"lydia lunch merkliste",
    		"prt",
    		"educate yourself",
    		"lyrics to learn from",
    		"albums I own",
		    "best album",
		    "tha eastsidaz",
		    "kaudogg",
		    "pih-poh",
		    "my fave break up album",	  
		    "purple haze",		    
		    "codeine lein",
		    "nigga please",		    
		    "opposite of h20",	  
		    "hhc 95-05 top 100",	  
		    "Back in the day Hip Hop",	   
		    "hot to def",	   
		    "v",
		    "sole",
		    "boxofmusic",	  
		    "favorites",	   
		    "Listen carefully",
		    "fun to skateboard to",
		    "underground fun",
		    "excellent lyricism",
		    "check the wordplay"
		    "favourite albums",
		    "High School",
		    "Mase",
		    "top25",
		    "old faves",
		    "HS-College",	  
		    "hell",
		    "good albums",
		    "Beasts From the East",
		    "Real hip-hop",
		    "hiphop classic albums",
		    "A Good 1",
		    "work songs",
		    "real hip hop",
		    "if only everyone knew",	   
		    "one hit wonder",
		    "various artists",
		    "Totec Radio",
		    "where is my bong",
		    "peerless",	    
		    "chilled",	   
		    "luni toonz",
		    "spin",  
		    "registret",
		    "old tapes",    
		    "family",
		    "Ohana",
		    "seadawgg",   
		    "1001 Albums You Must Hear Before You Die",   
		    "Classic Era Rap",
		    "leapsandbounds tapecollection",
		    "BIG TYME",   
		    "favorite albums",  
		    "weekend-club",
		    "The Guardian list of 1000 albums to hear before you die"	   
		    "only listen",    
		    "albums i have on mp3",  
		    "guilty pleasure",    
		    "boom or bust",  
		    "puma is the brand",
		    "bass machine supreme",
		    "808 boom",
		    "kangol rocks"
		    "My Dope Albums",
		    "My vinyl",
		    "favs",
		    "4nas",
		    "nadh",
		    "vemu",
		    "Back In The Day - Hip Hop Jams",	 
		    "leapsand80sAlbums",
		    "my fav frm my teens",		  
		    "POTTERY WORDZ",		    
		    "I love do we have a chance",		 
		    "milla best",		  
		    "Essential Albums",
		    "ok track",		   
		    "buy",
		    "This is so bad it makes me wanna shove an emo hedgehog up my ass and masturbate to pictures of bisexual gay pinguins but it is still somehow better then Michael Angelo Batio",		 
		    "jbtv recommendation",		   
		    "where are my headphones",
		    "beats for days",		  
		    "Keith Murray",
		    "k",
		    "b",
		    "Tenoxsax Radio Mix",
		    "blak",
		    "hot rap music",	  
		    "rich finck",	  
		    "too short cocktails",
		    "to short cocktals",	 
		    "Dirty 3rd",	   
		    "Ghetto Bloods",	    
		    "slimm calhoun",
		    "dungeon family",
		    "top cd",
		    "sigh another album from my not dissipated enough youth",
		    "one of my favorites",
		    "707",
		    "rehab",
		    "ghetty",
		    "quirky",
		    "whimsical",
		    "Chillosophy",
		    "Freewheeling",
		    "fun",
		    "best",
		    "silly",
		    "albums",
		    "witty",		    
		    "own",		   
		    "amiable/good-natured",
		    "luzik",
		    "Mes CD",
		    "divercibelz",
		    "true school",		    
		    "TIME IS MONEY LP",		    
		    "pifou station",		    
		    "kid24",
		    "yay area"
]

Hundred_tags = []


for album_info in data:


	# make a list to store our good tags
	good_tags = []

	# does it have last fm tags?
	if "toptags" in album_info['last_fm']:
		# loop through each tag
		for tag in album_info['last_fm']['toptags']['tag']:
			if tag['name'] not in bad_tags:
				good_tags.append(tag)

				# ?????
				if tag['count'] == 100 and tag['name'] not in Hundred_tags:
					Hundred_tags.append(tag['name'])


print (json.dumps (Hundred_tags, indent = 4))

json.dump(Hundred_tags,open('genre_list.json','w'))





	# you can now loop through good_tags to do what you want with them
	