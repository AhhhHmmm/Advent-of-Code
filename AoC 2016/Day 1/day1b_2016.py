direct_dictionary = {'R':-1j,'L':1j}

current_position = 0+0j
current_direction = 1j

current_info = [0+0j,1j]

positions = []
direction_list = []

def new_Directions(file_name):
	with open(file_name) as f:
		with open('new_direction.txt', 'w') as g:
			for line in f:
				line = line.split(', ')
				for command in line:
					n_times = int(command[1:])
					print(command[0],file=g)
					for num in range(n_times):
						print(1,file=g)

def move(current_info, command):
	if command == '1':
		current_info[0] = current_info[0] + 1*current_info[1]
		return(current_info)
	elif command == 'R':
		current_info[1] = -1j*current_info[1]
		return(current_info)
	elif command == 'L':
		current_info[1] = 1j*current_info[1]
		return(current_info)

def file_to_list(file_name):
	with open(file_name) as f:
		for line in f:
			direction_list.append(line.strip())


new_Directions('directions.txt')
file_to_list('new_direction.txt')

n = 0
while (current_info[0] not in positions [:-1] and n < len(direction_list)):
	positions.append(current_info[0])
	current_info = move(current_info, direction_list[n])
	#print(current_info)
	n += 1


print(abs(current_info[0].real) + abs(current_info[0].imag))


#with open('directions.txt') as f:
#	for line in f:
#		line = line.split(',')
#		for direction in line:
#			direction = direction.strip()
#			print(direction)
#			current_direction = current_direction*direct_dictionary[direction[0]]
#			for vals in range(int(direction[1:])):
#				current_position = current_position + current_direction
#				print(current_position)
#				if current_position in positions:
#					break
#				else:
#					positions.append(current_position)
#			if current_position in positions[:-1]:
#				break
#print(abs(current_position.real)+abs(current_position.imag))
