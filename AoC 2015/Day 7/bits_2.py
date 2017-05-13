import re

dictionary = {}

def convert_to_bit(string_num):
	digits = ''
	num = int(string_num)
	for power in [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]:
		digit = num//(2**power)
		num -= digit*(2**power)
		digits += str(digit)
	return(digits)

def bit_to_number(string_num):
	final_number = 0
	for index in range(0,len(string_num)):
		digit = int(string_num[index])*2**(len(string_num)-index-1)
		final_number += digit
	return(str(final_number))

def bit_and(num1,num2):
	temp_out = ''
	for digit in range(len(num1)):
		if num1[digit] == '1' and num2[digit] == '1':
			temp_out += '1'
		else:
			temp_out += '0'
	return(temp_out)

def bit_or(num1,num2):
	temp_out = ''
	for digit in range(len(num1)):
		if num1[digit] == '1' or num2[digit] == '1':
			temp_out += '1'
		else:
			temp_out += '0'
	return(temp_out)

def bit_complement(num):
	temp_out = ''
	for digit in range(len(num)):
		temp_out += str((int(num[digit])+1)%2)
	return(temp_out)

def l_shift(num,shift_num):
	temp_out = ''
	for digit in range(len(num)):
		try:
			temp_out += num[(digit + int(shift_num))]
		except:
			temp_out += '0'
	return(temp_out)

def r_shift(num,shift_num):
	for iteration in range(int(shift_num)):
		temp_out = ''
		temp_out += num[0]
		for digit in range(1,len(num)):
			temp_out += num[digit-1]
		num = temp_out
	return(num)

def parse_line(line):
	if 'AND' in line:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[0]) == None:
			pass
		else:
			stuff_list[0] = dictionary.get(stuff_list[0])
		if dictionary.get(stuff_list[2]) == None:
			pass
		else:
			stuff_list[2] = dictionary.get(stuff_list[2])
		if re.search(r'\d+', stuff_list[0]) == None or re.search(r'\d+', stuff_list[2]) == None:
			pass
		else:
			num1 = convert_to_bit(stuff_list[0])
			num2 = convert_to_bit(stuff_list[2])
			dictionary[stuff_list[3]] = bit_to_number(bit_and(num1,num2))
	elif 'OR' in line:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[0]) == None:
			pass
		else:
			stuff_list[0] = dictionary.get(stuff_list[0])
		if dictionary.get(stuff_list[2]) == None:
			pass
		else:
			stuff_list[2] = dictionary.get(stuff_list[2])
		if re.search(r'\d+', stuff_list[0]) == None or re.search(r'\d+', stuff_list[2]) == None:
			pass
		else:
			num1 = convert_to_bit(stuff_list[0])
			num2 = convert_to_bit(stuff_list[2])
			dictionary[stuff_list[3]] = bit_to_number(bit_or(num1,num2))
	elif 'RSHIFT' in line:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[0]) == None:
			pass
		else:
			stuff_list[0] = dictionary.get(stuff_list[0])
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			num = convert_to_bit(stuff_list[0])
			shift_num = stuff_list[2]
			dictionary[stuff_list[3]] = bit_to_number(r_shift(num,shift_num))
	elif 'LSHIFT' in line:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[0]) == None:
			pass
		else:
			stuff_list[0] = dictionary.get(stuff_list[0])
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			num = convert_to_bit(stuff_list[0])
			shift_num = stuff_list[2]
			dictionary[stuff_list[3]] = bit_to_number(l_shift(num,shift_num))
	elif 'NOT' in line:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[1]) == None:
			pass
		else:
			stuff_list[1] = dictionary.get(stuff_list[1])
		if re.search(r'\d+', stuff_list[1]) == None:
			pass
		else:	
			num = convert_to_bit(stuff_list[1])
			dictionary[stuff_list[2]] = bit_to_number(bit_complement(num))
	else:
		stuff_list = re.findall(r'\w+',line)
		if dictionary.get(stuff_list[0]) == None:
			pass
		else:
			stuff_list[0] = dictionary.get(stuff_list[0])
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			dictionary[stuff_list[1]] = stuff_list[0]

#print(r_shift('00010111','1'))

print(dictionary)

counter = 0

while counter < 150:
	with open('part2_directions.txt') as f:
		for line in f:
			parse_line(line.strip())
			#print(dictionary)
	counter += 1

print(dictionary)
print(dictionary.get('a'))

