def print_models(unprinted_designs):
	"""
	Simulate printing each design, until none are left.
	move each desing to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#Simulate crdeating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)
	show_completed_models(completed_models)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
