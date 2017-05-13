import re

def check_non_bracks(line):
	non_bracks = re.sub(r'\[\w+\]', ' ', line)
	aba_list = []
	for val in range(len(non_bracks)-2):
		if non_bracks[val] != ' ' and non_bracks[val+1] != ' ' and non_bracks[val] == non_bracks[val+2] and non_bracks[val] != non_bracks[val+1]:
			aba_list.append(non_bracks[val] + non_bracks[val+1] + non_bracks[val+2])
	return(aba_list)

def check_bracks(line):
	bracks = ' '.join(re.findall(r'\[\w+\]', line))
	aba_list = []
	for val in range(1,len(bracks)-2):
		if bracks[val] != ' ' and bracks[val+1] != ' ' and bracks[val] == bracks[val+2] and bracks[val] != bracks[val+1]:
			aba_list.append(bracks[val] + bracks[val+1] + bracks[val+2])
	return(aba_list)

def compare_list(line):
	test = 0
	for item in check_non_bracks(line):
		bab_of_aba = item[1] + item[0] + item[1]
		if bab_of_aba in check_bracks(line):
			test = 1
	return(test)

def parse_data(file):
	count = 0
	with open(file) as f:
		for line in f:
			print(line)
			count += compare_list(line)
	return(count)

#with open('data.txt') as f:
#		for line in f:
#			print(check_bracks(line))

print(parse_data('data.txt'))