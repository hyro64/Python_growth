class Restaurant():
	"""Stores a model of a restaurant"""
	
	def __init__(self,name,cuisine):
		"""Intialize a name and the cuisine of the restaurant"""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
		
	def describe_restaurant(self):
		"""Describes the resturant and the cuisine offered"""
		print(self.name.title() + " serves " + self.cuisine + " type of"
		+ " food.")
		
	def open_restaurant(self):
		"""Displays a message saying the restaurant is open"""
		print(self.name.title()+ " is open!")
		
	def display_served(self):
		"""Reads the number of served patraons"""
		print(self.name + " has served " + str(self.number_served) +
				" customers.")
	def set_number_served(self,customers):
		"""Reads the number of served patraons"""
		self.number_served += customers
		print(self.name + " has served " + str(self.number_served) +
				" customers.")
	def increment_number_served(self,customers):
		"""Reads the number of served patraons"""
		self.number_served += customers
		print(self.name + " has served " + str(self.number_served) +
				" customers.")
		
restaurant = Restaurant("stubens", "american")

print("This restaurant's name is " + restaurant.name.title() + ".")
print("It usually serves " +restaurant.cuisine.title() + ".")

restaurant.describe_restaurant() 
restaurant.open_restaurant()
restaurant.display_served()
restaurant.set_number_served(86)
restaurant.increment_number_served(86)
