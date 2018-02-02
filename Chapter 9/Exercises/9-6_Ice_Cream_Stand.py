class Restaurant():
	"""Stores a model of a restaurant"""
	def __init__(self,name,cuisine,customers):
		"""Intialize a name and the cuisine of the restaurant"""
		self.name = name
		self.cuisine = cuisine
		self.number_served = customers

########################################################################		
	
	def describe_restaurant(self):
		"""Describes the resturant and the cuisine offered"""
		long_name = self.name.title() + " serves " + self.cuisine + " type of food."
		return long_name

########################################################################		
	
	def open_restaurant(self):
		"""Displays a message saying the restaurant is open"""
		print(self.name.title()+ " is open!")

########################################################################		
	
	def display_served(self):
		"""Reads the number of served patraons"""
		print(self.name + " has served " + str(self.number_served) +
				" customers.")

########################################################################				
	
	def set_number_served(self,customers):
		"""Reads the number of served patraons"""
		self.number_served += customers
		print(self.name + " has served " + str(self.number_served) +
				" customers.")

########################################################################
	
	def increment_number_served(self,customers):
		"""Reads the number of served patraons"""
		self.number_served += customers
		print(self.name + " has served " + str(self.number_served) +
				" customers.")

########################################################################		

class IceCreamStand(Restaurant):
	""""""
	def __init__(self,name,cuisine,customers):
		 """Initialize attributes fo th parent class."""
		 super().__init__()
		 self.flavors = ["vanilla", 
						"chocolate",
						"pistacio",
						]

########################################################################			 

	def describe_flavors(self):
		"""Display the flavors"""
		while self.flavors:
			current_flavor = self.flavors.pop()
			print("They have " + current_flavor.title() + ".")

########################################################################
myRestaurant1 = Restaurant("little man's", "ice cream",0)	
myRestaurant = IceCreamStand("little man's", "ice cream",0)
myRestaurant.describe_flavors()
print(myRestaurant1.describe_restaurant())


"""
restaurant.describe_restaurant() 
restaurant.open_restaurant()
restaurant.display_served()
restaurant.set_number_served(86)
restaurant.increment_number_served(86)
"""

#restaurant.IceCreamStand.describe_flavors()
