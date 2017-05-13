import re

def check_nonbrack(line):
	t_value = False
	for index in range(len(line)-3):
		if (line[index] + line[index+1] == line[index+3] + line[index+2]) and (line[index] != line[index+1]):
			t_value = True
			print(line[index] + line[index+1] + line[index+2] + line[index+3])
			break
		else:
			pass
	return(t_value)

def check_brack(line):
	t_value = True
	for index in range(len(line)-3):
		if (line[index] + line[index+1] == line[index+3] + line[index+2]) and (line[index] != line[index+1]):
			t_value = False
			print(line[index] + line[index+1] + line[index+2] + line[index+3])
			break
		else:
			pass
	return(t_value)

def parse_data(file):
	count = 0
	with open(file) as f:
		for line in f:
			line_list = []
			line_list.append(re.sub(r'\[\w+\]', ' ', line))
			line_list.append(' '.join(re.findall(r'\[\w+\]', line)))
			if check_nonbrack(line_list[0]) == True and check_brack(line_list[1]) == True:
				count += 1
	return(count)

print(parse_data('data.txt'))