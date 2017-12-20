current_number = 0

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue # this skips the print statement if divisible
	print(current_number)
