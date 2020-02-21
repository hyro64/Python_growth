fileName = "learning_python.txt"

with open(fileName) as fObj:
	contents = fObj.read()
	print(contents)
	
with open(fileName) as fObj:
	for line in fObj:
		print(line.strip())

with open(fileName) as fObj:
	lines = fObj.readlines()
	
pyString = ''
for line in lines:
	pyString += line.strip() + "\n"
	

print("\n" + pyString)
