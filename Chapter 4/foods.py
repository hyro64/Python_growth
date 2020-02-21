my_foods = ["Pizza","Falafel","Carrot cake"]
friend_foods = my_foods[:]

my_foods.append("Cannoli")
friend_foods.append("Ice Cream")

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friends favorite foods are:")	
for food in friend_foods:
	print(food)
