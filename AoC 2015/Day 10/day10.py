
#start = '1'
start = '1321131112'
iterations = 50;

def look_and_say(seq):
	final_seq = ''
	temp_seq = seq
	while temp_seq:
		working_value = temp_seq[0]
		temp_seq = temp_seq[1:]
		count = 1
		for char in temp_seq:
			if char == working_value:
				count += 1
				temp_seq = temp_seq[1:]
			else:
				break
		final_seq += str(count)
		final_seq += working_value
		
	return final_seq

index = 0
seq = start
while index < iterations:
	index += 1
	print('Computing iteration ' + str(index) + '...')
	seq = look_and_say(seq)
	print('\tLength is: ' + str(len(seq)))
	

print(len(seq))

