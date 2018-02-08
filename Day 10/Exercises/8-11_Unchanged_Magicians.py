def showMagicians(unchangedMagicianNames):
	'''Takes a list and compiles the list in print function.'''
	print("\nThe following magicians are: ")
	for magician in unchangedMagicianNames:
		print(magician)
		
def make_great(unchangedMagicianNames,greatMagicians):
	"""Adds 'The great' to each magician"""
	while unchangedMagicianNames:
		greatMagician = "The great " + unchangedMagicianNames.pop()
		greatMagicians.append(greatMagician)

unchangedMagicianNames = ['penn','teller','blaine','angel']
greatMagicians = []

showMagicians(unchangedMagicianNames[:])
make_great(unchangedMagicianNames[:],greatMagicians)
showMagicians(greatMagicians)
