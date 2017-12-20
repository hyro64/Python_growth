age = 0
prompt = "Enter your age for the movie tickets: "

active = True

while active:
	age = input(prompt)
	age = int(age)
	if age == -1:
		continue
	if age <= 3:
		print("Your addmission is free.")
	elif age <= 13:
		print("Your addmission is 10 dollars.")
	else:
		print("Your addmission is 15 dollars.")
