class User(object):	#object is used to make sure that python can use super
	"""Stores user related information"""
	def __init__(self,first_name,last_name,DOB,location,gender):
		""""""
		self.first_name = first_name
		self.last_name = last_name
		self.DOB = DOB
		self.location = location
		self.gender = gender
		self.login_attempts = 0
########################################################################
	def describe_user(self):
		"""Prints user infomation"""
		print("User info: ")
		print("\t-" + self.first_name.title())
		print("\t-" + self.last_name.title())
		print("\t-" + self.DOB)
		print("\t-" + self.location.title())
		print("\t-" + self.gender.title())
########################################################################
	def greet_user(self):
		"""Displays a personalized message for the user"""
		print("Hello " + self.first_name.title() + ". How are you?")
########################################################################
	def increment_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts += 1
		print("You have attempted to login " + str(self.login_attempts)+
			" time(s).")
########################################################################
	def reset_login_attempts(self):
		"""Increases the login attempts by one"""
		self.login_attempts = 0
########################################################################

class Admin(User): #This class is a model for an admin
	def __init__(self,first_name,last_name,DOB,location,gender):
		"""Admin,self above are used to make sure super can be used"""
		super(Admin,self).__init__(first_name,last_name,DOB,location,gender)
		self.privileges = Privileges() 
########################################################################			
class Privileges(): #This class show the privilages of a user
	"""A simple attempt to model privilages for a user."""
	def __init__(self):
		self.Privalages = ["can add post",
							"can delete post",
							"can ban users",
							]
	def show_privileges(self):
		"""Show the privalages that the user can use."""
		print("The above user: ")
		while self.Privalages:
			current_Privalages = self.Privalages.pop()
			print("\t    " + current_Privalages + ".")
########################################################################			
admin = Admin("kate",
			"mcDonald",
			"08.12.1980",
			"lakewood",
			"female"
			)
########################################################################
"""The class below calls the class methods described above."""
admin.describe_user()
admin.privileges.show_privileges()
admin.greet_user()
