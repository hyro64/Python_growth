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
		self.login_attempts = 0
		
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
	
	def increment_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts += 1
		print("You have attempted to login " + str(self.login_attempts)+
			" time(s).")
			
	def reset_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts = 0
		
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

class Admin(User):
	def __init__(self,first_name,last_name,DOB,location,gender):
		super().__init__(first_name,last_name,DOB,location,gender)
		self.Privalages = ["can add post",
							"can delete post",
							"can ban users",
							]
	def show_privalages(self):
		"""Show the privalages taht the user can use."""
		self.greet_user()
		print("The above user: ")
		while self.Privalages:
			current_Privalages = self.Privalages.pop()
			print("\t\t"+ current_Privalages + ".")
			
admin1 = Admin("Larold",
				"Boria",
				"01.26.1996",
				"Dover",
				"Male",
				)

admin1.show_privalages()				
admin1.describe_user()

"""			
user1.describe_user()
print("\n")
user1.greet_user()
print("\n")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()
user2.describe_user()
print("\n")
user2.greet_user()
print("\n")
user3.describe_user()
print("\n")
user3.greet_user()
"""
