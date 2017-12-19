favorite_languages = {
	'jen':'python',
	'sarah':"c",
	'edward':"ruby",
	'phil':"python",
	}

friends = ['jesse','sarah','katie']

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + "." + "Thank you for taking the poll.")
for friends in favorite_languages.keys():
	print(friends.title() +"Take the poll") 
