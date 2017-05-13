move_vals = {'^':(0+1j),'v':(0-1j),'>':(1+0j),'<':(-1+0j)}
index = 1


starting_pos = 0+0j
norm_current_pos = starting_pos
robo_current_pos = starting_pos
norm_visited = {starting_pos}
robo_visited = {starting_pos}



with open('santa_path.txt') as f:
	for line in f:
		for char in line:
			if index % 2 == 1:
				norm_current_pos = norm_current_pos + move_vals[char]
				norm_current_pos_set = {norm_current_pos}
				norm_visited = norm_visited | norm_current_pos_set
			else:
				robo_current_pos = robo_current_pos + move_vals[char]
				robo_current_pos_set = {robo_current_pos}
				robo_visited = robo_visited | robo_current_pos_set
			index += 1

tot_visited = norm_visited | robo_visited

print(len(tot_visited))