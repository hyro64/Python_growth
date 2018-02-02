def city_country(city, country):
	formattedCity = city.title() +", " + country.title()
	return formattedCity	
	
while True:
	city = input("Please enter a city: \n(Enter 'q' to quit)\n")
	if city =='q':
		break
		
	country = input("Please enter a country: \n(Enter 'q' to quit)\n")
	if country =='q':
		break

	print(city_country(city, country))
	
	
