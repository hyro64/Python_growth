"""This program was modified from the original to 
add a quit funtion to all"""

########################################################################
import sys # used in corralation with the quit funtion below
def quit():
	"""This function exits the entire program"""
	sys.exit()
########################################################################
def get_formated_name(first_name,last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + '' + last_name
	return full_name.title()
########################################################################
# This is was an infinite loop
#main part of the program
while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		quit()
	
	l_name = input("Last name: ")
	if l_name == 'q':
		quit()
	
	formatted_name = get_formated_name(f_name, l_name)
	print("\nHello, "+formatted_name+"!")
