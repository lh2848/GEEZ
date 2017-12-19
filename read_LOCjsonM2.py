import json

data = json.load(open('rap_results2.json'))

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
		    "Anika Euin",
		    "nice nite",
		    "classic",
		    "Dope",
		    "SilentAngel",
		    "my shit",
		    "Diary of a sinner",
		    "me femme you hard butch daddy stone tg FtM  but like this group",
		    "check the wordplay",

		    "real 80s",
		    "KKN",
		    "mklk",
		    "tlc",
		    "love action",
		    "lights low",
		   
		    "allmusicp",
		  
		    "cool",
		    "got on vinyl",
		   
		    "slow jam",
		  
		    "detroit",
		    "Progressive metal",
		  
		    "heavy metal",
		    "metal",
		    "alternative metal",
		    "Nu Metal",
		 
		    "REAL HIP HOP MA MAN",
		    
		    "Rap-A-Lot Records",
		  
		    "Haystak the natural",
		    "favourite albums",
		    "mayara",
		    "dope house",
		    "P Troy",
		    "golden age",
		    "Good Hip-Hop",  
		    "top 40",
		    "djtopp",
		    "friends",
		    "dirty dime music",
		    "10-A-Cee music",
		    "missionary flows",
		    "insane clown posse",
		    "three 6 mafia",
		    "three six mafia",
		    "ICP",
		    "Gangsta Boo",
		    "Twiztid",
		    "three 6",
		  
		    "When Tha Smoke Clears",
		    "Ants fav",
		    "fahad",
		    "JaydPeezy",
		    "sought",
		    "sexrap",
		    "old school",
		    "trick daddy-thug holiday",
		    "2003",
		    "mine",
		    "thats my shizznit",
		    "bow wow",
		 
		    "Brutal Death Metal",
		    "brutal deathcore",
		    "Altar of the Metal Gods",
		    "Altar of the Metal Gods Sludge",
		    "Altar of the Metal Gods Melodic Metal",
		    "Altar of the Metal Gods Neo-Classical Metal",
		    "Altar of the Metal Gods Death Metal",
		    "Altar of the Metal Gods Black Metal",
		    "Altar of the Metal Gods Thrash Metal",
		    "Altar of the Metal Gods Folk Metal",
		    "Altar of the Metal Gods Ambient Metal",
		    "Altar of the Metal Gods NWOBHM",
		    "Altar of the Metal Gods Doom Metal",
		    "Altar of the Metal Gods Pagan Metal",
		    "Altar of the Metal Gods Technical Death Metal",
		    "Altar of the Metal Gods Symphonic Metal",
		    "Altar of the Metal Gods Epic Metal",
		    "Altar of the Metal Gods Hardcore",
		    "Altar of the Metal Gods Power Metal",
		    "Altar of the Metal Gods Industrial Metal",
		    "Altar of the Metal Gods Drone Metal",

		    "allmusicm",
		    "allmusick",

		    "Monakitty432",
		    "rsyniklaced",
		    "deviliscious432",
		    "cmurder",
		    "nolimit",
		    "trapedincrime",
		    "phx602phx",
		    
		    "Regrets",
		    "100 things for now",
		    "rhymes that make me laugh",
		 
		    "singles i own",
		    "carey",
		    "Marajka",
		   
		    "bootcamp",
		   
		    "da Unbreakables",
		 
		    "CD",

		    "sent from daloooon my baby",
		    "LBM",
		    "Mark Ronson",
		    "allmusicr",
		    "morr music",
		  
		    "legit",
		  
		    "Justin Broadrick",
		 
		    "imp",
		  
		    "vico c",
		    "Only God Can Judge Me  A release by Master P",

		    "on the grind",
		    
		    "WC",
		  
		    "Loved this album back in the days",
		    "tame one",

		    "1",

		    "weightlifting music",
		    "rolling stone top 50 albums 2003",

		    "albums i once owned but decided were not worth my time",

		    "Anika Euin",
		  
		    "amazing",
		  
		    "southern devils",
		 
		    "gucci mane",
		   
		    "puerto rican hiphop at its finest",
		  
		    "Baby Bash",
		    "chillaut",
		   
		    "Love",

		    "Ying Yang twins",

		    "Bell Biv DevVoe",

		    "wu-tang"

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

json.dump(Hundred_tags,open('genre_list2.json','w'))




	# you can now loop through good_tags to do what you want with them