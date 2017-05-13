import re
import collections

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

def process_code(code):
	ordered_letters = ''
	count = collections.Counter(code)
	count = collections.OrderedDict(sorted(count.items(),key=lambda t: (-t[1], t[0])))
	for key in count.keys():
		ordered_letters += key
	return(ordered_letters[0:5])

total_sum = 0

with open('room_codes.txt') as f:
	for line in f:
		#print(line.strip())
		#print(parse_line(line))
		#print()
		temp_line = parse_line(line)
		temp_line[0] = process_code(temp_line[0])
		if temp_line[0] == temp_line[2]:
			total_sum += temp_line[1]
		else:
			pass

print(total_sum)

#line = parse_line('xmtjbzidx-ytz-nojmvbz-525[hyzbw]')
#print(line)
#print(process_code('xmtjbzidxytznojmvbz'))