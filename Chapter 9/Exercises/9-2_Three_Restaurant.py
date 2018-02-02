class Restaurant():
	"""Stores a model of a restaurant"""
	
	def __init__(self,name,cuisine):
		"""Intialize a name and the cuisine of the restaurant"""
		self.name = name
		self.cuisine = cuisine
		
	def describe_restaurant(self):
		"""Describes the resturant and the cuisine offered"""
		print(self.name.title() + " serves " + self.cuisine + " type of"
		+ " food.")
		
	def open_restaurant(self):
		"""Displays a message saying the restaurant is open"""
		print(self.name.title()+ " is open!")
		
restaurant = Restaurant("stubens", "american")
restaurant2 = Restaurant("Dae gae", "korean")
restaurant3 = Restaurant("the proten house", "healthy")

print("This restaurant's name is " + restaurant.name.title() + ".")
print("It usually serves " +restaurant.cuisine.title() + ".")

restaurant.describe_restaurant() 
restaurant.open_restaurant()

restaurant2.describe_restaurant()  

restaurant3.describe_restaurant() 
