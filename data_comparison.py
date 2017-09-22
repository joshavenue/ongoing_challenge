data_A = []
data_B = []
count = 0

while True:

	add_data_A = int(input('Enter numbers between 0 - 100 : '))
	add_data_B = int(input('Enter numbers between 0 - 100 : '))
	count += 1

	if add_data_A < 0 or add_data_A > 100:
		del add_data_A[count]
		print('Invalid input.')
		count -= 1
	elif add_data_B < 0 or add_data_B > 100:
		del add_data_B[count]
		print('Invalid input.')
		count -= 1
	else:
		data_A.append(add_data_A)
		data_B.append(add_data_B)
		pass

	ask = str(input('Add new data? y/n'))
	
	if ask.lower() == 'n':
		break
	else:
		continue 

for x in data_A:
	for y in data_B:
		if x != y:
			data_A.append(x)
	else:
		pass

print(seen)
