def build_profile(first,last,**user_info):
	"""Build a dictionary containing everything we know about th user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('Hyro', '64',
							location = 'aurora',
							field = 'Student',
							major = 'computer science',)
print(user_profile) 