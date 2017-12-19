#Store information about pizza being ordered
pizza = {
	'crust':'thick',
	'toppings':['mushrooms', 'extra cheese'],
	
	}
#Summarize your order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the follwing toppings:")
	
for topping in pizza['toppings']:
	print("\t" + topping)

