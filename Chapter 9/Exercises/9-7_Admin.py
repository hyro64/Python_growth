class User(object):	#object is used to make sure that python can use super
	"""
	Stores user related information
	"""
	
	def __init__(self,first_name,last_name,DOB,location,gender):
		""""""
		self.first_name = first_name
		self.last_name = last_name
		self.DOB = DOB
		self.location = location
		self.gender = gender
		self.login_attempts = 0
#############################_Method_END_###############################
	def describe_user(self):
		"""Prints user infomation"""
		
		print("User info: ")
		print("\t-" + self.first_name.title())
		print("\t-" + self.last_name.title())
		print("\t-" + self.DOB)
		print("\t-" + self.location.title())
		print("\t-" + self.gender.title())
#############################_Method_END_###############################
	def greet_user(self):
		"""Displays a personalized message for the user"""
		
		print("Hello " + self.first_name.title() + ". How are you?")
#############################_Method_END_###############################
	def increment_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts += 1
		print("You have attempted to login " + str(self.login_attempts)+
			" time(s).")
#############################_Method_END_###############################
	def reset_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts = 0
##############################_CLASS_END_###############################

class Admin(User):
	def __init__(self,first_name,last_name,DOB,location,gender):
		super(Admin,self).__init__(first_name,last_name,DOB,location,gender)
		"""Admin,self above are used to make sure super can be used"""
		self.Privalages = ["can add post",
							"can delete post",
							"can ban users",
							]
	def show_privalages(self):
		"""Show the privalages that the user can use."""
		self.greet_user()
		print("The above user: ")
		while self.Privalages:
			current_Privalages = self.Privalages.pop()
			print("\t\t" + current_Privalages + ".")
##############################_CLASS_END_###############################				
admin1 = Admin("kate",
			"mcDonald",
			"08.12.1980",
			"lakewood",
			"female"
			)
admin1.show_privalages()
admin1.describe_user()
