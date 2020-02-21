my_foods = ["Pizza","Steak","Lassanga","Scrambled Eggs","Cheese",
"Beef Wellington","Ice cream","Cereal","Crepes"]

print("The first three items in the list are: ")
for food in my_foods[:3]:
	print(food.title())

print("\nThe middle three items in the list are: ")
for food in my_foods[3:6]:
	print(food.title())

print("\nThe last three items in the list are: ")
for food in my_foods[-3:]:
	print(food.title())
