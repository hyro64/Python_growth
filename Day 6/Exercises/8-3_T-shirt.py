def makeShirt(size,message):
	"""Ask for a shirt size and message on the front"""
	print("Your shirt will be " + size.title() + " size.")
	print("the message on the front will be " + message.title()+ ".")
	
size = input("Please enter a size shirt:\n")
message = input("Please enter a message that will be on the shirt:\n")

makeShirt(size,message)

