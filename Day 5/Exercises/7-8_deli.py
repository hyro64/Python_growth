sandwichOrders = [
	'CheeseSteak',
	'Pastrami',
	'Club Sandwhich',
	'Hamburger',
	'Pastrami',
	'French Dip',
	'Banhmi',
	'Italian beef',
	'Pastrami on rye',
	'Pastrami',
	]
finishedSandwiches = []

while sandwichOrders:
	workingOrder = sandwichOrders.pop()
	finishedSandwiches.append(workingOrder)
	print("I made your " + workingOrder)
print("\n----Completed Orders----\n")
for sandwich in finishedSandwiches:
	print("\t" + sandwich)
	
