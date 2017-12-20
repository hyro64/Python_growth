print("\n------->The deli has run out of pastrami<------\n")

sandwichOrders = [
	'CheeseSteak',
	'Pastrami',
	'Club Sandwhich',
	'Hamburger',
	'Pastrami',
	'French Dip',
	'Banhmi',
	'Italian beef',
	'Pastrami',
	'Pastrami',
	]
finishedSandwiches = []

while 'Pastrami' in sandwichOrders:
	sandwichOrders.remove('Pastrami')

while sandwichOrders:
	workingOrder = sandwichOrders.pop()
	finishedSandwiches.append(workingOrder)
	print("I made your " + workingOrder)
	
print("\n----Completed Orders----\n")
for sandwich in finishedSandwiches:
	print("\t" + sandwich)
	
