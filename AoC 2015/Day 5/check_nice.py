#test_message = input("Test message: ")


def checkVowels(message):
	vowels = 0
	for letter in message:
		if letter in ['a','e','i','o','u']:
			vowels += 1
	if vowels >= 3:
		return(True)
	else:
		return(False)

def checkDoubles(message):
	num = 0
	check_double_letter = False
	while (num < len(message)-1 and check_double_letter == False):
		if message[num] == message[num+1]:
			check_double_letter = True
			num += 1
			break
		else:
			num += 1
	return(check_double_letter)

def checkBadPairs(message):
	num = 0
	bad_pairs = ['ab','cd','pq','xy']
	check_bad_pairs = True
	while (num < len(message)-1 and check_bad_pairs):
		if (message[num] + message[num+1]) in bad_pairs:
			check_bad_pairs = False
			num += 1
			break
		else:
			num += 1
	return(check_bad_pairs)

def checkAll(message):
	if (checkDoubles(message) and checkBadPairs(message) and checkVowels(message)):
		return(True)
	else:
		return(False)

count_nice = 0

with open('santa_list.txt') as f:
	for line in f:
		count_nice += checkAll(line)

print(count_nice)



