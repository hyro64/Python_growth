prompt = "\nTell me something. I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program\n"

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
		print("Program terminated")
		
	else:
		print(message)
