floor = 0

input_text = 'santa_route.txt'

with open(input_text) as f:
	for line in f:
		for char in line:
			if char == '(':
				floor +=1
			elif char == ')':
				floor -=1

print(floor)
