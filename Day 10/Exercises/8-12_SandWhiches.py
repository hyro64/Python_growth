def make_Sandwhich(size,*toppings):
	"""Summarize the Sanwhich we are about to make."""
	print("\nMaking a " + str(size) +
		" with the following toppings:")
	for topping in toppings:
		print("- " + topping)
		
make_Sandwhich('large', 'mushrooms', 'green peppers', 'extra cheese')
make_Sandwhich('medium', 'lettuce', 'tomatos', 'bacon','Cheese')
make_Sandwhich('small', 'onions', 'ham', 'extra cheese')
