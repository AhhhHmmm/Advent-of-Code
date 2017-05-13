keypad = {-1+1j:'1', 0+1j:'2', 1+1j:'3', -1+0j:'4', 0+0j:'5',1+0j:'6', -1-1j:'7',0-1j:'8',1-1j:'9'}

moves = {'U': 0+1j, 'R':1+0j, 'D':0-1j, 'L':-1+0j}

current_position = 0+0j

code =''

def make_move(position,direction):
	temp_pos = position + moves[direction]
	if abs(temp_pos.real) < 2 and abs(temp_pos.imag) < 2:
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