class User():
	"""
	Stores user related information
	"""
	
	def __init__(self,first_name,last_name,DOB,location,gender):
		self.first_name = first_name
		self.last_name = last_name
		self.DOB = DOB
		self.location = location
		self.gender = gender
		
	def describe_user(self):
		"""
		Prints user infomation
		"""
		print("User info: ")
		print("\t-" + self.first_name.title())
		print("\t-" + self.last_name.title())
		print("\t-" + self.DOB)
		print("\t-" + self.location.title())
		print("\t-" + self.gender.title())
		
	def greet_user(self):
		"""
		Displays a personalized message for the user
		"""
		print("Hello " + self.first_name.title() + ". How are you?")
			
user1 = User("clyde",
			"Millano",
			"10.12.1980",
			"colorado springs",
			"male"
			)
user2 = User("kate",
			"mcDonald",
			"08.12.1980",
			"lakewood",
			"female"
			)
user3 = User("panda",
			"bear",
			"08.12.1990",
			"arvada",
			"female"
			)

user1.describe_user()
print("\n")
user1.greet_user()
print("\n")
user2.describe_user()
print("\n")
user2.greet_user()
print("\n")
user3.describe_user()
print("\n")
user3.greet_user()

