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
		temp_out += num[(digit + int(shift_num)) % len(num)]
	return(temp_out)

def r_shift(num,shift_num):
	temp_out = ''
	for digit in range(len(num)):
		temp_out += num[(digit - int(shift_num)) % len(num)]
	return(temp_out)

def parse_line(line):
	if 'AND' in line:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[0]) == None or re.search(r'\d+', stuff_list[2]) == None:
			pass
		else:
			num1 = stuff_list[0]
			num2 = stuff_list[2]
			dictionary[stuff_list[3]] = bit_and(num1,num2)
	elif 'OR' in line:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[0]) == None or re.search(r'\d+', stuff_list[2]) == None:
			pass
		else:
			num1 = stuff_list[0]
			num2 = stuff_list[2]
			dictionary[stuff_list[3]] = bit_or(num1,num2)
	elif 'RSHIFT' in line:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			num = stuff_list[0]
			shift_num = stuff_list[2]
			dictionary[stuff_list[3]] = r_shift(num,shift_num)
	elif 'LSHIFT' in line:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			num = stuff_list[0]
			shift_num = stuff_list[2]
			dictionary[stuff_list[3]] = l_shift(num,shift_num)
	elif 'NOT' in line:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[1]) == None:
			pass
		else:	
			num = stuff_list[1]
			dictionary[stuff_list[2]] = bit_complement(num)
	else:
		stuff_list = re.findall(r'\w+',line)
		if re.search(r'\d+', stuff_list[0]) == None:
			pass
		else:
			dictionary[stuff_list[1]] = stuff_list[0]

print(bit_to_number('10001'))

parse_line('10000011 LSHIFT 3 -> ls')
try:
	print(dictionary['ls'])
except:
	print("Oops")

with open('directions.txt') as f:
	for line in f:
		if re.search(r'^\d+ -> \w+',line):
			print(line)
