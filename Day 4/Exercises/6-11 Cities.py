cities = {
	'denver': {
		'country':"usa",
		'population':"682,545",
		'fact':"5280 ft above sea level.",
		},
	'hong kong' : {
		'country':"china",
		'population':"7.347 million ",
		'fact':"Hong Kong means Fragrant Harbor.",
		},
	'barcelona':{
		'country':"spain",
		'population':"1.609 million",
		'fact': "second largest city in spain.",
		},
	'chihuahua':{
		'country':"mexico",
		'population':"809,232",
		'fact':"Chihuahua's Copper Canyon is at least 7x larger than the Grand Canyon.",
		}
	}
for city, city_info in cities.items():
	print(city.title())
	for category,facts in city_info.items():
		print("\t"+category.title())
		print("\t\t"+facts.title())
