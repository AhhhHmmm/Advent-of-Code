direct_dictionary = {'R':-1j,'L':1j}

current_position = 0+0j
current_direction = 1j

with open('directions.txt') as f:
	for line in f:
		line = line.split(',')
		for direction in line:
			direction = direction.strip()
			print(direction)
			current_direction = current_direction*direct_dictionary[direction[0]]
			current_position = current_position + int(direction[1:])*current_direction
			print(current_position)

print(abs(current_position.real)+abs(current_position.imag))
