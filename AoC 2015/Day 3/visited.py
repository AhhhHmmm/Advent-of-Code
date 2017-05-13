move_vals = {'^':(0+1j),'v':(0-1j),'>':(1+0j),'<':(-1+0j)}

starting_pos = 0+0j
current_pos = starting_pos
visited = {starting_pos}

with open('santa_path.txt') as f:
	for line in f:
		for char in line:
			current_pos = current_pos + move_vals[char]
			current_pos_set = {current_pos}
			visited = visited | current_pos_set

print(len(visited))