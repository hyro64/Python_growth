fileName = 'programming.txt'

with open(fileName, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.")
	file_object.close()
	
