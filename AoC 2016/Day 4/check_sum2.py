import re
import collections
import string

def parse_line(line):
	parsed = []
	number = int(re.findall('\d+',line)[0])
	checksum = re.findall('\[\w+\]',line)[0]
	checksum = checksum[1:-1]
	code = line.replace(str(number),'')
	code = code.replace(checksum,'')
	code = code.split('-')
	code = "".join(code)[:-3]
	parsed = [code,number,checksum]
	return(parsed)

def parse_line2(line):
	parsed = []
	number = int(re.findall('\d+',line)[0])
	checksum = re.findall('\[\w+\]',line)[0]
	checksum = checksum[1:-1]
	code = line.replace(str(number),'')
	code = code.replace(checksum,'')
	code = code[:-3]
	parsed = [code,number,checksum]
	return(parsed)

def process_code(code):
	ordered_letters = ''
	count = collections.Counter(code)
	count = collections.OrderedDict(sorted(count.items(),key=lambda t: (-t[1], t[0])))
	for key in count.keys():
		ordered_letters += key
	return(ordered_letters[0:5])

def decode(line, shift):
	alph = string.ascii_lowercase
	decoded_line = ''
	for char in line:
		if char == '-':
			decoded_line += ' '
		else:
			new_position = (alph.index(char) + shift) % 26
			decoded_line += alph[new_position]
	return(decoded_line)

with open('room_codes.txt') as f:
	with open('good_room_codes.txt', 'w') as g:
		for line in f:
			#print(line.strip())
			#print(parse_line(line))
			#print()
			temp_line = parse_line(line)
			temp_line[0] = process_code(temp_line[0])
			if temp_line[0] == temp_line[2]:
				print(line.strip(), file=g)
			else:
				pass


with open('good_room_codes.txt') as f:
	with open('decoded_good_codes.txt', 'w') as g:
		for line in f:
			processed_line = parse_line2(line)
			decoded_line = decode(processed_line[0],processed_line[1])
			print(decoded_line + ' ' + str(processed_line[1]), file=g)

with open('decoded_good_codes.txt') as f:
	for line in f:
		if 'northpole object storage' in line:
			print(re.findall('\d+', line))
			break
		else:
			pass

#line = parse_line2('xmtjbzidx-ytz-nojmvbz-525[hyzbw]')
#print(line)