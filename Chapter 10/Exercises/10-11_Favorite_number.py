import json
# loads the number in the stored in the  file Somewhere

fileName = 'userNumber.json'

try:
	with open(fileName) as fObj:
		userNumber = json.load(fObj)
		
except FileNotFoundError:
	userNumber = input("What is your fucking favorite number?\n")
	with open(fileName, 'w') as fObj:
		json.dump(userNumber1, fObj)
		#fObj.write(fileName)
		print("Got your fucking number. It is " + userNumber + "!")

else:
	print("I still remember your fucking number it is " + userNumber + "!")
