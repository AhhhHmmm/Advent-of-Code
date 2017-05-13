floor = 0
n = 0

input_text = 'santa_route.txt'

with open(input_text) as f:
	for line in f:
		for char in line:
			if floor >= 0:	
				if char == '(':
					floor +=1
					n += 1
				elif char == ')':
					floor -=1
					n += 1
			else:
				print(floor)
				print(n)
				exit()

print(floor)