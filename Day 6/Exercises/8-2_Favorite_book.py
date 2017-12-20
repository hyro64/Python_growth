def favoriteBook(title):
	"""Function that diplays the title of a book"""
	
	print("\nOne of my favorite books is " + title.title() + "!")
##################################################################

#main

bookTitle = input("What is your favorite book?\n")	
favoriteBook(bookTitle)
