def describe_city(city = 'denver', country = 'united states of america'):
	"""Ask for a city and a country then print the information"""
	print(city.title() + " is in "+ country.title() + ".")

describe_city()	
describe_city("reykjavik", "iceland")
describe_city("barcelona","spain")
describe_city("hong kong","china")
