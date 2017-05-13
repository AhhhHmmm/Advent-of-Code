check_list = []

with open('check.txt') as f:
	for line in f:
		check_list.append(line)

check_list.count('value')