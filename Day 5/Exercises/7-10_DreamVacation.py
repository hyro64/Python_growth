responses = {}

# Set a flag to indicate the termination.
activePoll = True

while True:							#takes the responses and stores it
	userName = input("What is your name?\n")
	print("If you could visit one place in the world.")
	response = input("Where would you go?\n")
	
	responses[userName] = response			#Uses responses and name to store in responses
	
	repeat = input("Would you like to let another person take the poll?(Yes/No)")
	if repeat == 'no':
		break #activePoll = False					#Stops the while loop from continuing if input is no

print("\n--------Poll Results----------\n")		#Prints the response
for name, response in responses.items():
	print(name.title() + " would like to vacation in " + response.title()
	 + ".")
