prompt = ("Please enter the toppings you want on your pizza.")
prompt += "\n(Enter 'quit' when you are finished.)\n"

pizzaToppings = [] 						#A list for the toppings
active = True	   						#A variable for the termination

while active:
	topping = input(prompt) 			#Shows and ask for the topping
	pizzaToppings.append(topping)		#Adds the topping to the list
	 
	if topping == 'quit':				#Stops the program
		pizzaToppings.remove(topping)	#Removes quit from the list
		print("The following toppings were added:") 

		for userTopping in pizzaToppings:	
			print("\t" + userTopping.title())	#prints the list
			
		active = False
		break
	else:
		print("You got it, " + topping + " has been added.\n")
