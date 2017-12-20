persons = {
	'person1':{
		'first name':"katie",
		'last name': "meow",
		'age': 32,
		'city': "thorton", 
		},
	'person2' : {
		'first name':"kacy",
		'last name': "curd",
		'age': "n/a",
		'city': "yuma", 
		},
	'person3' : {
		'first name':"Amanda",
		'last name': "n/a",
		'age': "23",
		'city': "aurora", 
		},
	}

for person, personInfo in sorted(persons.items()):
	print("\nFirst Name: " + personInfo['first name'].title())
	print("\tLast Name: "+personInfo['last name'].title())
	print("\tAge: "+ str(personInfo['age']))
	print("\tCity: "+personInfo['city'].title())
	
	
	
