prompt = "\nTell me something. I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program\n"

message = ''
while message != 'quit':
	message = input(prompt)
	print(message)
	
	if message != 'quit':
		print(message)
