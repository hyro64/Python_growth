# In this exercise the program it replaces the data strin "python" with
# "C"
fileName = "learning_python.txt"

with open(fileName) as fObj:
	lines = fObj.readlines()
	
pyString = ''

for line in lines:
	pyString += line.strip().replace('python','C') + "\n"
	

print(pyString)
