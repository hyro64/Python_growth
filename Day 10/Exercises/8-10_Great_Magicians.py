def showMagicians(magicianNames):
	'''Takes a list and compiles the list in print function.'''
	print("\nThe following magicians are: ")
	for magician in magicianNames:
		print(magician)
def make_great(greatMagicians):
	"""Adds 'The great' to each magician"""
	while magicianNames:
		greatMagician = magicianNames.pop()
		print("The great " + greatMagician)
		greatMagicians.append(greatMagician)
magicianNames = ['penn','teller','blaine','angel']
greatMagicians = []
showMagicians(magicianNames[:])
make_great(greatMagicians)
showMagicians(greatMagicians)
