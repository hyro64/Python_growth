pizzas = ["Bacon","Sausage","Supreme"]

for pizza in pizzas:
	print("I like " + pizza + " pizza.\n")

print("I fucking love pizza.\n")

friendsPizza = pizzas[:]

pizzas.append("Hawaian")

friendsPizza.append("Cheese")

print("My favorite pizzas are:")
	
for pizza in pizzas:
	print(pizza)	

print("\nMy friends favorite pizzas are:")

for pizza in friendsPizza:
	print(pizza)
