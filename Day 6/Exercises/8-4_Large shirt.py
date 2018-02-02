def makeShirt(size = 'Large',message = 'I love python'):
	"""Ask for a shirt size and message on the front"""
	print("Your shirt will be " + size.title() + " size.")
	print("the message on the front will be " + message.title()+ ".")
	
makeShirt()

size = input("Please enter a size shirt:\n")
message = input("Please enter a message that will be on the shirt:\n")
makeShirt(size,message)

