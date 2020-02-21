#This program looks for the file within the file location it is located

filename = "pi_digits.txt"

#ver 3.0
with open(filename) as file_object:
		lines = file_object.readlines()
		
for line in lines:
	print(line.rstrip())

#ver 2.0
#This reads each line in the file. ".rstrip" takes the newline out 
#with open(filename) as file_object:
	#for line in file_object:
		#print(line.rstrip())

#ver 1.0
#.read() does exactly what is says
#with open("pi_digits.txt") as file_object:
	#contents = file_object.read()          
	#print(contents.rstrip())
