keypad = {0+2j:'1', -1+1j:'2', 0+1j:'3', 1+1j:'4', -2+0j:'5',-1+0j:'6', 0+0j:'7', 1+0j:'8', 2+0j:'9', -1-1j:'A', 0-1j:'B', 1-1j:'C', 0-2j:'9'}

moves = {'U': 0+1j, 'R':1+0j, 'D':0-1j, 'L':-1+0j}

current_position = -2+0j

code =''

def make_move(position,direction):
	temp_pos = position + moves[direction]
	if abs(temp_pos.real) + abs(temp_pos.imag) < 3:
		return(temp_pos)
	else:
		return(position)

with open('combo.txt') as f:
	for line in f:
		for letter in line:
			if letter == '\n':
				break
			else:
				current_position = make_move(current_position,letter)
		code += (keypad[current_position])


print(code)