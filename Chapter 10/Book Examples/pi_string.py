"""# Ver 3.0
# this version check to see if the input appears in the data specified
# After searching through the data it prints accordingly
fileName = "pi_million_digits.txt"

with open(fileName) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
		
for line in lines:
	pi_string += line. strip()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
"""

"""# Ver 2.0
# This version of this program creates the same methods and string as 
# the previous version
# The difference is that it only prints the the first 52 digits  

fileName = "pi_million_digits.txt"

with open(fileName) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
		
for line in lines:
	pi_string += line. strip()
	
print(pi_string[:52])
print("\nThe lenght of the text file is "+str(len(pi_string)))
"""

"""# Ver. 1.0 
# The method ".readlines()" is a python library method.
# The open method adds to the varible lines
# We create a string and add the data line by line to the string while
# striping the new line in the data of the text
# We then print the entire string and the lenght of the string

filename = "pi_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
		
for line in lines:
	pi_string += line. strip()
	
print(pi_string)
print("\nThe lenght of the text file is "+str(len(pi_string)))
 """
