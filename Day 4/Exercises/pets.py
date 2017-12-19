pets ={
	'argus':{
		'owner': "katie",
		'species': "dog",
		'color':"golden yellow",
		'breed':"chow mix",
		},
	'chell':{
		'owner': "tabitha",
		'species': "dog",
		'color':"black/white",
		'breed':"beagle mix",
		},
	'lily':{
		'owner': "chris",
		'species': "dog",
		'color':"black",
		'breed':"cocker spanish/ english spaniel",
		},
	} 
	
for pet, pet_info in pets.items():
	print("\nName: "+pet)
	for category in pet_info:
		current = pet_info[category]
		print("\t" + category.title() +":"+current.title())
